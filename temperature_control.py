import RPi.GPIO as GPIO
import dht_data_collect
import time
import settings
import file_logger
import os

# relay IN1, GPIO 4 for FAN
RELAY_GPIO_PIN = 4
logs_name = 'temperature_control.log'
file_logger.init(logs_name)


def init():
    file_logger.info('Init temperature control')

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RELAY_GPIO_PIN, GPIO.OUT)  # GPIO Assign mode
    time.sleep(1)


def start_monitoring():
    while True:

        try:
            fan_running = not GPIO.input(RELAY_GPIO_PIN)  # negation because of inverted connection to relays
            humidity, temperature = dht_data_collect.get_read_data(3)

            if temperature > settings.fan_enable_temperature_limit_celsius and not fan_running:
                GPIO.output(RELAY_GPIO_PIN, GPIO.LOW)  # on
                file_logger.info('Temperature: {} *C - FAN on'.format(temperature))
            elif temperature <= settings.fan_enable_temperature_limit_celsius and fan_running:
                GPIO.output(RELAY_GPIO_PIN, GPIO.HIGH)  # off
                file_logger.info('Temperature: {} *C - FAN off'.format(temperature))

            time.sleep(settings.fan_monitoring_interval_seconds)
        except Exception as e:
            file_logger.error('Error in: ' + os.path.basename(__file__))
            file_logger.error(e)


init()

start_monitoring()
# fan_control.stopFan()
