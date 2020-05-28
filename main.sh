#!/bin/bash

logsPath='/home/pi/gb_logs'
scriptsPath='/home/pi/green_box'

addDate() {
    while IFS= read -r line; do
        printf '%s: %s\n' "$(date '+%m-%d-%Y %H:%M   ')" "$line";
    done
}

python -u $scriptsPath/air_pump_control.py | addDate >> $logsPath/air_pump_control.log 2>&1 &
python -u $scriptsPath/data_save.py | addDate >> $logsPath/data_save.log 2>&1 &
python -u $scriptsPath/image_capture.py | addDate >> $logsPath/image_capture.log 2>&1 &
python -u $scriptsPath/meters_data_save.py | addDate >> $logsPath/meters_data_save.log 2>&1 &
python -u $scriptsPath/temperature_control.py | addDate >> $logsPath/temperature_control.log 2>&1 &
