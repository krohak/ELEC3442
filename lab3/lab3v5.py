from sense_hat import SenseHat
sense = SenseHat()
sense.clear()

r = g = b = 0

while True:
	temp = sense.get_temperature()
	print(temp)

	if temp < 15:
		r = g = 0
		b = 255
	elif temp < 20:
		r = b = 0
		g = 255
	elif temp < 30:
		b = g = 0
		r = 255
	elif temp < 40:
		b = r = 255
		g = 255


	for x in range(0, 8):
		for y in range(0, 8):
			sense.set_pixel(x, y, r, g, b)
