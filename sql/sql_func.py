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
    cur.execute("INSERT INTO CNAMEpackets VALUES (?, ?, ?, ?)", (domainName, sourceAddress, CNAMEAlias, hasAType))
    return

def fetchDomainFromAlias(CNAMEAlias):
    cur.execute("SELECT domainName FROM CNAMEpackets WHERE CNAMEAlias = ?", (CNAMEAlias,))
    result = cur.fetchall()
    print(result)
    return result


conn.commit()
conn.close()