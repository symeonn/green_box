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
    GPIO.setup(RELAY_GPIO_PIN, GPIO.OUT)  # GPIO Assign mode
    time.sleep(1)


def start_monitoring():
    while True:

        humidity, temperature = dht_data_collect.getData()

        if temperature > highTemperatureLevel:
            GPIO.output(RELAY_GPIO_PIN, GPIO.LOW)  # on
            print(f'Temperature: {temperature} *C - FAN on')
        else:
            GPIO.output(RELAY_GPIO_PIN, GPIO.HIGH)  # off
            print(f'Temperature: {temperature} *C - FAN off')

        # print("watinig...")
        time.sleep(120)  # 2m


init()

start_monitoring()
# fan_control.stopFan()
