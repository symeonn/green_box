import RPi.GPIO as GPIO
import dht_data_collect
import time
import settings

# relay IN1, GPIO 4 for FAN
RELAY_GPIO_PIN = 4


def init():
    GPIO.setwarnings(False)
    print("init temperature control")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RELAY_GPIO_PIN, GPIO.OUT)  # GPIO Assign mode
    time.sleep(1)


def start_monitoring():
    while True:

        fan_running = not GPIO.input(RELAY_GPIO_PIN)  # negation because of inverted connection to relays
        humidity, temperature = dht_data_collect.get_read_data(3)

        if temperature > settings.fan_enable_temperature_limit_celsius and not fan_running:
            GPIO.output(RELAY_GPIO_PIN, GPIO.LOW)  # on
            print('Temperature: {} *C - FAN on'.format(temperature))
        elif temperature <= settings.fan_enable_temperature_limit_celsius and fan_running:
            GPIO.output(RELAY_GPIO_PIN, GPIO.HIGH)  # off
            print('Temperature: {} *C - FAN off'.format(temperature))

        time.sleep(settings.fan_monitoring_interval_seconds)


init()

start_monitoring()
# fan_control.stopFan()
