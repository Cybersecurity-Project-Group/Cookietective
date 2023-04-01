#!/bin/bash

sudo tcpdump -XX -A -G 5 -W 1 -w test.txt && tcpdump -r test.txt > pack.txt
python3 test_mitmproxy.py
