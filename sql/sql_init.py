import sqlite3

conn = sqlite3.connect('savedpackets.db')
cur = conn.cursor()

# Initialize the table
cur.execute("""CREATE TABLE CNAMEpackets (
    domainName text,
    sourceAddress text,
    CNAMEAlias text,
    hasAType int
    )""")

conn.commit()
conn.close()