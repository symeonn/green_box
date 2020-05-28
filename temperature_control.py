import RPi.GPIO as GPIO
import dht_data_collect
import time

highTemperatureLevel = 22
lowTemperatureLevel = 20


# relay IN1, GPIO 4 for FAN
RELAY_GPIO_PIN = 4


def init():
	GPIO.setwarnings(False)
	print("init temperature control")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(RELAY_GPIO_PIN, GPIO.OUT) # GPIO Assign mode
        time.sleep(1)


def startMonitoring():

	while True:

		humidity, temperature = dht_data_collect.getData()

		print("Temperature: {} *C".format(temperature))

		if temperature > highTemperatureLevel:
		        GPIO.output(RELAY_GPIO_PIN, GPIO.LOW) # on
			print("FAN on")
		else:
		        GPIO.output(RELAY_GPIO_PIN, GPIO.HIGH) # off
	                print("FAN off")

#		print("watinig...")
		time.sleep(120) #2m


init()

startMonitoring()
#fan_control.stopFan()
