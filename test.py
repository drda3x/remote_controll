#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import time

sock = socket.socket()
sock.connect(('192.168.0.111', 9090))

i = 0

while True:
	sock.send(str(i))
	i += 1
	time.sleep(2)


sock.close()

print data