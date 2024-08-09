import sqlite3

# Get user input
username = input("Enter username: ")
password = input("Enter password: ")

# Connect to the SQLite database
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

# Vulnerable query construction
query = f"SELECT username, password FROM logins WHERE username = '{username}' AND password = '{password}'"
cursor.execute(query)

# Fetch one result (if exists)
result = cursor.fetchone()

# Close the database connection
conn.close()

# Print the result if authentication is successful
if result:
    print(f"Username: {result[0]}")
    print(f"Password: {result[1]}")
# No output if the result is None (unsuccessful query)
