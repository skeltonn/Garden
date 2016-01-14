import mcp3008

class MoistureSensor():

    pins = []
    
    sensors = []

    @staticmethod
    def setup(pinNumbers):

        MoistureSensor.pins = pinNumbers
        for x in range(0, len(pinNumbers)):
	   
	   sensor = MoistureSensor(x)
	
        
    def __init__(self, number):

        self.pin = MoistureSensor.pins[number]
    	MoistureSensor.sensors.append(self)

	
    def getMoisture(self):
	
	return mcp3008.readadc(self.pin)
