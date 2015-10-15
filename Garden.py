#!/usr/bin/python
# Test program
import RPi.GPIO as GPIO
import time
import os
import random

from array import array
sleepTime = .1
GPIO.setmode(GPIO.BCM)

relays= [21,20,22,27,17,18,24,23]

for x in relays:
	GPIO.setup(x, GPIO.OUT)


def pinControl(sleepTime):
	for y in range(0,5):
		
		random.shuffle(relays)
		for x in relays:

			GPIO.output(x, False)
			time.sleep(sleepTime)
			print "Loop " + str(x)
			GPIO.output(x, True)
			time.sleep(sleepTime)


pinControl(sleepTime)

GPIO.cleanup()
GPIO.setwarnings(False)
