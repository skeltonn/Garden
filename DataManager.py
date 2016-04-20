import pymysql

class DataManager:

	connection = null
	
	@staticmethod
	def getLatestMoisture():
		
		connection = pymysql.connect(host='localhost',
                             user='pi',
                             password='GardenPi',
                             db='Garden',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
                             
		try:
    		with connection.cursor() as cursor:
        		# Read a single record
        		sql = "SELECT zone1, zone2, zone3, zone4 FROM observed where record BETWEEN (NOW() - INTERVAL 1 DAY) AND NOW() order by record desc limit 1"
        		cursor.execute(sql)
        		result = cursor.fetchone()
        		print(result)
        		
		finally:
    		connection.close()