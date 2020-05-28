import RPi.GPIO as GPIO
import time
from datetime import datetime
import settings

print("init air pump control")

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

# relay IN2, GPIO 27 for air pump
RELAY_GPIO_PIN = 27

GPIO.setup(RELAY_GPIO_PIN, GPIO.OUT)  # GPIO Assign mode
time.sleep(1)


def runNightHours():
    print("air pump ON")
    GPIO.output(RELAY_GPIO_PIN, GPIO.LOW)  # on
    time.sleep(3600)  # 1h

    print("air pump OFF")
    GPIO.output(RELAY_GPIO_PIN, GPIO.HIGH)  # off
    time.sleep(900)  # 15m


def runDayHours():
    print("air pump ON")
    GPIO.output(RELAY_GPIO_PIN, GPIO.LOW)  # on
    time.sleep(1800)  # 30m

    print("air pump OFF")
    GPIO.output(RELAY_GPIO_PIN, GPIO.HIGH)  # off
    time.sleep(900)  # 15m


while True:
    now = datetime.now()

    if settings.nightHourBegin <= now.hour or now.hour <= settings.nightHourEnd:
        print("night hours")
        runNightHours()
    else:
        print("day hours")
        runDayHours()
