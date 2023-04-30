import sys
import socket
from datetime import datetime as dt
import time

# https://stackoverflow.com/questions/47964457/python-whois-library-return-nothing-for-active-domain-names

def get_whois_data(ip):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("whois.arin.net", 43))
    s.send(('n ' + ip + '\r\n').encode())

    response = b""

    # setting time limit in secondsmd
    startTime = time.mktime(dt.now().timetuple())
    timeLimit = 3
    while True:
        elapsedTime = time.mktime(dt.now().timetuple()) - startTime
        data = s.recv(4096)
        response += data
        if (not data) or (elapsedTime >= timeLimit):
            break
    s.close()

    return response.decode()

def findOrgName(whoisString):
    orgNameIndex = whoisString.find("OrgName")
    orgNameEnd = whoisString.find("OrgId")
    orgName = whoisString[orgNameIndex+16:orgNameEnd-1]
    return orgName

def main():
    domain1 = "play.google.com"
    domain1ip = socket.gethostbyname(domain1);
    url1Dump = get_whois_data(domain1ip)
    url1name = findOrgName(url1Dump)

    domain2 = "youtube.com"
    domain2ip = socket.gethostbyname(domain2);
    url2Dump = get_whois_data(domain2ip)
    url2name = findOrgName(url2Dump)

    print(url1name)
    print(url2name)

main()