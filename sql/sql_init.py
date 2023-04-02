import sqlite3

conn = sqlite3.connect('savedpackets.db')
cur = conn.cursor()

# Initialize the table
cur.execute("""CREATE TABLE packets (
    website text,
    IP blob,
    vulnerability text
    )""")

conn.commit()
conn.close()