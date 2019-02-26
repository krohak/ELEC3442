import RPi.GPIO as GPIO
import time
import random

led1 = 2
led2 = 3
led3 = 4
left_button = 14
right_button = 15


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)

GPIO.output(led1, 0)
GPIO.output(led2, 0)
GPIO.output(led3, 0)

GPIO.setup(left_button, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(right_button, GPIO.IN, GPIO.PUD_UP)



def patternA():
	GPIO.output(led1, 1)
	GPIO.output(led2, 0)
	GPIO.output(led3, 0)

	time.sleep(1)

	GPIO.output(led1, 0)
	GPIO.output(led2, 1)
	GPIO.output(led3, 0)

	time.sleep(1)

	GPIO.output(led1, 0)
	GPIO.output(led2, 0)
	GPIO.output(led3, 1)

	time.sleep(1)

	GPIO.output(led1, 0)
	GPIO.output(led2, 0)
	GPIO.output(led3, 0)


def patternB():
	GPIO.output(led1, 1)
	GPIO.output(led2, 1)
	GPIO.output(led3, 0)

	time.sleep(1)

	GPIO.output(led1, 0)
	GPIO.output(led2, 1)
	GPIO.output(led3, 1)

	time.sleep(1)

	GPIO.output(led1, 1)
	GPIO.output(led2, 0)
	GPIO.output(led3, 1)

	time.sleep(1)

	GPIO.output(led1, 0)
	GPIO.output(led2, 0)
	GPIO.output(led3, 0)


def patternC():
	GPIO.output(led1, 1)
	GPIO.output(led2, 1)
	GPIO.output(led3, 1)

	time.sleep(1)

	GPIO.output(led1, 0)
	GPIO.output(led2, 0)
	GPIO.output(led3, 0)

	time.sleep(1)



patternA()
patternB()
patternC()

if GPIO.input(left_button) == False:
	print("Left Button Pressed")

if GPIO.input(right_button) == False:
	print("Right Button Pressed")


GPIO.cleanup()
