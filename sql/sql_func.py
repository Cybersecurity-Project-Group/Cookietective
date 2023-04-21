import sqlite3

# Insert functions
def insertCNAMEpacketsEntry(domainName, sourceAddress, CNAMEAlias, hasAType):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO CNAMEpackets VALUES (?, ?, ?, ?)", (domainName, sourceAddress, CNAMEAlias, hasAType))
    conn.commit()
    conn.close()
    return

def insertIpEntry(domainName, ip):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO ip VALUES (?, ?)", (domainName, ip))
    
    conn.commit()
    conn.close()
    return

def insertCookieEntry(domainName, src_ip, domain_setting, httponly, secure):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO cookie VALUES (?, ?, ?, ?, ?)", (domainName, src_ip, domain_setting, httponly, secure))
    
    conn.commit()
    conn.close()
    return

# Fetch functions

def fetchDomainFromAlias(CNAMEAlias):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("SELECT domainName FROM CNAMEpackets WHERE CNAMEAlias = ?", (CNAMEAlias,))
    result = cur.fetchall()

    conn.commit()
    conn.close()
    return result

def fetchIpFromDomain(domainName):
    cur.execute("SELECT ip FROM ip WHERE domainName = ?", (domainName,))
    result = cur.fetchall()
    return result

def fetchATypeRecordsFromDomain(domainName):
    cur.execute("SELECT hasAType FROM CNAMEpackets WHERE domainName = ?", (domainName,))
    result = cur.fetchall()

    return result
