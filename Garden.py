#!/usr/bin/python
# Test program

import PinController
import os
import time
import RPi.GPIO as GPIO

pinController = PinController.PinController()

for x in pinController.relays:
	pinController.controlPin(x, False)
	time.sleep(1)
	pinController.controlPin(x, True)


GPIO.cleanup()
GPIO.setwarnings(False)
