import sqlite3

conn = sqlite3.connect("soc.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS profile(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone TEXT,
    department TEXT
)
""")

conn.commit()
conn.close()

print("Profile Table Created Successfully")