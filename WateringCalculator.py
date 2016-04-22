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
		previousRain = DataManager.getLatestRain(pymysql.connect(host='localhost',
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
			if currentMoistures[x] > sectorTargets[x]:
				result.insert(x, 0)
			elif (previousRain * 560) + recentWateringGallons[x + 1] > 280:
				result.insert(x, 0)
			else:
				result.insert(x, 1)
			print(previousRain * 560) + recentWateringGallons[x + 1])
		
		return result
