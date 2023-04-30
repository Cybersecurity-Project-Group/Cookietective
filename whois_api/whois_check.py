import sys
import socket
from datetime import datetime as dt

import time
import sqlite3

def get_whois_data(ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("whois.arin.net", 43))
    s.send(('n ' + ip + '\r\n').encode())

    response = b""

    # setting time limit in secondsmd
    startTime = time.mktime(dt.now().timetuple())
    timeLimit = 3
    while True:
        elapsedTime = time.mktime(dt.now().timetuple()) - startTime
        data = s.recv(4096)
        response += data
        if (not data) or (elapsedTime >= timeLimit):
            break
    s.close()

    return response.decode()

def findOrgName(whoisString):
    orgNameIndex = whoisString.find("OrgName")
    orgNameEnd = whoisString.find("OrgId")
    orgName = whoisString[orgNameIndex+16:orgNameEnd]
    return orgName


def compareWhois(rowNum, database): # given the row number of the table, compare the domain that belongs to the
    conn = sqlite3.connect(database)
    cur = conn.cursor()

    # Execute the SELECT statement to retrieve the domainName and originalURL values for a specific row
    cur.execute("SELECT domainName, originalURL FROM CNAMEpackets WHERE rowid = ?", (rowNum,))

    # Fetch the result set and retrieve the values
    row = cur.fetchone()
    domainName = row[0].decode()
    originalURL = row[1]

    print("Domain Name: " + domainName)
    print("Original URL: " + originalURL)

    # reset the event object
    whoisFound.clear()

    # Pull data from Whois
    domainNameWhoisThread = threading.Thread(target=get_whois_data, args=(domainName,))
    domainNameWhoisThread.start()
    whoisFound.wait()
    domainNameWhois = whoisData
    print(domainNameWhois.org)

    # reset the event object
    domainNameWhoisThread.join()
    whoisFound.clear()

    # pull data from Whois for other thread
    originalURLWhoisThread = threading.Thread(target=get_whois_data, args=(originalURL,))
    originalURLWhoisThread.start()
    whoisFound.wait()
    originalURLWhois = whoisData
    print(originalURLWhois.org)

    # reset these
    originalURLWhoisThread.join()
    whoisFound.clear()

    returnVal = 0
    if domainNameWhois is None or originalURLWhois is None:
        returnVal = 2

    # If the organizations are the same, write one to database and return 1
    elif domainNameWhois.org == originalURLWhois.org:
        # Update the whoisAnalysis value to 1 for the row with the specified rowid value
        #cur.execute("UPDATE CNAMEpackets SET whoisAnalysis = ? WHERE rowid = ?", (1, rowNum))
        returnVal = 1

    # If they are not the same, return 0
    elif domainNameWhois.org != originalURLWhois.org:
        # Update the whoisAnalysis value to 0 for the row with the specified rowid value
        #cur.execute("UPDATE CNAMEpackets SET whoisAnalysis = ? WHERE rowid = ?", (0, rowNum))
        returnVal = 0

    conn.commit()
    conn.close()
    return returnVal
