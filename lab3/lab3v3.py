from sense_hat import SenseHat
sense = SenseHat()
sense.clear()
pressure = sense.get_pressure()
pressure = round(pressure, 1)
print(pressure)

humidity = sense.get_humidity()
humidity = round(humidity, 1)
print(humidity)


sense.clear()
on_pixel = [255, 0, 0]
off_pixel = [0, 0, 0]
while True:
	humidity = sense.get_humidity()
	humidity = round(humidity, 1)
	if humidity > 100:
		humidity = 100.0
	pixels = []
	on_count = int((64 / 100.0) * humidity)
	off_count = 64 - on_count
	pixels.extend([on_pixel] * on_count)
	pixels.extend([off_pixel] * off_count)
	sense.set_pixels(pixels)
