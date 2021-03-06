#!/bin/bash

# BEWARE OF LINE ENDINGS

logsPath="/home/pi/gb_data/gb_logs/cron.log"

addDate() {
  while IFS= read -r line; do
    printf '%s: %s\n' "$(date '+%m-%d-%Y %H:%M   ')" "$line"
  done
}

syncLogs() {
  echo "SYNC logs:"
  rsync -azvhO /home/pi/gb_data/gb_logs greenbox@192.168.0.19:/share/green_box/
}

syncLogs | addDate >>$logsPath
