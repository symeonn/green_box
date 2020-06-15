import serial
import time
import fnmatch
import os


def get_data():
    temperature = get_water_temperature_data()
    print("T: {} ".format(temperature))

    temperature, ph, ec = get_meters_data()
    print("T: {} :: pH: {} :: EC: {} ".format(temperature, ph, ec))


def get_water_temperature_data():
    return get_water_data(False)


def get_usb_port_path():
    search_path = '/dev/'

    for file in os.listdir(search_path):
        if fnmatch.fnmatch(file, 'ttyUSB*'):
            # print(file)
            return search_path + file

    return ''


def get_water_data(all_sensors):
    usb_port_path = get_usb_port_path()
    ser = serial.Serial(usb_port_path, 9600)

    while True:
        if ser.in_waiting > 0:
            raw_serial = ser.readline()
            row_serial = raw_serial.decode('utf-8').strip('\r\n')
            # print(rowSerial)
            data_split = row_serial.split(',')
            temperature = data_split[0]
            if not all_sensors:
                ser.close()
                return temperature

            ph = data_split[1]
            ec = data_split[2]

            # print(ph)
            # print(ec)

            if float(ph) >= 0 or float(ec) >= 0:
                print("T: {} :: pH: {} :: EC: {} ".format(temperature, ph, ec))
                ser.close()
                return temperature, ph, ec

        time.sleep(5)


def get_meters_data():
    return get_water_data(True)

# getData()
# getMetersData()
# getWaterTemperatureData()
