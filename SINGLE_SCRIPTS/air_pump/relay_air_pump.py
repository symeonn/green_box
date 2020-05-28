import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# relay IN1, GPIO 4 for FAN

RELAY_GPIO_PIN = 27


GPIO.setup(RELAY_GPIO_PIN, GPIO.OUT) # GPIO Assign mode
time.sleep(1)

GPIO.output(RELAY_GPIO_PIN, GPIO.LOW) # out
time.sleep(30)
GPIO.output(RELAY_GPIO_PIN, GPIO.HIGH) # on

time.sleep(5)

GPIO.output(RELAY_GPIO_PIN, GPIO.LOW) # out
time.sleep(30)
GPIO.output(RELAY_GPIO_PIN, GPIO.HIGH) # on


time.sleep(5)

GPIO.cleanup()

