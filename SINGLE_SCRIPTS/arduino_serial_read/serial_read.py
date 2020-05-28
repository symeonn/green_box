#rpi-arduino-dht11
#Raspberry Pi reads temperature and humidity sensor data from Arduino
import serial, string, time
#In this example /dev/ttyUSB0 is used
#This may change in your case to /dev/ttyUSB1, /dev/ttyUSB2, etc.
ser = serial.Serial('/dev/ttyUSB0', 9600)
#The following block of code works like this:
#If serial data is present, read the line, decode the UTF8 data,
#...remove the trailing end of line characters
#...split the data into temperature and humidity
#...remove the starting and ending pointers (< >)
#...print the output
while True:
        if ser.in_waiting > 0:
            rawserial = ser.readline()
            cookedserial = rawserial.decode('utf-8').strip('\r\n')
            #datasplit = cookedserial.split(',')
            #temperature = datasplit[0].strip('<')
            #humidity = datasplit[1].strip('>')
            #print(temperature)
            #print(humidity)
	    print(cookedserial)

