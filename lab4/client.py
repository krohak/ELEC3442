import socket
SERVER = '<Server IP>'
PORT = 12345
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((SERVER, PORT))
print('Server connected.')
server.close()
