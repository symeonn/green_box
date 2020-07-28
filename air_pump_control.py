import RPi.GPIO as GPIO
import time
from datetime import datetime
import settings
import file_logger
import os

# relay IN2, GPIO 27 for air pump
RELAY_GPIO_PIN = 27
logs_name = 'air_pump_control.log'
file_logger.init(logs_name)


def init():
    file_logger.info("Init air pump control")

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RELAY_GPIO_PIN, GPIO.OUT)  # GPIO Assign mode
    time.sleep(1)


def run_night_hours():
    file_logger.info("air pump ON (for {} minutes)".format(settings.air_pump_on_interval_night_seconds / 60))
    GPIO.output(RELAY_GPIO_PIN, GPIO.LOW)  # on
    time.sleep(settings.air_pump_on_interval_night_seconds)

    file_logger.info("air pump OFF (for {} minutes)".format(settings.air_pump_off_interval_night_seconds / 60))
    GPIO.output(RELAY_GPIO_PIN, GPIO.HIGH)  # off
    time.sleep(settings.air_pump_off_interval_night_seconds)


def run_day_hours():
    file_logger.info("air pump ON (for {} minutes)".format(settings.air_pump_on_interval_day_seconds / 60))
    GPIO.output(RELAY_GPIO_PIN, GPIO.LOW)  # on
    time.sleep(settings.air_pump_on_interval_day_seconds)

    file_logger.info("air pump OFF (for {} minutes)".format(settings.air_pump_off_interval_day_seconds / 60))
    GPIO.output(RELAY_GPIO_PIN, GPIO.HIGH)  # off
    time.sleep(settings.air_pump_off_interval_day_seconds)


def start():
    while True:
        try:
            now = datetime.now()

            if settings.air_pump_night_hour_begin <= now.hour or now.hour <= settings.air_pump_night_hour_end:
                run_night_hours()
            else:
                run_day_hours()
        except Exception as e:
            file_logger.error('Error in: ' + os.path.basename(__file__))
            file_logger.error(e)


init()
start()
