import scapy.all as scapy

listCNAMES = []

# Function to be run everytime sniffer encounters a DNS packet
def parseDNS(packet):

    # Check if packet contains Transport layer UDP and Application layer DNS
    if (packet and packet.haslayer('DNS') and packet.haslayer('UDP')):
        udp = packet['UDP']
        dns = packet['DNS']

        # Check if packet is DNS response (source binded to DNS port)
        if (int(udp.sport) == 53):
            # Iterate through all DNS resource records
            for i in range(dns.ancount):
                dnsrr = dns.an[i]
                type_field = dnsrr.get_field('type')

                # If DNS entry is of type CNAME, store it in listCNAMES
                if (type_field.i2repr(dnsrr, dnsrr.type) == 'CNAME'):
                    listCNAMES.append(dnsrr)
        
# Listens to traffic for DNS traffic (udp port 53) for 5 seconds then prints summary
scapy.sniff(filter="udp port 53", timeout=5, prn=parseDNS)

# Iterate through all CNAME packets and list their name, alias pair
for i, packet in enumerate(listCNAMES):
    type_field = packet.get_field('type')
    print("CNAME Packet", i, ":", packet.rrname, "->", packet.rdata)
