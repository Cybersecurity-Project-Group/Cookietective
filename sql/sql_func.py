import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()


''' The table has the following columns
cur.execute("""CREATE TABLE CNAMEpackets (
    domainName text,
    sourceAddress text,
    CNAMEAlias text,
    hasAType int
    )""")
'''

def insertCNAMEpacketsEntry(domainName, sourceAddress, CNAMEAlias, hasAType):
    cur.execute("INSERT INTO packets VALUES (?, ?, ?)", (domainName, sourceAddress, CNAMEAlias, hasAType))
    return

def fetchEntryWebsite(website):
    cur.execute("SELECT * FROM packets WHERE website = ?", (website,))
    result = cur.fetchall()
    print(result)
    return result


conn.commit()
conn.close()