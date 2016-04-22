
class WateringCalculator:
	
	@staticmethod
	def calculateNeededGallons():
		
		result = []
		
		recentWateringGallons = DataManager.getPreviousWateringAmounts()
		sectorTargets = DataManager.getTargetCapacity()
		previousRain = DataManager.getLatestRain()
		currentMoistures = DataManager.getLatestMoisture()
		
		for x in range(0, 4):
			if currentMoistures[x] > sectorTargets[x]:
				result.insert(x, 0)
			elif (previousRain * 560) + recentWateringGallons[x + 1] > 280:
				result.insert(x, 0)
			else:
				result.insert(x, 1)
		
		return result