#!/bin/bash

# Set up the network settings based on the operating system
# Install the mitmproxy certificate
openssl x509 -in mitmproxy-ca-cert.pem -out mitmproxy-ca-cert.crt

# Install certificate and set up proxies for Mac
if [[ "$OSTYPE" == "darwin"* ]]; then
    # Add in the mitmproxy certificate
    sudo security add-trusted-cert -d -p ssl -p basic -k /Library/Keychains/System.keychain mitmproxy-ca-cert.pem
    
    networksetup -setwebproxy "Wi-Fi" localhost 8080
    networksetup -setsecurewebproxy "Wi-Fi" localhost 8080
# Install certificate and set up proxies for Linux
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Add in mitmproxy certificate for local user
    cp mitmproxy-ca-cert.pem ~/.local/share/ca-certificates/
    trust anchor --store mitmproxy-ca-cert.pem

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


# End code cleanup: Remove the proxies and certificates
if [[ "$OSTYPE" == "darwin"* ]]; then
    sudo security delete-certificate -c "mitmproxy" /Library/Keychains/System.keychain
    networksetup -setwebproxystate "Wi-Fi" off
    networksetup -setsecurewebproxystate "Wi-Fi" off
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    trust anchor --remove mitmproxy-ca-cert.pem
    unset http_proxy
    unset https_proxy
fi
