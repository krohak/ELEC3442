import RPi.GPIO as GPIO
import time

right_button  = 15

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(right_button, GPIO.IN, GPIO.PUD_UP)


def my_callback(channel):
    print('This is a edge event callback function!')
    print('Edge detected on channel %s'%channel)
    print('This is run in a different thread to your main program')



GPIO.add_event_detect(right_button, GPIO.RISING ,callback=my_callback, bouncetime=700)


#while True:
time.sleep(5)

if GPIO.event_detected(right_button):
    print('Button pressed')


GPIO.cleanup()


