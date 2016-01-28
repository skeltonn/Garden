import RPi.GPIO as GPIO
from array import array

class Sprinkler:

    pins = []

    sprinklers = []

    @staticmethod
    def setup(pinNumbers):

        GPIO.setmode(GPIO.BCM)

        Sprinkler.pins = pinNumbers
			
        for x in range(0, len(pinNumbers)):

            sprinkler = Sprinkler(x)


    def __init__(self, number):

        self.pin = Sprinkler.pins[number]
        
        GPIO.setup(x, GPIO.OUT)
	GPIO.output(x, True)
	
        Sprinkler.sprinklers.append(self)
        

    def changeState(boolean):

        GPIO.output(self.pin, boolean)
        
