#!/usr/bin/env python
#
# Copyright (c) 2017, ARNERI, arneri@ukr.net All rights reserved
#
# A 'server' part of HTTP-JSON task
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#        * Redistributions of source code must retain the above copyright
#          notice, this list of conditions and the following disclaimer.
#        * Redistributions in binary form must reproduce the above copyright
#          notice, this list of conditions and the following disclaimer in the
#          documentation and/or other materials provided with the distribution.
#        * Neither the name of The Linux Foundation nor
#          the names of its contributors may be used to endorse or promote
#          products derived from this software without specific prior written
#          permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NON-INFRINGEMENT ARE DISCLAIMED.    IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#


# Import base classes
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


# Redefine class' methods for own purposes
class S(BaseHTTPRequestHandler):

	# Process 'C-L' part
	def _set_headers(self):

		# Report success on procesisng a request
		self.send_response(200)

		# Send header
		self.send_header('Content-type', 'text/html')

		# Finalize
		self.end_headers()

	# Process 'GET' request
	def do_GET(self):

		# Prepare heading of a responce
		self._set_headers()

		# Forge data (relevant under current task) and send back
		self.wfile.write("<html><body><h1>.</h1></body></html>")

	# Process 'HEAD' request
	def do_HEAD(self):

		# Prepare heading of a responce
		self._set_headers()
        

	# Process 'POST' request
	def do_POST(self):

		# Compute data size
		content_length = int(self.headers['Content-Length'])

		# Obtain data into buffer 
		post_data = self.rfile.read(content_length) 

		# Display aforementioned buffer locally
		print post_data

		# Prepare heading of a responce
		self._set_headers()


# Program launcher        
def run(server_class=HTTPServer, handler_class=S, port=80):

	# Construct server with default address and port ID received through command line
	server_address = ('', port)

	# Instantiate HTTP server
	httpd = server_class(server_address, handler_class)

	# Verbose current state of a program 
	print 'Starting HTTP server with POST/GET/HEAD methods redefined on port', port

	# Launch the server
	httpd.serve_forever()


# Define a namespace (for the case if somebody will try to import this script as a module from outter script)
if __name__ == "__main__":

	# Variadic parameter set processing module
	from sys import argv

	# Parameter set is correct? 
	if len(argv) == 2:

		# Take a command line parameter as HTTP server port ID and go ahead ...
		run(port=int(argv[1]))
	else:
		# Go ahead anyway ...
		run()

# End of a script
