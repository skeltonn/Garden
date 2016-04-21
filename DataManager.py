import pymysql

class DataManager:

	connection = pymysql.connect(host='localhost',
    	user='root',
    	password='',
        db='Garden',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
                             
   	result = ""
	
	@staticmethod
	def getLatestMoisture():
	
		try:
		    	with connection.cursor() as cursor:
	    			global result
    				sql = "SELECT zone1, zone2, zone3, zone4 FROM observed where record BETWEEN (NOW() - INTERVAL 1 DAY) AND NOW() order by record desc limit 1"
    				cursor.execute(sql)
       				result = cursor.fetchone()
        			
		finally:
			global result
    			connection.close()
    			return [result["zone1"], result["zone2"], result["zone3"], result["zone4"]]

	@staticmethod
	def getLatestRainfall():
	
		try:
		    	with connection.cursor() as cursor:
		    		global result
    				sql = "SELECT rain FROM observed where record BETWEEN (NOW() - INTERVAL 1 DAY) AND NOW() order by record desc limit 1"
    				cursor.execute(sql)
    				result = cursor.fetchone()
        			
		finally:
			global result
    			connection.close()
    			return result["rain"]
    			
	@staticmethod
	def getPredictedRainfall():
	
		try:
		    	with connection.cursor() as cursor:
		    		global result
        			sql = "SELECT pchance, prain FROM observed where record BETWEEN (NOW() - INTERVAL 1 DAY) AND NOW() order by record desc limit 1"
        			cursor.execute(sql)
        			result = cursor.fetchone()
        		
		finally:
			global result
    			connection.close()
    			return [result["pchance"], result["prain"]]
    			
	@staticmethod
	def getPreviousWateringTimes():
	
		try:
		    	with connection.cursor() as cursor:
		    		global result
        			sql = "SELECT record, water1, water2, water3, water4 FROM observed where record BETWEEN (NOW() - INTERVAL 2 DAY) AND NOW() order by record desc"
        			cursor.execute(sql)
        			result = cursor.fetchall()
        		
		finally:
			global result
    			connection.close()
    			for row in result:
        			if row[1] > 0 or row[2] > 0 or row[3] > 0 or row[4] > 0:
        				return row
        		return ["2000-01-01 01:00:00", 0, 0, 0, 0]
    			
	@staticmethod
	def getSprinklerWaterRate():
	
		try:
		    	with connection.cursor() as cursor:
	    			global result
        			sql = "SELECT gpm FROM calibration"
        			cursor.execute(sql)
        			result = cursor.fetchall()
        		
		finally:
			global result
    			connection.close()
    			return [result[0], result[1], result[2], result[3]]
    			
	@staticmethod
	def getTargetCapacity():
	
		try:
	   	 	with connection.cursor() as cursor:
	    			global result
        			sql = "SELECT capcity FROM calibration"
        			cursor.execute(sql)
        			result = cursor.fetchall()
        	
		finally:
			global result
    			connection.close()
    			return result
