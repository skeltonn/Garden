import time
from MoistureSensor import MoistureSensor

myrange = [0]

MoistureSensor.setup([5])

for x in range(0,100):

	print "Repetition " + str(x)
	
	for x in myrange:
	
		print "Sensor " + str(x) + ": " + str(MoistureSensor.sensors[x].getMoisture())
	
	time.sleep(2)
