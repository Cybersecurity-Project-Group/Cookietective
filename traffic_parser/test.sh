#!/bin/bash

sudo tcpdump -XX -A -G 10 -W 1 -w test.pcap &
python3 dnsscan.py test.pcap
# python3 test_mitmproxy.py test.pcap

networksetup -setwebproxy "Wi-Fi" localhost 8080
networksetup -setsecurewebproxy "Wi-Fi" localhost 8080

networksetup -setwebproxystate "Wi-Fi" off
networksetup -setsecurewebproxystate "Wi-Fi" off