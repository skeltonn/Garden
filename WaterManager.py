import time

range = Range(0,4)

for x in range:

	print "Repetition " + x
	sensor = MoistureSensor(x)

for x in Range(0,100):

	print "Repetition " + x
	
	for x in range:
	
		print "Sensor " + x ": " + MoistureSensor.sensors[x].getMoisture()
	
	time.wait(1000)
	