#!/bin/bash

# Helper bash script for testing that turns on proxy settings
# openssl x509 -in ~/.mitmproxy/mitmproxy-ca-cert.pem -out mitmproxy-ca-cert.crt
# sudo security add-trusted-cert -d -p ssl -p basic -k /Library/Keychains/System.keychain mitmproxy-ca-cert.crt
networksetup -setwebproxy "Wi-Fi" localhost 8080
networksetup -setsecurewebproxy "Wi-Fi" localhost 8080