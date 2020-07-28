#!/bin/bash

scriptsPath='/home/pi/green_box'

python -u $scriptsPath/air_pump_control.py &
python -u $scriptsPath/data_save.py &
python -u $scriptsPath/image_capture.py &
python -u $scriptsPath/meters_data_save.py &
python -u $scriptsPath/temperature_control.py &
