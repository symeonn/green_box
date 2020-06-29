#!/bin/bash

# BEWARE OF LINE ENDINGS

logsPath="/home/pi/gb_data/gb_logs/cron.log"

addDate() {
  while IFS= read -r line; do
    printf '%s: %s\n' "$(date '+%m-%d-%Y %H:%M   ')" "$line"
  done
}

echo "Daily restart..." | addDate >>$logsPath
sudo reboot
