import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()


# Insert functions

def insertCNAMEpacketsEntry(domainName, sourceAddress, CNAMEAlias, hasAType):
    cur.execute("INSERT INTO CNAMEpackets VALUES (?, ?, ?, ?)", (domainName, sourceAddress, CNAMEAlias, hasAType))
    return

def insertIpEntry(domainName, ip):
    cur.execute("INSERT INTO ip VALUES (?, ?)", (domainName, ip))
    return

def insertCookieEntry(domainName, src_ip, domain_setting, httponly, secure):
    cur.execute("INSERT INTO cookie VALUES (?, ?, ?, ?, ?)", (domainName, src_ip, domain_setting, httponly, secure))
    return

# Fetch functions

def fetchDomainFromAlias(CNAMEAlias):
    cur.execute("SELECT domainName FROM CNAMEpackets WHERE CNAMEAlias = ?", (CNAMEAlias,))
    result = cur.fetchall()
    return result

def fetchIpFromDomain(domainName):
    cur.execute("SELECT ip FROM ip WHERE domainName = ?", (domainName,))
    result = cur.fetchall()
    return result

def fetchATypeRecordsFromDomain(domainName):
    cur.execute("SELECT hasAType FROM CNAMEpackets WHERE domainName = ?", (domainName,))
    result = cur.fetchall()
    return result


conn.commit()
conn.close()