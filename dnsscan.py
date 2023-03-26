import scapy.all as scapy
import selenium

listCNAMES = []

# TO DO: 
# - Need to save all first domain names in Domain settings
# - Save IP address of domain AND IP address of original URL
# - Get list of Domains from Domain attribute of cookies

class CNAME_packet():
    def __init__(self, packet, A):
        self.packet = packet
        self.has_A = A
        self.domain = packet.rrname
        self.cname = packet.rdata
        

# Function to be run everytime sniffer encounters a DNS packet
def parseDNS(packet):
    # Check if packet contains Transport layer UDP and Application layer DNS
    if (packet and packet.haslayer('DNS') and packet.haslayer('UDP')):
        udp = packet['UDP']
        dns = packet['DNS']

        has_CNAME = False
        has_Atype = False
        CNAME_index = 0

        # Check if packet is DNS response (source binded to DNS port)
        if (int(udp.sport) == 53):
            # Iterate through all DNS resource records
            for i in range(dns.ancount):
                dnsrr = dns.an[i]
                type_field = dnsrr.get_field('type')

                # If DNS entry is of type CNAME, store it in listCNAMES
                if (type_field.i2repr(dnsrr, dnsrr.type) == 'CNAME'):
                    CNAME_index = i
                    has_CNAME = True
                
                if (type_field.i2repr(dnsrr, dnsrr.type) == 'A'):
                    has_Atype = True
        
        if (has_CNAME):
            print("here")
            listCNAMES.append(CNAME_packet(dns.an[CNAME_index], has_Atype))
                    


def parseHTTP(packet):
    print(packet)


# Listens to traffic for DNS traffic (udp port 53) for 5 seconds then prints summary
# OR listens to HTTP traffic (port 80 / 443) to search for HTTP packets with cookies
scapy.sniff(filter="udp port 53", timeout=5, prn=parseDNS)
# scapy.sniff(filter="port 80 or port 443", timeout=5, prn=parseHTTP)

# Iterate through all CNAME packets and list their name, alias pair
for i, packet in enumerate(listCNAMES):
    print("CNAME Packet", i, ": ", packet.domain, packet.cname, packet.has_A)
