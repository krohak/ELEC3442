import socket
PORT = 12345
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', PORT))
print('Server created.')
server.listen(1)
con, addr = server.accept()
print('Connected to %s:%s.' % (addr[0], addr[1]))

data = con.recv(1024)
print(data.decode())
con.send('Greetings from the server.'.encode())


while True:
	msg = con.recv(1024).decode().split(' ')
	if msg[0] == 'KILL':
		print('Shut down server.')
		con.close()
		server.close()
		break
	elif msg[0] == 'SHOW':
		print(' '.join(msg[1:]))
	else:
		print('Message: %s' % msg)
