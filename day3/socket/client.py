from socket import *
import sys


HOST = 'localhost'
PORT = 2000
Addr = (HOST, PORT)


clientSocket = socket(AF_INET, SOCK_STREAM)


try:
	clientSocket.connect(Addr)
except Exception as err:
	print ("Can not Connect to (%s:%s)" % Addr)
	sys.exit()

print("Success connect to (%s:%s)" % Addr)

def prompt():
	sys.stdout.write("Me>> ")
	sys.stdout.flush()

while True:
	try:

		message = sys.stdin.readline()
		clientSocket.send(message)
		prompt()
		print("%s"%clientSocket.recv(1024))

	
	except KeyboardInterrupt:
		clientSocket.close()
		sys.exit()

