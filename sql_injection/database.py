import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS USERS (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               username TEXT,
               password TEXT
               )
"""
               )

conn.commit()

# print("Table created")


# cursor.execute("""
# INSERT INTO users(username, password)
# VALUES('admin', '1234')
# """)

conn.commit()
# print("test user inserted")

# conn.execute("DROP TABLE users")


# username = "admin"
# password = "234"

# username= input("username")
# password = input("password")


#unsecure version 
def login_unsecure(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    qt = f"""
    SELECT * FROM users 
    WHERE username = '{username}' AND password = '{password}'
    """
    cursor.execute(qt)
    result = cursor.fetchone()
    conn.close()
    return result



#secure version
def login_secure(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    cursor.execute("""
    SELECT * FROM users 
    WHERE username = ? AND password = ?""", (username, password))
    qw = cursor.fetchone()
    conn.close()
    return qw





