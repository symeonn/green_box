
import subprocess
from datetime import datetime
import RPi.GPIO as GPIO
import time

print("init image capture")
captureHour = 15

def captureImage():

	print("Capturing image...")
	now = datetime.now() # current date and time


#	print(now)
	fileName = now.strftime("%Y-%m-%d_%H%M") + ".jpg"
#	print(fileTimestamp)


	bashCommand = "fswebcam --no-banner -q -r 1600x1200 -p YUYV -S 1 --jpeg 95 /home/pi/gb_cam_images/{}".format(fileName)


#	ledWhiteOn()
	GPIO.setmode(GPIO.BCM)

        RELAY_GPIO_PIN = 8 # relay IN1, GPIO 8 for FAN

        GPIO.setup(RELAY_GPIO_PIN, GPIO.OUT) # GPIO Assign mode
        time.sleep(1)

        GPIO.output(RELAY_GPIO_PIN, GPIO.LOW) # on


	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()

	time.sleep(20)

        GPIO.output(RELAY_GPIO_PIN, GPIO.HIGH) # off

        time.sleep(5)

        GPIO.cleanup()

#	print(output)
#	print(error)
	print("Image captured: {}".format(fileName))


def ledWhiteOn():
	GPIO.setmode(GPIO.BCM)

	RELAY_GPIO_PIN = 8 # relay IN1, GPIO 8 for FAN

	GPIO.setup(RELAY_GPIO_PIN, GPIO.OUT) # GPIO Assign mode
	time.sleep(1)

	GPIO.output(RELAY_GPIO_PIN, GPIO.LOW) # on
	time.sleep(60)
	GPIO.output(RELAY_GPIO_PIN, GPIO.HIGH) # off


	time.sleep(5)

	GPIO.cleanup()


while True:
	now = datetime.now()

	if now.hour == captureHour:
		captureImage()

	time.sleep(55 * 60) #55m

#capture()
