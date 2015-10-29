#!/usr/bin/python
# Test program

import PinController
import os
import time
import RPi.GPIO as GPIO

pinController = PinController.PinController()

pinController.controlPin(20, True)

time.sleep(10000)

pinController.controlPin(27, False)

GPIO.cleanup()
GPIO.setwarnings(False)
