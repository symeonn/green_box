import RPi.GPIO as GPIO
import time

RELAY_GPIO_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_GPIO_PIN, GPIO.OUT)  # GPIO Assign mode
time.sleep(1)

fan_state = not GPIO.input(RELAY_GPIO_PIN)  # negation because of inverted connection to relays

print(fan_state)

if fan_state:
    print("start fan")
else:
    print("stop fan")
