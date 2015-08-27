from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost',2000))
serverSocket.listen(1)

conn, addr = serverSocket.accept()

recvBuf = conn.recv(1024)
print(len(recvBuf))
print(recvBuf)