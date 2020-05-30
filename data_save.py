import csv
from datetime import datetime
import os
import co2_data_collect
import dht_data_collect
import water_data_collect
import time
import pandas as pd
import plotly.express as px

print("init data save")

syncHours = [10, 22]

fileFolder = '/home/pi/gb_CSV/'
csv_file_name = 'grow_data.csv'
html_file_name = 'grow_data_plot.html'


def proceed():
    voc, co2 = co2_data_collect.getData()
    print("VOC: {} :: CO2: {} ".format(voc, co2))

    humidity, temperature = dht_data_collect.getData()
    print("Humidity: {} :: Temperature: {} ".format(humidity, temperature))

    water_temperature = water_data_collect.getWaterTemperatureData()
    print("Water temperature: {} ".format(water_temperature))

    write_data([voc, co2, humidity, temperature, water_temperature])


def write_data(readings):  # voc, co2, humidity, temperature, waterTemperature

    print("Writing data to CSV...")

    current_datetime = datetime.now()

    readings.insert(0, current_datetime.strftime("%Y-%m-%d %H:%M:%S"))
    readings.insert(6, -1.0)
    readings.insert(7, -1.0)

    file_full_path = fileFolder + csv_file_name

    with open(file_full_path, 'a') as file:
        writer = csv.writer(file)

        if os.stat(file_full_path).st_size == 0:
            writer.writerow(["datetime", "VOC", "CO2", "humidity", "temperature", "water_temperature", "pH", "EC"])

        writer.writerow(readings)

    write_html_file(file_full_path)


def write_html_file(file_full_path=None):
    df = pd.read_csv(file_full_path)
    html_file_path: str = fileFolder + html_file_name
    fig = px.line(df, x='datetime', y=['CO2', 'VOC', 'humidity', 'temperature', 'water_temperature', 'pH', 'EC'],
                  title='Apple Share Prices over time (2014)')
    with open(html_file_path, 'w') as file:
        html = fig.to_html()
        file.write(html)


while True:

    now = datetime.now()

    if now.hour in syncHours:
        print("Getting sensors readings...")
        proceed()
        print("Data saving done.")

    time.sleep(55 * 60)  # 55m
