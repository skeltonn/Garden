import time
import pymysql
from MoistureSensor import MoistureSensor
from Sprinkler import Sprinkler
from DataManager import DataManager

myrange = [0,1,2,3,4,5,6]

MoistureSensor.setup([5])
Sprinkler.setup([18,23,24,25,16,21,20])


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
connection = pymysql.connect(host='localhost',
    	user='root',
    	password='',
        db='Garden',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
        
for x in range(0, 5):
	
	if x == 0:
		print(DataManager.getLatestMoisture(a = connection))
	elif x == 1:
		print(DataManager.getLatestRainfall(a = connection))
	elif x == 2:
		print(DataManager.getPredictedRainfall(a = connection))
	elif x == 3:
		print(DataManager.getPreviousWateringTimes(a = connection))
	elif x == 4:
		print(DataManager.getSprinklerWaterRate(a = connection))
	else:
		print(DataManager.getTargetCapacity(a = connection))
