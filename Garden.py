#!/usr/bin/python
# Test program
import PinController

pinController = PinController()

pinController.controlPin(21, True)

GPIO.cleanup()
GPIO.setwarnings(False)
