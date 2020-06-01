import csv
from datetime import datetime
import time
import water_data_collect

print("init meters data save")

fileName = 'grow_data.csv'
fileFolder = '/home/pi/gb_CSV/'


def get_meters_data():
    print("Waiting for meters readings...")
    water_temperature, ph, ec = water_data_collect.getMetersData()
    return water_temperature, ph, ec


def write_data(ph, ec):  # voc, co2, humidity, temperature, waterTemperature

    # print("Writing data...")

    file_full_path = fileFolder + fileName

    with open(file_full_path) as file:

        lines = file.read().splitlines()

        if lines:
            last_line = lines[-1]

            cells = last_line.split(',')

            if float(cells[6]) < 0 <= float(ph):
                print("Writing pH value: {}".format(float(ph)))
                cells[6] = float(ph)

            if float(cells[7]) < 0 <= float(ec):
                print("Writing EC value: {}".format(float(ec)))
                cells[7] = float(ec)

    with open(file_full_path, "w") as file:
        writer = csv.writer(file, delimiter=',')
        # print lines
        for line in lines[:-1]:
            writer.writerow(line.split(','))
        writer.writerow(cells)


while True:
    water_temperature, ph, ec = get_meters_data()

    write_data(ph, ec)

    time.sleep(30)  # 30s
