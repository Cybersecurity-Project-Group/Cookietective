from time import sleep

import whois
import sqlite3

def compareWhois(rowNum): # given the row number of the table, compare the domain that belongs to the
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    # Execute the SELECT statement to retrieve the domainName and originalURL values for a specific row
    cur.execute("SELECT domainName, originalURL FROM CNAMEpackets WHERE rowid = ?", (rowNum,))

    # Fetch the result set and retrieve the values
    row = cur.fetchone()
    domainName = row[0]
    originalURL = row[1]

    # Pull data from Whois
    domainNameWhois = whois.whois(domainName)
    sleep(.7) # maybe try to remove this?
    originalURLWhois = whois.whois(originalURL)

    print(domainNameWhois.org)
    print(originalURLWhois.org)

    returnVal = 0

    # If the organizations are the same, write one to database and return 1
    if domainNameWhois.org == originalURLWhois.org:
        # Update the whoisAnalysis value to 1 for the row with the specified rowid value
        cur.execute("UPDATE CNAMEpackets SET whoisAnalysis = ? WHERE rowid = ?", (1, rowNum))
        returnVal = 1

    # If they are not the same, return 0
    elif domainNameWhois.org != originalURLWhois.org:
        # Update the whoisAnalysis value to 0 for the row with the specified rowid value
        cur.execute("UPDATE CNAMEpackets SET whoisAnalysis = ? WHERE rowid = ?", (0, rowNum))
        returnVal = 0

    conn.commit()
    conn.close()
    return returnVal