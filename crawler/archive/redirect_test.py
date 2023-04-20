import socket

ip_address = socket.getaddrinfo('google.com')
print(ip_address)