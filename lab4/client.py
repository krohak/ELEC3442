import socket

SERVER = '172.16.0.206'
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((SERVER, PORT))

print('Server connected.')

server.close()
