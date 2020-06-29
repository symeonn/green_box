#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")
pwd
fswebcam --no-banner -r 1600x1200 -p YUYV -S 1 --jpeg 95 /home/pi/gb_data/gb_cam_images/$DATE.jpg
