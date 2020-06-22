import csv
from datetime import datetime
import os
import co2_data_collect
import dht_data_collect
import water_data_collect
import time
import settings

# import pandas as pd
# import plotly.express as px

print("init data save")

file_folder = '/home/pi/gb_CSV/'
csv_file_name = 'grow_data.csv'
html_file_name = 'grow_data_plot.html'

csv_file_full_path = file_folder + csv_file_name
html_file_full_path = file_folder + html_file_name


def get_sensors_data():
    voc, co2 = co2_data_collect.get_data()
    print("VOC: {} :: CO2: {} ".format(voc, co2))

    humidity, temperature = dht_data_collect.get_read_data(3)
    print("Humidity: {} :: Temperature: {} ".format(humidity, temperature))

    water_temperature = water_data_collect.get_water_temperature_data()
    print("Water temperature: {} ".format(water_temperature))

    return voc, co2, humidity, temperature, water_temperature


def write_data(readings):  # voc, co2, humidity, temperature, waterTemperature

    print("Writing data to CSV...")

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


while True:

    now = datetime.now()

    if settings.data_save_night_hour_end <= now.hour <= settings.data_save_night_hour_begin:
        print("Getting sensors readings...")

        voc, co2, humidity, temperature, water_temperature = get_sensors_data()
        write_data([voc, co2, humidity, temperature, water_temperature])
        # write_html_file()

        print("Data saving done.")

    time.sleep(settings.data_save_delay_seconds)
