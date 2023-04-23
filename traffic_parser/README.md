# Traffic Parser
This portion of the code is designed to parse through networking traffic, grab the information wanted for Cookietective, then store those values into the database.db SQLite3 database. For the purposes of this project, the traffic being parsed is only DNS and HTTP/HTTPS packets to grab CNAME aliasing information and Set-Cookie header information found while web crawling. The specific reasons for using the information we gather is specified in the main README documentation.

## dnsscan.py
Python script to be run in the background that parses through networking traffic for 15 seconds to search for DNS packets. If any DNS response packets are found with a CNAME-type resource record, it will store the following information into the SQLite3 database (per CNAME packet):

- domainName (Original domain that has a CNAME alias)
- sourceAddress (IP Address that the packet came from)
- CNAMEAlias (Domain name that the original domain is aliased as)
- hasAType (Boolean for if this packet contains any A-type resource records)

## mitmproxy_script.py
Python script to be run with mitmproxy. As the Man in the Middle proxy runs, it will use this script for whenever it intercepts any HTTP/HTTPS response packets. The request function specifies how we want the proxy to modify / parse through incoming HTTP/HTTPS packets. In this case, we're using it to see if the packet contains Set-Cookie headers (cookie settings) that we store into SQLite using this information gathered:

- domainName (Domain name of packet sender)
- sourceAddress (IP address that sent the packet)
- domain_setting (What are the domain settings specified if any)
- httponly (Does cookie settings contain HttpOnly attribute)
- secure (Does cookie settings contain Secure attribute)

## test.sh
Bash script that sets up network settings (for Mac / Linux) and certificates necessary to run mitmproxy. 