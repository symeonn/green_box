from dataclasses import dataclass
import json
from json import JSONEncoder
from git import Repo
from datetime import datetime
import os

DATA_PATH = '/home/pi/gb_data/'


@dataclass
class CurrentState:
    local_ip: str
    vpn_ip: str
    voc: float
    co2: float
    humidity: float
    temperature: float
    water_temperature: float
    ph: float
    ec: float
    datetime: str = datetime.now().strftime("%Y-%m-%d_%H:%M")


class CurrentStateEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def get_ip():
    vpn_ip = os.popen("sudo ifconfig | grep 'inet 10.8.0' | sed -e 's/^[[:space:]]*//' | cut -d' ' -f 2").read().strip()
    local_ip = os.popen(
        "sudo ifconfig | grep 'inet 192.168.' | sed -e 's/^[[:space:]]*//' | cut -d' ' -f 2").read().strip()

    return local_ip, vpn_ip


def get_latest_data():
    voc, co2, humidity, temperature, water_temperature, ph, ec = get_data_from_csv()

    local_ip, vpn_ip = get_ip()
    # print("get_latest_data")
    # print(voc, co2, humidity, temperature, water_temperature, ph, ec)

    curr_state = CurrentState(local_ip, vpn_ip, voc, co2, humidity, temperature, water_temperature, ph, ec)
    return curr_state


def get_data_from_csv(line_from_end=1):
    # print(line_from_end)
    with open(DATA_PATH + 'gb_csv/grow_data.csv') as csv:
        lines = csv.read().splitlines()

        if lines:
            last_line = lines[-line_from_end]

            # print("get_data_from_csv")
            # print(last_line)
            cells = last_line.split(',')

            voc = cells[1]
            co2 = cells[2]
            humidity = cells[3]
            temperature = cells[4]
            water_temperature = cells[5]
            ph = cells[6]
            ec = cells[7]

            if float(ph) <= 0 or float(ec) <= 0:
                vocT, co2T, humidityT, temperatureT, water_temperatureT, phT, ecT = get_data_from_csv(line_from_end + 1)

                if float(ph) <= 0:
                    ph = phT
                if float(ec) <= 0:
                    ec = ecT

            return float(voc), float(co2), float(humidity), float(temperature), float(water_temperature), float(
                ph), float(ec)


def create_json():
    curr_state = get_latest_data()
    print(curr_state)

    save_json(curr_state)


def save_json(curr_state):
    with open(DATA_PATH + 'current_data.json', 'w') as outfile:
        json.dump(curr_state, outfile, cls=CurrentStateEncoder)


def push_to_repo():
    repo = Repo(DATA_PATH)
    repo.git.add('--all')
    repo.index.commit("data push")

    origin = repo.remote('origin')
    origin.push()


def sync():
    create_json()
    push_to_repo()


sync()
