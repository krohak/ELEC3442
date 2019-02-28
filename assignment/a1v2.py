import RPi.GPIO as GPIO
import time

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

def setVector(l1,l2,l3):
	GPIO.output(led1, l1)
	GPIO.output(led2, l2)
	GPIO.output(led3, l3)


def patternA():
	setVector(1,0,0)
	time.sleep(1)
	setVector(0,1,0)
	time.sleep(1)
	setVector(0,0,1)
	time.sleep(1)
	setVector(0,0,0)


def patternB():
	setVector(1,1,0)
	time.sleep(1)
	setVector(0,1,1)
	time.sleep(1)
	setVector(1,0,1)
	time.sleep(1)
	setVector(0,0,0)


def patternC():
	setVector(1,1,1)
	time.sleep(1)
	setVector(0,0,0)
	time.sleep(1)

patternArr = {0:patternA, 1:patternB, 2:patternC}

def changePattern(pattern, bool):
	return (pattern+1)%3 if bool else (pattern-1)%3

def playPattern(pattern):
	print("Pattern", pattern)
	patternArr[pattern]()


# def my_callback(channel):
#     print('This is a edge event callback function!')
#     print('Edge detected on channel %s'%channel)
#     print('This is run in a different thread to your main program')


GPIO.add_event_detect(left_button, GPIO.RISING, bouncetime=700)
GPIO.add_event_detect(right_button, GPIO.RISING, bouncetime=700)

Exit = False
pattern = 0

while not Exit:

	if GPIO.event_detected(left_button) and GPIO.event_detected(right_button):
		print("Both Button Pressed")
		playPattern(2)
		Exit = True
	
	elif GPIO.event_detected(left_button):
		pattern = changePattern(pattern, False)
		playPattern(pattern)

	elif GPIO.event_detected(right_button):
		pattern = changePattern(pattern, True)
		playPattern(pattern)

	else:
		playPattern(pattern)

GPIO.cleanup()

