import socket

PORT = 12345
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', PORT))

print('Server created.')

server.listen(1)
con, addr = server.accept()
\
print('Connected to %s:%s.' % (addr[0], addr[1]))
