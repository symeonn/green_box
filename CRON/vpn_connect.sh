#!/bin/bash

addDate() {
    while IFS= read -r line; do
        printf '%s: %s\n' "$(date '+%m-%d-%Y %H:%M   ')" "$line";
    done
}


logsPath="/home/pi/gb_logs/vpn.log"
vpn_conn=$(sudo ifconfig | grep tun)


echo $vpn_conn | addDate >> $logsPath

if [[ $vpn_conn == '' ]]
then

	echo "VPN not connected. Connecting..." | addDate >> $logsPath
	sudo openvpn --config /home/pi/N.ovpn
else
	echo "VPN connected. Idle..." | addDate >> $logsPath
fi


#echo $(ifconfig)
