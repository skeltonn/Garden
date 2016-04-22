import pymysql
from DataManager import DataManager

class WateringCalculator:
	
	@staticmethod
	def calculateNeededGallons():
		
		result = []
		
		recentWateringGallons = DataManager.getPreviousWateringAmounts(pymysql.connect(host='localhost',
	    		user='root',
    			password='',
        		db='Garden',
       		 	charset='utf8mb4',
        		cursorclass=pymysql.cursors.DictCursor))
		sectorTargets = DataManager.getTargetCapacity(pymysql.connect(host='localhost',
    			user='root',
    			password='',
        		db='Garden',
        		charset='utf8mb4',
        		cursorclass=pymysql.cursors.DictCursor))
		previousRain = DataManager.getLatestRainfall(pymysql.connect(host='localhost',
    			user='root',
    			password='',
        		db='Garden',
        		charset='utf8mb4',
    			cursorclass=pymysql.cursors.DictCursor))
    	predictedRain = DataManager.getPredictedRainfall(pymysql.connect(host='localhost',
    			user='root',
    			password='',
        		db='Garden',
        		charset='utf8mb4',
    	    	cursorclass=pymysql.cursors.DictCursor))
		currentMoistures = DataManager.getLatestMoisture(pymysql.connect(host='localhost',
    			user='root',
    			password='',
        		db='Garden',
        		charset='utf8mb4',
        		cursorclass=pymysql.cursors.DictCursor))
		
		for x in range(0, 4):
			
			currentGallons = (previousRain * 560) + recentWateringGallons[x + 1]
			
			if currentMoistures[x] > sectorTargets[x]:
				result.insert(x, 0)
			elif currentGallons > 280:
				result.insert(x, 0)
			else:
				if (predictedRain[1] * 560) * predictedRain[0] + currentGallons > 280:
					result.insert(x, 0)
				else:
					result.insert(x, 280 - ((predictedRain[1] * 560) * predictedRain[0] + currentGallons))
			
			print((predictedRain[1] * 560) * predictedRain[0] + currentGallons)
			
		return result
