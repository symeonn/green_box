#!/bin/bash

logPath='/home/pi/gb_logs'

tail -f $logPath/temperature_control.log &
tail -f $logPath/meters_data_save.log &
tail -f $logPath/data_save.log &
tail -f $logPath/air_pump_control.log &
tail -f $logPath/image_capture.log
