import pymysql
from DataManager import DataManager

class SprinklerManager:
	
	@staticmethod
	def determineMinutes(gallons):
		
		minutes = []
		
		sprinklerWaterRates = DataManager.getSprinklerWaterRates(pymysql.connect(host='localhost',
	    		user='root',
    			password='',
        		db='Garden',
       		 	charset='utf8mb4',
        		cursorclass=pymysql.cursors.DictCursor))
		
		for x in range(0, 4):
			print gallons[x]
			print sprinklerWaterRates[x]
			minutes.insert(x, int((gallons[x] / sprinklerWaterRates[x]) + 1))
			
		return minutes
		