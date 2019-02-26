import RPi.GPIO as GPIO
import time

left_button = 14
right_button = 15

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(left_button, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(right_button, GPIO.IN, GPIO.PUD_UP)


while True:
	if GPIO.input(left_button) == False:
		t1 = time.time()
		while (time.time() - t1 < 7):
			pass

		print("Left Button Pressed")
		break


	if GPIO.input(right_button) == False:
		print("Right Button Pressed")
		break

GPIO.cleanup()

