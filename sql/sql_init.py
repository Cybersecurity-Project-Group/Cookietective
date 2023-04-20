import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

# Initialize the CNAME table
cur.execute("""CREATE TABLE CNAMEpackets (
    domainName text,
    sourceAddress text,
    CNAMEAlias text,
    hasAType int
    )""")

# Initialize the IP table that stores IP packets associated with A-type packets
cur.execute("""CREATE TABLE ip (
    domainName text PRIMARY KEY NOT NULL,
    ip text NOT NULL
    )""")

# Initialize the cookie table that stores Set-Cookie information from MITMproxy
cur.execute("""CREATE TABLE cookie (
    domainName text PRIMARY KEY NOT NULL,
    src_ip text NOT NULL,
    domain_setting text NOT NULL,
    httponly int,
    secure int
    )""")

conn.commit()
conn.close()