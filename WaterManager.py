import time
from MoistureSensor import MoistureSensor
from Sprinkler import Sprinkler
from DataManager import DataManager

myrange = [0,1,2,3,4,5,6]

MoistureSensor.setup([5])
Sprinkler.setup([18,23,24,25,16,21,20])


'''
while True:

        for x in myrange:

                

                if MoistureSensor.sensors[0].getMoisture() > 40:
                        Sprinkler.sprinklers[x].changeState(False)

                else:
                        Sprinkler.sprinklers[x].changeState(True)

        print(MoistureSensor.sensors[0].getMoisture())
        time.sleep(2)
'''

connection = pymysql.connect(host='localhost',
    	user='root',
    	password='',
        db='Garden',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)

DataManager.getLatestMoisture(connection)