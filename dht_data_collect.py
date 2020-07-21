import Adafruit_DHT
import numpy
import time


def get_single_read_data():
    sensor = 11
    pin = 17

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    # print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))

    try:
        float(humidity)
    except Exception as e:
        print("humidity Not a float")
        humidity = 0.0

    try:
        float(temperature)
    except Exception as e:
        print("temperature Not a float")
        temperature = 0.0

    return humidity, temperature


def get_read_data(read_count=3):
    sample_array = numpy.zeros((read_count, 2))

    for read_number in range(read_count):
        humidity, temperature = get_single_read_data()

        if humidity != 0.0 and temperature != 0.0:
            sample_array[read_number] = humidity, temperature
        # print('H={0:0.1f}*  T={1:0.1f}%'.format(sample_array[read_number][0], sample_array[read_number][1]))
        time.sleep(2)

    avg_result = numpy.mean(sample_array, axis=0)
    return avg_result[0], avg_result[1]
