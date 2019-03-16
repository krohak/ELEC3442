import pygame
from pygame.locals import *
from sense_hat import SenseHat

pygame.init()
pygame.display.set_mode((640, 480))
sense = SenseHat()
sense.clear()

x = 3
y = 3
sense.set_pixel(x, y, 255, 255, 255)

running = True
while running:
	for event in pygame.event.get():
		#print(event)
		if event.type == KEYDOWN:
			if event.key == K_DOWN and y < 7:
				sense.set_pixel(x, y, 0, 0, 0)
				y = y + 1
				sense.set_pixel(x, y, 255, 255, 255)
			elif event.key == K_RIGHT and x < 7:
				sense.set_pixel(x, y, 0, 0, 0)
				x = x + 1
				sense.set_pixel(x, y, 255, 255, 255)
			elif event.key == K_UP and y > 0:
				sense.set_pixel(x, y, 0, 0, 0)
				y = y - 1
				sense.set_pixel(x, y, 255, 255, 255)
			elif event.key == K_LEFT and x > 0:
				sense.set_pixel(x, y, 0, 0, 0)
				x = x - 1
				sense.set_pixel(x, y, 255, 255, 255)
			elif event.key == K_RETURN:
				sense.set_pixel(x, y, 0, 0, 0)
				x = 3
				y = 3
				sense.set_pixel(x, y, 255, 255, 255)
		if event.type == QUIT:
			running = False
			print("GOODBYE")
