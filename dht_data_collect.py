import Adafruit_DHT
import time

def getData():
        sensor = 11
        pin = 17

        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        #print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
        return humidity, temperature



#getData()
