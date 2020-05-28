import csv
from datetime import datetime
import os
import co2_data_collect
import dht_data_collect
import water_data_collect
import time

print("init data save")

syncHours = [10,22]

fileName = 'grow_data.csv'
fileFolder = '/home/pi/gb_CSV/'

def proceed():

	voc, co2 = co2_data_collect.getData()
	print("VOC: {} :: CO2: {} ".format(voc,co2))

	humidity, temperature = dht_data_collect.getData()
	print("Humidity: {} :: Temperature: {} ".format(humidity, temperature))

	waterTemperature = water_data_collect.getWaterTemperatureData()
	print("Water temperature: {} ".format(waterTemperature))

	writeData([voc, co2, humidity, temperature, waterTemperature])

def writeData(readings): #voc, co2, humidity, temperature, waterTemperature

	print("Writing data to CSV...")

        now = datetime.now() # current date and time
        #print(now)
        #fileTimestamp = now.strftime("%Y-%m-%d")
	#print(fileTimestamp)
	#print(fileTimestamp + fileNamePostfix)

#	timestamp = (now - datetime(1970, 1, 1)).total_seconds()

#	print(readings)
	readings.insert(0, now.strftime("%Y-%m-%d %H:%M:%S"))
	readings.insert(6, -1.0)
	readings.insert(7, -1.0)

#	print(readings)

#	for i in readings :
#    		print(i)
	#readings = readings.insert(0, now)

	fileFullPath = fileFolder+fileName


	with open(fileFullPath, 'a') as file:

		writer = csv.writer(file)

                if os.stat(fileFullPath).st_size == 0:
	                writer.writerow(["datetime","VOC","CO2","humidity","temperature","water_temperature", "pH", "EC"])

		writer.writerow(readings)



while True:

	now = datetime.now()

	if now.hour in syncHours:
		print("Getting sensors readings...")
		proceed()
		print("Data saving done.")

	time.sleep(55 * 60) #55m
