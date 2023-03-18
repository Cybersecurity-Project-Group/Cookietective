import scapy.all as scapy

# Function to be run everytime sniffer encounters a DNS packet
def parseDNS(packet):

    # Check if packet contains Transport layer UDP and Application layer DNS
    if (packet and packet.haslayer('DNS') and packet.haslayer('UDP')):
        ip = packet['IP']
        udp = packet['UDP']
        dns = packet['DNS']

        # Check if packet is DNS request (destination binded to DNS port)
        if int(udp.dport) == 53:
            qtype_field = dns.qd.get_field('qtype')
            print("\n### DNS Request ###\n")
            print("Qname:", dns.qd.qname)
            print("Qtype:", qtype_field.i2repr(dns.qd, dns.qd.qtype))


        # Check if packet is DNS response (source binded to DNS port)
        elif int(udp.sport) == 53:
            # Iterate through all DNS resource records
            for i in range(dns.ancount):
                dnsrr = dns.an[i]
                type_field = dnsrr.get_field('type')
                print("\n### DNS Response ###\n")
                print("Name:", dnsrr.rrname)
                print("Type:", type_field.i2repr(dnsrr, dnsrr.type))
                print("Data:", dnsrr.rdata)
        
# Listens to traffic for DNS traffic (udp port 53) for 5 seconds then prints summary
scapy.sniff(filter="udp port 53", timeout=5, prn=parseDNS)
