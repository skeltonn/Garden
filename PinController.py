#!/usr/bin/python

import RPi.GPIO as GPIO
import os

from array import array

class PinController:

	relays = [21,20,22,27,17,18,24,23]

	def __init__(self):
		
		GPIO.setmode(GPIO.BCM)

		for x in self.relays:
			GPIO.setup(x, GPIO.OUT)
			
	def controlPin(self, pin, setting):
		
		print str(pin) + " set to " + str(setting);
		GPIO.output(pin, setting);
