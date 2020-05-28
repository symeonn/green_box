import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


GPIO.setup(4, GPIO.OUT) # GPIO Assign mode
time.sleep(1)
GPIO.output(4, GPIO.LOW) # out
time.sleep(1)
GPIO.output(4, GPIO.HIGH) # on


GPIO.setup(27, GPIO.OUT) # GPIO Assign mode
time.sleep(1)
GPIO.output(27, GPIO.LOW) # out
time.sleep(1)
GPIO.output(27, GPIO.HIGH) # on


GPIO.setup(18, GPIO.OUT) # GPIO Assign mode
time.sleep(1)
GPIO.output(18, GPIO.LOW) # out
time.sleep(1)
GPIO.output(18, GPIO.HIGH) # on

GPIO.setup(23, GPIO.OUT) # GPIO Assign mode
time.sleep(1)
GPIO.output(23, GPIO.LOW) # out
time.sleep(1)
GPIO.output(23, GPIO.HIGH) # on

GPIO.setup(24, GPIO.OUT) # GPIO Assign mode
time.sleep(1)
GPIO.output(24, GPIO.LOW) # out
time.sleep(1)
GPIO.output(24, GPIO.HIGH) # on

GPIO.setup(25, GPIO.OUT) # GPIO Assign mode
time.sleep(1)
GPIO.output(25, GPIO.LOW) # out
time.sleep(1)
GPIO.output(25, GPIO.HIGH) # on

GPIO.setup(8, GPIO.OUT) # GPIO Assign mode
time.sleep(1)
GPIO.output(8, GPIO.LOW) # out
time.sleep(1)
GPIO.output(8, GPIO.HIGH) # on

GPIO.setup(7, GPIO.OUT) # GPIO Assign mode
time.sleep(1)
GPIO.output(7, GPIO.LOW) # out
time.sleep(1)
GPIO.output(7, GPIO.HIGH) # on









time.sleep(5)

GPIO.cleanup()
