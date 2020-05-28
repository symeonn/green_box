import csv
from datetime import datetime
import time
import water_data_collect

print("init meters data save")

fileName = 'grow_data.csv'
fileFolder = '/home/pi/gb_CSV/'

def proceed():
	print "Waiting for meters readings..."
	waterTemperature, ph, ec = water_data_collect.getMetersData()
#	print("Water temperature: {} :: pH: {} :: EC: {} ".format(waterTemperature, ph, ec))


	writeData(waterTemperature, ph, ec)
#	writeData(0,10.6,5)

def writeData(waterTemperature, ph, ec): #voc, co2, humidity, temperature, waterTemperature

	print("Writing data...")
        #now = datetime.now() # current date and time
        #print(now)
        #fileTimestamp = now.strftime("%Y-%m-%d")
	#print(fileTimestamp)
	#print(fileTimestamp + fileNamePostfix)

	#timestamp = (now - datetime(1970, 1, 1)).total_seconds()

#	print(readings)
#	readings.insert(0, timestamp)
#	print(readings)

#	for i in readings :
#    		print(i)
	#readings = readings.insert(0, now)

        fileFullPath = fileFolder+fileName



	with open(fileFullPath) as file:
	    #writer = csv.writer(file)
	    #writer.writerow(readings)
#		csv.reader
#		file.read()

		lines = file.read().splitlines()

#		print lines

		if lines:
			first_line = lines[:1]
			last_line = lines[-1]
#			print first_line
#			print last_line
			cells = last_line.split(',')
#			print(cells)
#			print(cells[6])
			if float(cells[6]) < 0 and float(ph) >= 0:
				print("Writing pH value: {}".format(float(ph)))
				cells[6] = float(ph)
#				print(cells)

                        if float(cells[7]) < 0 and float(ec) >= 0:
                                print("Writing EC value: {}".format(float(ec)))
                                cells[7] = float(ec)
#                                print(cells)
#			print lines
#			lines[-1] = cells
#			print lines


	with open(fileFullPath, "w") as file:
		writer = csv.writer(file, delimiter=',')
#		print lines
		for line in lines[:-1]:
			writer.writerow(line.split(','))
	       	writer.writerow(cells)

while True:
	proceed()
	time.sleep(30) #30s
