#!/bin/bash

# Helper script to turn off proxy settings
networksetup -setwebproxystate "Wi-Fi" off
networksetup -setsecurewebproxystate "Wi-Fi" off