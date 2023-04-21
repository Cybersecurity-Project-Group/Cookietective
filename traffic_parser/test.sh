#!/bin/bash

# Set up the network settings based on the operating system
if [[ "$OSTYPE" == "darwin"* ]]; then
    networksetup -setwebproxy "Wi-Fi" localhost 8080
    networksetup -setsecurewebproxy "Wi-Fi" localhost 8080
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    gsettings set org.gnome.system.proxy.http host 'my.proxy.com'
    gsettings set org.gnome.system.proxy.http port 8000

    gsettings set org.gnome.system.proxy.https host 'my.proxy.com'
    gsettings set org.gnome.system.proxy.https port 8000

    gsettings set org.gnome.system.proxy mode 'manual'

else
    echo "ERROR: Not a supported Operating System"
fi

# Code that runs the stuff
# sudo tcpdump -XX -A -G 10 -W 1 -w test.pcap &
# python3 dnsscan.py test.pcap
# python3 test_mitmproxy.py test.pcap

sleep 10


# End code cleanup: Remove the proxies
if [[ "$OSTYPE" == "darwin"* ]]; then
    networksetup -setwebproxystate "Wi-Fi" off
    networksetup -setsecurewebproxystate "Wi-Fi" off
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    gsettings set org.gnome.system.proxy mode 'none'
fi
