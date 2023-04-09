import scapy.all as scapy

listCNAMES = []

# TO DO: 
# - 

class CNAME_packet():
    def __init__(self, packet, A, ip):
    def __init__(self, packet, A, ip):
        self.packet = packet
        self.has_A = A
        self.domain = packet.rrname
        self.cname = packet.rdata
        if len(ip) < 1:
            self.ip = None
        else:
            self.ip = ip
        self.ip = ip
        

# Function to be run everytime sniffer encounters a DNS packet
def parseDNS(packet):
    # Check if packet contains Transport layer UDP and Application layer DNS
    if (packet and packet.haslayer('DNS') and packet.haslayer('UDP')):
        udp = packet['UDP']
        dns = packet['DNS']

        has_CNAME = False
        has_Atype = False
        CNAME_index = 0
        ip = []

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
                    ip.append(dnsrr.rdata)
        
        # Append DNSRR information to global list if has CNAME entry
        if (has_CNAME):
            listCNAMES.append(CNAME_packet(dns.an[CNAME_index], has_Atype, ip))
            
# Main function that executes the DNSscanner
def main():
    scapy.load_layer("http")
    scapy.load_layer("tls")
            listCNAMES.append(CNAME_packet(dns.an[CNAME_index], has_Atype, ip))
            # print(ip)
                    


def parseHTTP(packet):
    # Check if on TLS layer (since HTTP and HTTPS requests are only on TCP)
    if (packet.haslayer('TCP')):
        if (packet.haslayer(http.HTTPRequest) or packet.haslayer(http.HTTPResponse) or packet.haslayer('SSL_TLS')):
            # if (packet.haslayer(scapy.Raw)):
            #     keys = ["Domain", "Set-Cookie"]
                # if any(key in packet[scapy.Raw].load for key in keys):
                #     print(packet[scapy.Raw].load)
            if (packet.haslayer(http.HTTPRequest)):
                print(packet[http.HTTPRequest].fields.get('Cookie'))
            else:
                print(packet[http.HTTPResponse].fields.get('Cookie'))
            print(packet.show())
    # if (packet.haslayer('TCP')):
    #     if(packet['TCP'].payload != scapy.packet.raw):
    #         print(packet.iteritems())
        
scapy.load_layer("http")
scapy.load_layer("tls")

    # Listens to traffic for DNS traffic (udp port 53) for 15 seconds then prints summary
    scapy.sniff(filter="udp port 53", timeout=15, prn=parseDNS)

    # for packet in scapy.PcapReader('test.pcap'):
    #     parseDNS(packet)

    # # Iterate through all CNAME packets and list their name, alias pair
    # for i, packet in enumerate(listCNAMES):
    #     print("CNAME Packet", i, ": Domain:", packet.domain, "CNAME Alias:", packet.cname, "Has A-type", packet.has_A)
