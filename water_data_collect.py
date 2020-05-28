import serial
import time

def getData():
	temperature = getWaterTemperatureData()
	print("T: {} ".format(temperature))

	temperature, ph, ec = getMetersData()
	print("T: {} :: pH: {} :: EC: {} ".format(temperature, ph, ec))

def getWaterTemperatureData():
	return getWaterData(False)


def getWaterData(all):

        #Raspberry Pi reads temperature and humidity sensor data from Arduino
#	with serial.Serial() as ser:
 #   		ser.baudrate = 9600
  #  		ser.port = '/dev/ttyUSB0'
#		ser.open()
    		#ser.write(b'hello')
	ser = serial.Serial('/dev/ttyUSB0', 9600)

	while True:
        	if ser.in_waiting > 0:
               		rawserial = ser.readline()
                	rowSerial = rawserial.decode('utf-8').strip('\r\n')
#		          	print(rowSerial)
	       	        datasplit = rowSerial.split(',')
                	temperature = datasplit[0]
			if not all :
				ser.close()
				return temperature

	               	ph = datasplit[1]
			ec = datasplit[2]

#	        	        print(ph)
#                		print(ec)

			if float(ph) >= 0 or float(ec) >= 0:
				print("T: {} :: pH: {} :: EC: {} ".format(temperature, ph, ec))
				ser.close()
			        return temperature, ph, ec

		time.sleep(5)

def getMetersData():

	return getWaterData(True)


#getData()
#getMetersData()
#getWaterTemperatureData()
