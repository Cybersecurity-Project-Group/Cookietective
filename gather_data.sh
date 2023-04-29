#!/bin/bash

ids=$(sudo docker container ls -q)

for id in $ids; do
    echo $id
done