import sqlite3

conn = sqlite3.connect('savedpackets.db')
cur = conn.cursor()

def addEntry(website, ip, vulnerability):
    cur.execute("INSERT INTO packets VALUES (?, ?, ?)", (website, ip, vulnerability))
    return

def fetchEntryWebsite(website):
    cur.execute("SELECT * FROM packets WHERE website = ?", (website,))
    print(cur.fetchall())
    return


conn.commit()
conn.close()