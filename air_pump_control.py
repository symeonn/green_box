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


def run_night_hours():
    print("air pump ON (night hours)")
    GPIO.output(RELAY_GPIO_PIN, GPIO.LOW)  # on
    time.sleep(3600)  # 1h

    print("air pump OFF (night hours)")
    GPIO.output(RELAY_GPIO_PIN, GPIO.HIGH)  # off
    time.sleep(900)  # 15m


def run_day_hours():
    print("air pump ON (day hours)")
    GPIO.output(RELAY_GPIO_PIN, GPIO.LOW)  # on
    time.sleep(1800)  # 30m

    print("air pump OFF (day hours)")
    GPIO.output(RELAY_GPIO_PIN, GPIO.HIGH)  # off
    time.sleep(900)  # 15m


while True:
    now = datetime.now()

    if settings.night_hour_begin <= now.hour or now.hour <= settings.night_hour_end:
        run_night_hours()
    else:
        run_day_hours()
