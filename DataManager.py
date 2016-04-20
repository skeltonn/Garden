import pymysql

class DataManager:

	connection = pymysql.connect(host='localhost',
                             user='pi',
                             password='GardenPi',
                             db='Garden',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
	
	@staticmethod
	def getLatestMoisture():
	
		try:
	    		with connection.cursor() as cursor:
        			# Read a single record
        			sql = "SELECT zone1, zone2, zone3, zone4 FROM observed where record BETWEEN (NOW() - INTERVAL 1 DAY) AND NOW() order by record desc limit 1"
        			cursor.execute(sql)
        			result = cursor.fetchone()
        			return [result["zone1"], result["zone2"], result["zone3"], result["zone4"]]
        		
		finally:
    			connection.close()

	@staticmethod
	def getLatestRainfall():
	
		try:
	    		with connection.cursor() as cursor:
        			# Read a single record
        			sql = "SELECT rain FROM observed where record BETWEEN (NOW() - INTERVAL 1 DAY) AND NOW() order by record desc limit 1"
        			cursor.execute(sql)
        			result = cursor.fetchone()
        			return result["rain"]
        		
		finally:
    			connection.close()
    			
    @staticmethod
	def getPredictedRainfall():
	
		try:
	    		with connection.cursor() as cursor:
        			# Read a single record
        			sql = "SELECT pchance, prain FROM observed where record BETWEEN (NOW() - INTERVAL 1 DAY) AND NOW() order by record desc limit 1"
        			cursor.execute(sql)
        			result = cursor.fetchone()
        			return [result["pchance"], result["prain"]]
        		
		finally:
    			connection.close()
    			
    @staticmethod
	def getPreviousWateringTimes():
	
		try:
	    		with connection.cursor() as cursor:
        			# Read a single record
        			sql = "SELECT record, water1, water2, water3, water4 FROM observed where record BETWEEN (NOW() - INTERVAL 2 DAY) AND NOW() order by record desc"
        			cursor.execute(sql)
        			result = cursor.fetchall()
        			for row in result:
        				if row[1] > 0 or row[2] > 0 or row[3] > 0 or row[4] > 0 or row[5] > 0;
        					return row
        			return ["2000-01-01 01:00:00", 0, 0, 0, 0]
        		
		finally:
    			connection.close()
    			
    			
    			