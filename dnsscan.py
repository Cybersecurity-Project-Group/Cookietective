import scapy.all as scapy


# Listens to traffic for DNS traffic (udp port 53) for 5 seconds then prints summary
capture = scapy.sniff(filter="udp port 53", timeout=5)
capture.summary()
