#!/bin/bash

addDate() {
    while IFS= read -r line; do
        printf '%s: %s\n' "$(date '+%m-%d-%Y %H:%M   ')" "$line";
    done
}

syncData() {
	echo "SYNC images:"
	rsync -azvhO /home/pi/gb_cam_images greenbox@192.168.0.19:/share/green_box/

	echo "SYNC CSV:"
	rsync -azvhO /home/pi/gb_CSV greenbox@192.168.0.19:/share/green_box/
}

syncData | addDate >> /home/pi/gb_logs/rsync.log 2>&1
