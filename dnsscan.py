import scapy.all as scapy


def parseDNS(capture):

    # Check if any DNS packets were scanned in capture
    if (len(capture) < 1):
        print("No DNS requests found")
        return []
    
    for packet in capture:
        print(i[scapy.DNS.an[0]].show())
        
# Listens to traffic for DNS traffic (udp port 53) for 5 seconds then prints summary
capture = scapy.sniff(filter="udp port 53", timeout=5)
parseDNS(capture)