#!/bin/bash

ids=$(docker ps -f "status=exited" -q)

for id in $ids; do
    echo $id
    docker cp $id:/home/CoolestProject/database.db $id.db
    sqlite3 $id.db "SELECT * FROM cookie;"
done
