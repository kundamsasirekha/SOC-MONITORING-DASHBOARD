import sqlite3

conn = sqlite3.connect("soc.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM profile")

conn.commit()
conn.close()

print("Profile data deleted successfully.")