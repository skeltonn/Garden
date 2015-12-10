#!/usr/bin/python
# Test program
import sys
import PinController
import os
import time
import RPi.GPIO as GPIO
pinController = PinController.PinController()
pinController.controlPin(pinController.relays[int(sys.argv[1])], False)
time.sleep(int(sys.argv[2]))
pinController.controlPin(pinController.relays[int(sys.argv[1])], True)

GPIO.cleanup()
GPIO.setwarnings(False)
