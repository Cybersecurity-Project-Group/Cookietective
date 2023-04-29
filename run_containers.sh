#!/bin/bash

NUM_CONTAINERS=10
NUM_URLS=3300
INDEX_OFFSET=0
URLS_PER_CONTAINER=$(( $NUM_URLS/$NUM_CONTAINERS ))

docker build -t snickerdoodle .

for (( i=0 ; i < $NUM_CONTAINERS ; i++ )); do
    UDP_PORT=$(( $i + 9000 ))
    HTTPS_PORT=$(( $i + 9500))

    start=$(( $INDEX_OFFSET + $URLS_PER_CONTAINER*$i ))
    end=$(( $INDEX_OFFSET + $URLS_PER_CONTAINER*($i+1)))
        
    docker run -dp $UDP_PORT:53/udp -dp $HTTPS_PORT:8080 snickerdoodle $start $end

done


# docker run -p 9000:53/udp 9500:8080 snickerdoodle 0 4
# docker run -p 9001:53/udp 9501:8080 snickerdoodle 5 8
