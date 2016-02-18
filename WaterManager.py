import time
from MoistureSensor import MoistureSensor
from Sprinkler import Sprinkler

myrange = [0,1,2,3,4,5,6]

MoistureSensor.setup([5])
Sprinkler.setup([18,23,24,25,16,21,20])

while True:

        for x in myrange:

                

                if MoistureSensor.sensors[0].getMoisture() > 40:
                        Sprinkler.sprinklers[x].changeState(False)

                else:
                        Sprinkler.sprinklers[x].changeState(True)

        print(MoistureSensor.sensors[0].getMoisture())
        time.sleep(2)
