from socketserver import ThreadingTCPServer, StreamRequestHandler

PORT = 2000
BUFSIZE=1024

class MyRequestHandler(StreamRequestHandler):
	def handle(self):
		conn = self.request
		print("connection from", self.client_address)
		buf = conn.recv(BUFSIZE)
		if not buf:
			print("nothing")
		else:
			print(buf)

server = ThreadingTCPServer(('localhost',PORT), MyRequestHandler)
print("listening on port :", PORT)
server.serve_forever()