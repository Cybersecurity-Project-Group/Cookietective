#!/bin/bash

NUM_CONTAINERS=2
NUM_URLS=10
URLS_PER_CONTAINER=$(( $NUM_URLS/$NUM_CONTAINERS ))

# echo $URLS_PER_CONTAINER
# for (( i=0 ; i < $NUM_CONTAINERS ; i++ )); 
#     do echo $i
# done


docker run -p 9000:53/udp snickerdoodle 0 4
docker run -p 9001:53/udp snickerdoodle 5 8