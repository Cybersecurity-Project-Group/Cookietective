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
    print(result)
    
    conn.commit()
    conn.close()
    return result
