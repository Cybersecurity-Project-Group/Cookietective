#!/bin/bash

ids=$(docker ps -f "status=exited" -q)

# Iterate through all container id's
for id in $ids; do
    # Copy the database.db from the container into the current directory
    docker cp $id:/home/CoolestProject/database.db $id.db

    # Copy the data from the database into the current database
    sqlite3 database.db "ATTACH DATABASE '$id.db' AS results;"
    sqlite3 database.db "INSERT INTO CNAMEpackets SELECT * FROM results.CNAMEpackets;"
    sqlite3 database.db "INSERT INTO ip SELECT * FROM results.ip;"
    sqlite3 database.db "INSERT INTO cookie SELECT * FROM results.cookie;"

    # Drop the tables out of the database
    sqlite3 database.db "DROP TABLE results.CNAMEpackets;"
    sqlite3 database.db "DROP TABLE results.ip;"
    sqlite3 database.db "DROP TABLE results.cookie;"

done
