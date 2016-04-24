import pymysql
import datetime

class DataManager:

	@staticmethod
	def getLatestMoisture(connection):
	
		try:
    			sql = "SELECT zone1, zone2, zone3, zone4 FROM observed where record BETWEEN (NOW() - INTERVAL 1 DAY) AND NOW() order by record desc limit 1"
    			cursor = connection.cursor()
    			cursor.execute(sql)
       			result = cursor.fetchone()
        			
		finally:
    			connection.close()
    			return [result["zone1"], result["zone2"], result["zone3"], result["zone4"]]

	@staticmethod
	def getLatestRainfall(connection):
	
		try:
    			sql = "SELECT rain FROM observed where record BETWEEN (NOW() - INTERVAL 1 DAY) AND NOW() order by record desc limit 1"
    			cursor = connection.cursor()
    			cursor.execute(sql)
    			result = cursor.fetchone()
        			
		finally:
    			connection.close()
    			return result["rain"]
    			
	@staticmethod
	def getPredictedRainfall(connection):
	
		try:
        		sql = "SELECT pchance, prain FROM observed where record BETWEEN (NOW() - INTERVAL 1 DAY) AND NOW() order by record desc limit 1"
        		cursor = connection.cursor()
        		cursor.execute(sql)
        		result = cursor.fetchone()
        		
		finally:
    			connection.close()
    			return [result["pchance"], result["prain"]]
    			
	@staticmethod
	def getPreviousWateringAmounts(connection):
	
		try:
        		sql = "SELECT record, water1, water2, water3, water4 FROM observed where record BETWEEN (NOW() - INTERVAL 2 DAY) AND NOW() order by record desc"
        		cursor = connection.cursor()
        		cursor.execute(sql)
        		result = cursor.fetchall()
        		
		finally:
    			connection.close()
    			for row in result:
        			if row["water1"] > 0 or row["water2"] > 0 or row["water3"] > 0 or row["water4"] > 0:
        				return [row["record"], row["water1"], row["water2"], row["water3"], row["water4"]]
        		return [datetime.datetime.min, 0, 0, 0, 0]
    			
	@staticmethod
	def getSprinklerWaterRates(connection):
	
		try:
        		sql = "SELECT gpm FROM calibration"
        		cursor = connection.cursor()
        		cursor.execute(sql)
    			result = cursor.fetchall()
        		
		finally:
    			connection.close()
    			return [result[0]["gpm"], result[1]["gpm"], result[2]["gpm"], result[3]["gpm"]]
    			
	@staticmethod
	def getTargetCapacity(connection):
	
		try:
        		sql = "SELECT capacity FROM calibration"
        		cursor = connection.cursor()
        		cursor.execute(sql)
        		result = cursor.fetchall()
        	
		finally:
    			connection.close()
    			return [result[0]["capacity"], result[1]["capacity"], result[2]["capacity"], result[3]["capacity"]]
