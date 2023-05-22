#!/usr/bin/python3

# the core mod for all of the 3rd party networked servers is the socket module

import socket 

target_host = "127.0.0.1"
target_port = 80

# create a socket object 
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# connect the client
client.connect((target_host, target_port))

# send some data
client.sendto("AAABBBCCC".encode("utf-8"), (target_host, target_port))

# receive some data
data, addr = client.recvfrom(4096)

print(response)