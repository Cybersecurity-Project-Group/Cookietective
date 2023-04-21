#!/bin/bash

# Set up the network settings based on the operating system
# Install the mitmproxy certificate
openssl x509 -in mitmproxy-ca-cert.pem -out mitmproxy-ca-cert.crt

# Install certificate and set up proxies for Mac
if [[ "$OSTYPE" == "darwin"* ]]; then
    # Add in the mitmproxy certificate
    sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain mitmproxy-ca-cert.crt
    
    networksetup -setwebproxy "Wi-Fi" localhost 8080
    networksetup -setsecurewebproxy "Wi-Fi" localhost 8080
# Install certificate and set up proxies for Linux
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    certutil -d sql:$HOME/.pki/nssdb -A -t "C,," -n "mitmproxy" -i mitmproxy-ca-cert.crt
    export http_proxy=localhost:8080
    export https_proxy=localhost:8080

else
    echo "ERROR: Not a supported Operating System"
fi

# Code that runs the stuff
# sudo tcpdump -XX -A -G 10 -W 1 -w test.pcap &
# python3 dnsscan.py test.pcap
# python3 test_mitmproxy.py test.pcap
mitmproxy
sleep 10


# End code cleanup: Remove the proxies
if [[ "$OSTYPE" == "darwin"* ]]; then
    networksetup -setwebproxystate "Wi-Fi" off
    networksetup -setsecurewebproxystate "Wi-Fi" off
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    unset http_proxy
    unset https_proxy
fi
