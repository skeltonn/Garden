import pymysql

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
	def getPreviousWateringTimes(connection):
	
		try:
        		sql = "SELECT record, water1, water2, water3, water4 FROM observed where record BETWEEN (NOW() - INTERVAL 2 DAY) AND NOW() order by record desc"
        		cursor = connection.cursor()
        		cursor.execute(sql)
        		result = cursor.fetchall()
        		
		finally:
    			connection.close()
    			for row in result:
        			if row["water1"] > 0 or row["water2"] > 0 or row["water3"] > 0 or row["water4"] > 0:
        				return row
        		return ["2000-01-01 01:00:00", 0, 0, 0, 0]
    			
	@staticmethod
	def getSprinklerWaterRate(connection):
	
		try:
        		sql = "SELECT gpm FROM calibration"
        		cursor = connection.cursor()
        		cursor.execute(sql)
    			result = cursor.fetchall()
        		
		finally:
    			connection.close()
    			return [result[0], result[1], result[2], result[3]]
    			
	@staticmethod
	def getTargetCapacity(connection):
	
		try:
        		sql = "SELECT capcity FROM calibration"
        		cursor = connection.cursor()
        		cursor.execute(sql)
        		result = cursor.fetchall()
        	
		finally:
    			connection.close()
    			return result
