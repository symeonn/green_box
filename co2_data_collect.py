import fnmatch
import numpy
import seeed_sgp30
from grove.i2c import Bus
import time
import os


def get_i2c_port_number():
    search_path = '/dev/'

    for file in os.listdir(search_path):
        if fnmatch.fnmatch(file, 'i2c*'):
            # print(file)
            # print(file[-1])
            return int(file[-1])

    return ''


def get_data():
    i2c_port_number = get_i2c_port_number()
    sgp30 = seeed_sgp30.grove_sgp30(Bus(i2c_port_number))

    co2_eq_ppm = 400
    tvoc_ppb = 0

    sample_number = 0
    sample_array = numpy.zeros((10, 2))

    for lp in range(40):
        data = sgp30.read_measurements()
        co2_eq_ppm, tvoc_ppb = data.data
        # print("\r {}: tVOC = {} ppb CO2eq = {}  ".format(lp, tvoc_ppb, co2_eq_ppm))

        if co2_eq_ppm > 400 or tvoc_ppb > 0:
            sample_array[sample_number] = (tvoc_ppb, co2_eq_ppm)
            sample_number += 1
            # print(sample_array)

        if sample_number == 10:
            # print(sample_array)
            result = numpy.mean(sample_array, axis=0)
            # print(result)
            return result[0], result[1]  # VOC, CO2
            # break

        time.sleep(1)

    return get_data()
