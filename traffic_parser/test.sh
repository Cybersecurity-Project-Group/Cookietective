#!/bin/bash

sudo tcpdump -XX -A -G 10 -W 1 -w test.pcap
# python3 test_mitmproxy.py test.pcap
