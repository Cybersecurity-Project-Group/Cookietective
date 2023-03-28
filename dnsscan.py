import scapy.all as scapy
from scapy.layers import http
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
        
        # Append DNSRR information to global list if has CNAME entry
        if (has_CNAME):
            listCNAMES.append(CNAME_packet(dns.an[CNAME_index], has_Atype))
            packet.show()
                    


def parseHTTP(packet):
    # Check if on TLS layer (since HTTP and HTTPS requests are only on TCP)
    if (packet.haslayer('TCP')):
        if (packet.haslayer(http.HTTPRequest) or packet.haslayer(http.HTTPResponse)):
            if (packet.haslayer(scapy.Raw)):
                keys = ["Domain", "Set-Cookie"]
                # if any(key in packet[scapy.Raw].load for key in keys):
                #     print(packet[scapy.Raw].load)
                if (packet.haslayer(http.HTTPRequest)):
                    print(packet[http.HTTPRequest].fields.get('Cookie'))
                else:
                    print(packet[http.HTTPResponse].fields.get('Cookie'))

    # if (packet.haslayer('TCP')):
    #     if(packet['TCP'].payload != scapy.packet.raw):
    #         print(packet.iteritems())

# def process_packets(packet):
#     print("here")
#     if packet.haslayer(http.HTTPRequest):
#         print("here")
#         url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
#         print('URL: ' + url.decode())
        
scapy.load_layer("http")
scapy.load_layer("tls")

# Listens to traffic for DNS traffic (udp port 53) for 5 seconds then prints summary
# OR listens to HTTP traffic (port 80 / 443) to search for HTTP packets with cookies
# scapy.sniff(filter="udp port 53", timeout=5, prn=parseDNS)
scapy.sniff(filter="port 80 or port 443", timeout=10, prn=parseHTTP)
# scapy.sniff(iface="WiFi 2", store=False, prn=process_packets)

# Iterate through all CNAME packets and list their name, alias pair
for i, packet in enumerate(listCNAMES):
    print("CNAME Packet", i, ": Domain:", packet.domain, "CNAME Alias:", packet.cname, "Has A-type", packet.has_A)
    
# Notes:
# CNAME packets (with no A-type packet) do NOT contain IP address
# Megele paper says that (name,value) = (name looked up, name it's seen as)
# 
# 
# 
