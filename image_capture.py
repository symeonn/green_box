import subprocess
from datetime import datetime
import RPi.GPIO as GPIO
import time
import file_logger
import os
import settings

RELAY_GPIO_PIN = 8  # relay IN1, GPIO 8 for FAN

logs_name = 'image_capture.log'
file_logger.init(logs_name)

file_logger.info("Init image capture")


def captureImage(timestamp):
    file_logger.info("Capturing image...")

    file_name = timestamp.strftime("%Y-%m-%d_%H%M") + ".jpg"
    bash_command = "fswebcam --no-banner -q -r 1600x1200 -p YUYV -S 1 --jpeg 95 /home/pi/gb_data/gb_cam_images/{}" \
        .format(file_name)

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(RELAY_GPIO_PIN, GPIO.OUT)  # GPIO Assign mode
    time.sleep(1)
    GPIO.output(RELAY_GPIO_PIN, GPIO.LOW)  # on

    process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    time.sleep(20)

    GPIO.output(RELAY_GPIO_PIN, GPIO.HIGH)  # off

    time.sleep(5)

    GPIO.cleanup()

    file_logger.info("Image captured: {}".format(file_name))


while True:
    try:
        now = datetime.now()

        if now.hour == settings.image_capture_hour:
            captureImage(now)

        time.sleep(55 * 60)  # 55m
    except Exception as e:
        file_logger.error('Error in: ' + os.path.basename(__file__))
        file_logger.error(e)
