import sqlite3
con = sqlite3.connect("database.db")
domainName = "t"
sourceAddress = "r"
CNAMEAlias = "e"
hasAType = 0
con.execute("INSERT INTO CNAMEpackets VALUES (?, ?, ?, ?, ?)", (domainName, sourceAddress, CNAMEAlias, hasAType, None))
con.commit()
print(con.execute("SELECT * FROM CNAMEpackets WHERE originalURL IS NULL").fetchall())
con.execute("UPDATE CNAMEpackets SET originalURL='hey.com' WHERE originalURL IS NULL")
con.commit()
print(con.execute("SELECT * FROM CNAMEpackets WHERE originalURL IS NULL").fetchall())
con.close()
