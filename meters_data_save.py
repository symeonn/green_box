import csv
import time
import water_data_collect
import file_logger
import os

logs_name = 'meters_data_save.log'
file_logger.init(logs_name)

file_logger.info("Init meters data save")

fileName = 'grow_data.csv'
fileFolder = '/home/pi/gb_data/gb_csv/'

ph_cell_number = 6
ec_cell_number = 7


def get_meters_data():
    file_logger.info("Waiting for meters readings...")
    water_temperature, ph, ec = water_data_collect.get_all_meters_data()
    file_logger.info("T: {} :: pH: {} :: EC: {} ".format(water_temperature, ph, ec))
    return water_temperature, ph, ec


def write_data(ph, ec):  # voc, co2, humidity, temperature, waterTemperature

    file_full_path = fileFolder + fileName

    with open(file_full_path) as file:

        lines = file.read().splitlines()

        if lines:
            last_line = lines[-1]

            cells = last_line.split(',')

            if float(cells[ph_cell_number]) < 0 <= float(ph):
                file_logger.info("Writing pH value: {}".format(float(ph)))
                cells[ph_cell_number] = float(ph)

            if float(cells[ec_cell_number]) < 0 <= float(ec):
                file_logger.info("Writing EC value: {}".format(float(ec)))
                cells[ec_cell_number] = float(ec)

    with open(file_full_path, "w") as file:
        writer = csv.writer(file, delimiter=',')
        for line in lines[:-1]:
            writer.writerow(line.split(','))
        writer.writerow(cells)


def start():
    while True:
        try:

            water_temperature, ph, ec = get_meters_data()
            write_data(ph, ec)

            time.sleep(30)  # 30s
        except Exception as e:
            file_logger.error('Error in: ' + os.path.basename(__file__))
            file_logger.error(e)


start()
