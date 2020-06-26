#!/usr/bin/env python3
#
import socket
hostname = ['']
for i in range(2, 254):
    hostname = ['']
    ipAddress = "192.168.2.{}".format(i)
    try:
        hostname = socket.gethostbyaddr(""+ipAddress)
        print ("{} {}".format(ipAddress, hostname[0]))
    except:
        pass
