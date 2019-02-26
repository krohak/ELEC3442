import RPi.GPIO as GPIO
import time
import random

wait = random.uniform(2,5)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led =4
left_button = 14
right_button = 15

GPIO.setup(led, GPIO.OUT)
GPIO.setup(left_button, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(right_button, GPIO.IN, GPIO.PUD_UP)


left_name = raw_input('Left player name is ')
right_name = raw_input('Right player name is ')


GPIO.output(led, 1)
time.sleep(wait)
GPIO.output(led, 0)


while True:
	if GPIO.input(left_button) == False:
		'''print("Left Button Pressed")'''
		print(left_name+" won")
		break
	if GPIO.input(right_button) == False:
		'''print("Right Button Pressed")'''
		print(right_name+" won")
		break
	


GPIO.cleanup()
