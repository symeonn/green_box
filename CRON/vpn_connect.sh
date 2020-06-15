#!/bin/bash

addDate() {
  while IFS= read -r line; do
    printf '%s: %s\n' "$(date '+%m-%d-%Y %H:%M   ')" "$line"
  done
}

logsPath="/home/pi/gb_logs/cron.log"
vpn_conn=$(sudo ifconfig | grep tun)

#echo "$vpn_conn" | addDate >> $logsPath

if [[ $vpn_conn == '' ]]; then
  echo "VPN not connected. Connecting..." | addDate >>$logsPath
  sudo openvpn --config /home/pi/N.ovpn $
else
  echo "VPN connected. Idle..." | addDate >>$logsPath
fi

sleep 60

vpn_ip=$(sudo ifconfig | grep "inet 10.8.0" | sed -e 's/^[[:space:]]*//' | cut -d' ' -f 2)
echo "Current IP: ""$vpn_ip" | addDate >>$logsPath

#echo $(ifconfig)
