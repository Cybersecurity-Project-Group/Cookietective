#!/bin/bash

# Set up the network settings based on the operating system
# Install the mitmproxy certificate
openssl x509 -in ~/.mitmproxy/mitmproxy-ca-cert.pem -out mitmproxy-ca-cert.crt

# Install certificate and set up proxies for Mac
if [[ "$OSTYPE" == "darwin"* ]]; then
    # Add in the mitmproxy certificate
    sudo security add-trusted-cert -d -p ssl -p basic -k /Library/Keychains/System.keychain mitmproxy-ca-cert.crt
    
    networksetup -setwebproxy "Wi-Fi" localhost 8080
    networksetup -setsecurewebproxy "Wi-Fi" localhost 8080
# Install certificate and set up proxies for Linux
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Add in mitmproxy certificate for local user
    sudo cp mitmproxy-ca-cert.crt /usr/local/share/ca-certificates
    sudo update-ca-certificates

    export http_proxy=http://localhost:8080/
    export https_proxy=http://localhost:8080/

else
    echo "ERROR: Not a supported Operating System"
fi

# Code that runs the traffic scanners in the background
sudo python3 traffic_parser/dnsscan.py &
# sudo python3 httpsscan.py &
sudo mitmproxy -s traffic_parser/mitmproxy_script.py &
python3 crawler/crawler.py crawler/sample_urls.txt 
# python3 crawler

End code cleanup: Remove the proxies and certificates
if [[ "$OSTYPE" == "darwin"* ]]; then
    # sudo security delete-certificate -c "mitmproxy" /Library/Keychains/System.keychain
    networksetup -setwebproxystate "Wi-Fi" off
    networksetup -setsecurewebproxystate "Wi-Fi" off
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # trust anchor --remove mitmproxy-ca-cert.pem
    unset http_proxy
    unset https_proxy
fi
