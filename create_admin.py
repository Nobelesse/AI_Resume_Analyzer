import sqlite3
import bcrypt

from database.db import initialize_database

# Create database and tables first
initialize_database()

conn = sqlite3.connect(
    "database/resume_analyzer.db"
)

cursor = conn.cursor()

password = bcrypt.hashpw(
    "admin123".encode(),
    bcrypt.gensalt()
).decode()

cursor.execute("""
INSERT OR IGNORE INTO users
(name,email,password,role)
VALUES
(
'Administrator',
'testuser@gmail.com',
?,
'Test@123'
)
""", (password,))

conn.commit()
conn.close()

print("Admin Created Successfully")