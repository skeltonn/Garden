import sys
import time
import pymysql
import thread
from MoistureSensor import MoistureSensor
from Sprinkler import Sprinkler
from DataManager import DataManager
from WateringCalculator import WateringCalculator
from SprinklerManager import SprinklerManager

myrange = [0,1,2,3,4,5,6]

MoistureSensor.setup([5])

'''
while True:

        for x in myrange:

                

                if MoistureSensor.sensors[0].getMoisture() > 40:
                        Sprinkler.sprinklers[x].changeState(False)

                else:
                        Sprinkler.sprinklers[x].changeState(True)

        print(MoistureSensor.sensors[0].getMoisture())
        time.sleep(2)
'''

for x in range(0, 5):
	
	connection = pymysql.connect(host='localhost',
    	user='root',
    	password='',
        db='Garden',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
	
	if x == 0:
		print(DataManager.getLatestMoisture(connection))
	elif x == 1:
		print(DataManager.getLatestRainfall(connection))
	elif x == 2:
		print(DataManager.getPredictedRainfall(connection))
	elif x == 3:
		print(DataManager.getPreviousWateringAmounts(connection))
	elif x == 4:
		print(DataManager.getSprinklerWaterRates(connection))
	else:
		print(DataManager.getTargetCapacity(connection))
		
gallons = WateringCalculator.calculateNeededGallons()
minutes = SprinklerManager.determineMinutes(gallons)
print("Gallons: " + str(gallons))
print("Minutes: " + str(minutes))
SprinklerManager.setup()

for x in range(0, 4):
	
	if minutes[x] > 1:
		thread.start_new_thread(SprinklerManager.waterSector, (x, minutes[x]))
		time.sleep(1)

	while(SprinklerManager.active):
		time.sleep(2);

sys.exit()
