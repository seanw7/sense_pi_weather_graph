from sense_hat import *
from time import sleep

sense = SenseHat()

while True:
    sleep(5)
    myfile = open('weather.txt', 'a')
    myfile.write(f"{sense.temp}")
    print(f"{sense.temp}")
    myfile.write('\n')
    myfile.close()