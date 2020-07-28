import csv
from datetime import datetime
import os
import co2_data_collect
import dht_data_collect
import water_data_collect
import time
import settings
import file_logger

# import pandas as pd
# import plotly.express as px


logs_name = 'data_save.log'
file_logger.init(logs_name)

file_folder = '/home/pi/gb_data/gb_csv/'
csv_file_name = 'grow_data.csv'
csv_file_full_path = file_folder + csv_file_name


def init():
    file_logger.info('Init data save')


def get_sensors_data():
    voc, co2 = co2_data_collect.get_data()
    file_logger.info("VOC: {} :: CO2: {} ".format(voc, co2))

    humidity, temperature = dht_data_collect.get_read_data(3)
    file_logger.info("Humidity: {} :: Temperature: {} ".format(humidity, temperature))

    water_temperature = water_data_collect.get_water_temperature_data()
    file_logger.info("Water temperature: {} ".format(water_temperature))

    return voc, co2, humidity, temperature, water_temperature


def write_data(readings):  # voc, co2, humidity, temperature, waterTemperature

    file_logger.info("Writing data to CSV...")

    current_datetime = datetime.now()

    readings.insert(0, current_datetime.strftime("%Y-%m-%d %H:%M:%S"))
    readings.insert(6, -1.0)
    readings.insert(7, -1.0)

    with open(csv_file_full_path, 'a') as file:
        writer = csv.writer(file)

        if os.stat(csv_file_full_path).st_size == 0:
            writer.writerow(["datetime", "VOC", "CO2", "humidity", "temperature", "water_temperature", "pH", "EC"])

        writer.writerow(readings)


# def write_html_file():
#     df = pd.read_csv(csv_file_full_path)
#     fig = px.line(df, x='datetime', y=['CO2', 'VOC', 'humidity', 'temperature', 'water_temperature', 'pH', 'EC'],
#                   title='Apple Share Prices over time (2014)')
#     with open(html_file_full_path, 'w') as file:
#         html = fig.to_html()
#         file.write(html)

def start():
    while True:
        try:
            now = datetime.now()

            if settings.data_save_night_hour_end <= now.hour <= settings.data_save_night_hour_begin:
                file_logger.info("Getting sensors readings...")

                voc, co2, humidity, temperature, water_temperature = get_sensors_data()
                write_data([voc, co2, humidity, temperature, water_temperature])
                # write_html_file()

                file_logger.info("Data saving done.")

            time.sleep(settings.data_save_delay_seconds)

        except Exception as e:
            file_logger.error('Error in: ' + os.path.basename(__file__))
            file_logger.error(e)


init()
start()
