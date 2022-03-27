#!/bin/sh

WIFI_CONF_FILE="/etc/miio/wifi.conf"
DEVICE_CONFIG_FILE="/etc/miio/device.conf"
WIFI_SETUP_SCRIPT="/path/to/marvell_wifi_setup.sh"

wifi_ap_mode()
{
    # wifi stop
    CMD="${WIFI_SETUP_SCRIPT}  mlan0 stop"
    echo "CMD=${CMD}"
    #${CMD}

    # AP mode
    MODEL=`cat $DEVICE_CONFIG_FILE | grep -v ^#`
    MODEL=${MODEL##*model=}
    MODEL=`echo $MODEL | cut -d ' ' -f 1`
    vendor=`echo ${MODEL} | cut -d '.' -f 1`
    product=`echo ${MODEL} | cut -d '.' -f 2`
    version=`echo ${MODEL} | cut -d '.' -f 3`

    CMD="${WIFI_SETUP_SCRIPT}  mlan0 ap nl80211 ${vendor}-${product}-${version}_miap$1 0 open"
    echo "CMD=${CMD}"
    #${CMD}
}

wifi_sta_mode()
{
    # wifi stop
    CMD="${WIFI_SETUP_SCRIPT}  mlan0 stop"
    echo "CMD=${CMD}"
    #${CMD}

    # STA mode
    CMD="${WIFI_SETUP_SCRIPT}  mlan0 sta nl80211 $1 $2"
    echo "CMD=${CMD}"
    #${CMD}
}

get_ssid_passwd()
{
    STRING=`cat $WIFI_CONF_FILE | grep -v ^#`
    key_mgmt=${STRING##*key_mgmt=}
    if [ $key_mgmt == "NONE" ]; then
	passwd=""

	ssid=${STRING##*ssid=\"}
	ssid=${ssid%%\"*}
    else
	passwd=${STRING##*psk=\"}
	passwd=${passwd%%\"*}

	ssid=${STRING##*ssid=\"}
	ssid=${ssid%%\"*}
    fi
}

start()
{
    if [ -e $WIFI_CONF_FILE ]; then
	get_ssid_passwd
	wifi_sta_mode $ssid $passwd
    else
	STRING=`ifconfig mlan0`

	macstring=${STRING##*HWaddr }
	macstring=`echo ${macstring} | cut -d ' ' -f 1`

	mac1=`echo ${macstring} | cut -d ':' -f 5`
	mac2=`echo ${macstring} | cut -d ':' -f 6`
	MAC=${mac1}${mac2}

	wifi_ap_mode $MAC
    fi
}

start
