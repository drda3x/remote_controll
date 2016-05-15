#!/usr/bin/python
# -*- coding:utf-8 -*-

# import socket
import subprocess
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):

	def do_GET(self):
		subprocess.call(['xdotool', 'key', 'space'])
		self.send_response(200)


def start():

	# server = socket.socket()
	# server.bind(('192.168.0.111', 9090))
	# server.listen(1)
	# connection, address = server.accept()

	# while True:
	# 	data = connection.recv(1024)
	# 	if data:
	# 		print data

	# connection.close()

	print 'Remote controll lanched\nhost: 192.168.0.111\nport: 9090'

	server_params = ('192.168.0.111', 9090)
	httpd = HTTPServer(server_params, Handler)

	while True:
		httpd.handle_request()

if __name__ == '__main__':
	start()
