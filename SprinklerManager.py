import pymysql
import thread
import time
from DataManager import DataManager
from Sprinkler import Sprinkler

class SprinklerManager:

	threads = 0
	
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
		
	@staticmethod
	def setup():
		Sprinkler.setup([19,13,6,21])
		
	@staticmethod
	def waterSector(sector, minutes):
		SprinklerManager.threads += 1
		Sprinkler.sprinklers[sector].changeState(True)
		print("Turning on sprinkler " + str(sector) + " for " + str(minutes) + " minutes.")
		time.sleep(minutes * 60)
		print("Turning off sprinkler " + str(sector))
		SprinklerManager.threads -= 1
