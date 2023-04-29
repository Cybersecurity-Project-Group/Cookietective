import sqlite3
import socket
import sys
import tldextract
import whois
from url_checker import url_func
from sql import sql_func

def sameOwner(url1, url2):
    ext1 = tldextract.extract(url1)
    ext2 = tldextract.extract(url2)

    # check if the extracted top-level domains match
    if ext1.suffix == ext2.suffix:
        return True

    # if the top-level domains don't match, use the mostMatching function to check if they belong to the same owner
    matchCount, matches = mostMatching(url1, url2)

    # if there is only one matching domain and it is the top-level domain, assume they belong to the same owner
    if matchCount == 1 and matches[0] == ext1.suffix:
        return True

    # perform a WHOIS lookup for both domains and compare the registrant organization fields
    try:
        w1 = whois.whois(url1)
        w2 = whois.whois(url2)
        if w1.status == w2.status == None and w1.registrant_org == w2.registrant_org:
            return True
    except:
        pass

    return False



def get_ip_address(domain):
    ip_address = socket.gethostbyname(domain)
    return ip_address



def hasAType(domainName, dbFile='database.db'):
    conn = sqlite3.connect(dbFile)
    c = conn.cursor()
    c.execute("SELECT hasAType FROM CNAMEpackets WHERE domainName=?", (domainName,))
    result = c.fetchone()
    conn.close()
    if result is not None:
        return result[0]
    else:
        return None
        

def hasCNAMErecord(domainName, dbFile='database.db'):
    conn = sqlite3.connect(dbFile)
    c = conn.cursor()
    c.execute("SELECT EXISTS(SELECT 1 FROM CNAMEpackets WHERE domainName = ? LIMIT 1)", (domainName,))
    result = c.fetchone()[0]
    conn.close()
    return result
    
    

def firstPartyCheck(domainName, dbFile='database.db'):
    conn = sqlite3.connect(dbFile)
    c = conn.cursor()
    c.execute(f"SELECT CNAMEAlias FROM CNAMEpackets WHERE domainName='{domainName}'")
    result = c.fetchone()
    conn.close()

    if result is None:
        return 0

    cnameAlias = result[0]
    if sameOwner(domainName, cnameAlias):
        return 1
    else:
        return 0





