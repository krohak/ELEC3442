from sense_hat import SenseHat
import pygame
from pygame.locals import *
import socket

sense = SenseHat()
sense.clear()

pygame.init()
pygame.display.set_mode((640, 480))

SERVER = '172.16.0.206'
PORT = 12346

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((SERVER, PORT))

print('Server connected.')
server.send('Hello Server!'.encode())

reply = server.recv(1024)
print(reply.decode())

x, y = 3, 3

while True:
	for event in pygame.event.get():
		if event.type == KEYDOWN and event.key == K_DOWN:
			server.send('MOVE {0} {1} 0 0 0 '.format(x,y).encode())
			sense.set_pixel(x, y, 0, 0, 0)
			y = (y + 1) % 8
			server.send('MOVE {0} {1} 255 255 255 '.format(x,y).encode())
			sense.set_pixel(x, y, 255, 255, 255)
		elif event.type == KEYDOWN and event.key == K_UP:
			# Add some lines here
			server.send('MOVE {0} {1} 0 0 0 '.format(x,y).encode())
			sense.set_pixel(x, y, 0, 0, 0)
			y = (y - 1) % 8
			server.send('MOVE {0} {1} 255 255 255 '.format(x,y).encode())
			sense.set_pixel(x, y, 255, 255, 255)
		elif event.type == KEYDOWN and event.key == K_LEFT:
			# Add some lines here
			server.send('MOVE {0} {1} 0 0 0 '.format(x,y).encode())
			sense.set_pixel(x, y, 0, 0, 0)
			x = (x - 1) % 8
			server.send('MOVE {0} {1} 255 255 255 '.format(x,y).encode())
			sense.set_pixel(x, y, 255, 255, 255)
		elif event.type == KEYDOWN and event.key == K_RIGHT:
			# Add some lines here
			server.send('MOVE {0} {1} 0 0 0 '.format(x,y).encode())
			sense.set_pixel(x, y, 0, 0, 0)
			x = (x + 1) % 8
			server.send('MOVE {0} {1} 255 255 255 '.format(x,y).encode())
			sense.set_pixel(x, y, 255, 255, 255)

server.close()
