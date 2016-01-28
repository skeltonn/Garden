import time
from MoistureSensor import MoistureSensor

myrange = [0]

MoistureSensor.setup([5])
Sprinkler.setup([21])

while true:

        for x in myrange:

                if MoistureSensor.sensors[x].getMoisture() > 200:

                        Sprinkler.sprinklers[x].changeState(false)

                else:
                        Sprinkler.sprinklers[x].changeState(true)

        time.sleep(5)
