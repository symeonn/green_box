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
    print("air pump ON (for {} minutes)".format(settings.air_pump_on_interval_night_seconds / 60))
    GPIO.output(RELAY_GPIO_PIN, GPIO.LOW)  # on
    time.sleep(settings.air_pump_on_interval_night_seconds)

    print("air pump OFF (for {} minutes)".format(settings.air_pump_off_interval_night_seconds / 60))
    GPIO.output(RELAY_GPIO_PIN, GPIO.HIGH)  # off
    time.sleep(settings.air_pump_off_interval_night_seconds)


def run_day_hours():
    print("air pump ON (for {} minutes)".format(settings.air_pump_on_interval_day_seconds / 60))
    GPIO.output(RELAY_GPIO_PIN, GPIO.LOW)  # on
    time.sleep(settings.air_pump_on_interval_day_seconds)

    print("air pump OFF (for {} minutes)".format(settings.air_pump_off_interval_day_seconds / 60))
    GPIO.output(RELAY_GPIO_PIN, GPIO.HIGH)  # off
    time.sleep(settings.air_pump_off_interval_day_seconds)


while True:
    now = datetime.now()

    if settings.air_pump_night_hour_begin <= now.hour or now.hour <= settings.air_pump_night_hour_end:
        run_night_hours()
    else:
        run_day_hours()
