#!/bin/sh

WIFI_START_SCRIPT="/etc/miio_client/wifi_start.sh"
MIIO_RECV_LINE="/etc/miio_client/miio_recv_line"
MIIO_SEND_LINE="/etc/miio_client/miio_send_line"
WIFI_MAX_RETRY=5
WIFI_RETRY_INTERVAL=30
WIFI_SSID=

# contains(string, substring)
#
# Returns 0 if the specified string contains the specified substring,
# otherwise returns 1.
contains() {
    string="$1"
    substring="$2"
    if test "${string#*$substring}" != "$string"
    then
        return 0    # $substring is in $string
    else
        return 1    # $substring is not in $string
    fi
}

send_helper_ready() {
    ready_msg="{\"method\":\"_internal.helper_ready\"}"
    echo $ready_msg
    $MIIO_SEND_LINE "$ready_msg"
}

req_wifi_conf_status() {
    wificonf_dir=$1
    wificonf_dir=${wificonf_dir##*params\":\"}
    wificonf_dir=${wificonf_dir%%\"*}
    wificonf_file=${wificonf_dir}/wifi.conf

    REQ_WIFI_CONF_STATUS_RESPONSE=""
    if [ -e $wificonf_file ]; then
	REQ_WIFI_CONF_STATUS_RESPONSE="{\"method\":\"_internal.res_wifi_conf_status\",\"params\":1}"

	WIFI_SSID=`cat $wificonf_file | grep ssid`
	WIFI_SSID=${WIFI_SSID#*ssid=\"}
	WIFI_SSID=${WIFI_SSID%\"*}
	echo "WIFI_SSID_GUOZHIXIN: $WIFI_SSID"
    else
	REQ_WIFI_CONF_STATUS_RESPONSE="{\"method\":\"_internal.res_wifi_conf_status\",\"params\":0}"
    fi
}

request_dinfo() {
    dinfo_dir=$1
    dinfo_dir=${dinfo_dir##*params\":\"}
    dinfo_dir=${dinfo_dir%%\"*}
    dinfo_file=${dinfo_dir}/device.conf

    #dinfo_did=`cat $dinfo_file | grep -v ^# | grep did= | tail -1 | cut -d '=' -f 2`
    dinfo_did=`readFile $dinfo_file 'did='`
    sleep 1
    #dinfo_key=`cat $dinfo_file | grep -v ^# | grep key= | tail -1 | cut -d '=' -f 2`
    dinfo_key=`readFile $dinfo_file 'key='`
    sleep 1
    #dinfo_vendor=`cat $dinfo_file | grep -v ^# | grep vendor= | tail -1 | cut -d '=' -f 2`
    dinfo_vendor=`readFile $dinfo_file 'vendor='`
    sleep 1
    #dinfo_mac=`cat $dinfo_file | grep -v ^# | grep mac= | tail -1 | cut -d '=' -f 2`
    dinfo_mac=`readFile $dinfo_file 'mac='`
    sleep 1
    #dinfo_model=`cat $dinfo_file | grep -v ^# | grep model= | tail -1 | cut -d '=' -f 2`
    dinfo_model=`readFile $dinfo_file 'model='`
    sleep 1
    RESPONSE_DINFO="{\"method\":\"_internal.response_dinfo\",\"params\":{"
    if [ x$dinfo_did != x ]; then
	RESPONSE_DINFO="$RESPONSE_DINFO\"did\":$dinfo_did"
    else
	echo "did:"$dinfo_did
    fi
    if [ x$dinfo_key != x ]; then
	RESPONSE_DINFO="$RESPONSE_DINFO,\"key\":\"$dinfo_key\""
    else
	echo "key:"$dinfo_key
    fi
    if [ x$dinfo_vendor != x ]; then
	RESPONSE_DINFO="$RESPONSE_DINFO,\"vendor\":\"$dinfo_vendor\""
    else
	echo "vendor:"$vendor
    fi
    if [ x$dinfo_mac != x ]; then
	RESPONSE_DINFO="$RESPONSE_DINFO,\"mac\":\"$dinfo_mac\""
    else 
	echo "mac:"$mac
    fi
    if [ x$dinfo_model != x ]; then
	RESPONSE_DINFO="$RESPONSE_DINFO,\"model\":\"$dinfo_model\""
    else
	echo "model:"$model
    fi
    RESPONSE_DINFO="$RESPONSE_DINFO}}"
}

request_dtoken() {
    dtoken_string=$1
    dtoken_dir=${dtoken_string##*dir\":\"}
    dtoken_dir=${dtoken_dir%%\"*}
    dtoken_token=${dtoken_string##*ntoken\":\"}
    dtoken_token=${dtoken_token%%\"*}

    dtoken_file=${dtoken_dir}/device.token

    if [ ! -e ${dtoken_dir}/wifi.conf ]; then
	rm -f ${dtoken_file}
    fi

    if [ -e ${dtoken_file} ]; then
	dtoken_token=`cat ${dtoken_file}`
    else
	echo ${dtoken_token} > ${dtoken_file}
    fi

    RESPONSE_DTOKEN="{\"method\":\"_internal.response_dtoken\",\"params\":\"${dtoken_token}\"}"
}

main() {
    while true; do
	BUF=`$MIIO_RECV_LINE`
	if contains $BUF "_internal.info"; then
	    STRING=`wpa_cli status`

	    ifname=${STRING#*\'}
	    ifname=${ifname%%\'*}
	    echo "ifname: $ifname"

	    #if [ "x$WIFI_SSID" != "x" ]; then
	    #	ssid=$WIFI_SSID
	    #else
	    #	ssid=${STRING##*ssid=}
	    #	ssid=`echo ${ssid} | cut -d ' ' -f 1`
	    #fi
	    ssid=`readFile /etc/config/.wifissid`
	    echo "ssid: $ssid"

	    bssid=${STRING##*bssid=}
	    bssid=`echo ${bssid} | cut -d ' ' -f 1 | tr '[:lower:]' '[:upper:]'`
	    echo "bssid: $bssid"

	    ip=${STRING##*ip_address=}
	    ip=`echo ${ip} | cut -d ' ' -f 1`
	    echo "ip: $ip"

	    STRING=`ifconfig ${ifname}`

	    netmask=${STRING##*Mask:}
	    netmask=`echo ${netmask} | cut -d ' ' -f 1`
	    echo "netmask: $netmask"

	    gw=`route -n|grep 'UG'|tr -s ' ' | cut -f 2 -d ' '`
	    echo "gw: $gw"

	    # get vendor and then version
	    #vendor=`grep "vendor" /etc/miio/device.conf | cut -f 2 -d '=' | tr '[:lower:]' '[:upper:]'`
	    #sw_version=`grep "${vendor}_VERSION" /etc/os-release | cut -f 2 -d '='`
	    vendor=`readFile /etc/miio/device.conf 'vendor='`
	    sw_version=`readFile /etc/os-release 'ISA_VERSION='`
	    sleep 1
	    if [ -z $sw_version ]; then
		sw_version="unknown"
	    fi

	    msg="{\"method\":\"_internal.info\",\"partner_id\":\"\",\"params\":{\
\"hw_ver\":\"Linux\",\"fw_ver\":\"$sw_version\",\
\"ap\":{\
 \"ssid\":\"$ssid\",\"bssid\":\"$bssid\"\
},\
\"netif\":{\
 \"localIp\":\"$ip\",\"mask\":\"$netmask\",\"gw\":\"$gw\"\
}}}"

	    echo $msg
	    $MIIO_SEND_LINE "$msg"
	elif contains $BUF "_internal.req_wifi_conf_status"; then
	    echo "Got _internal.req_wifi_conf_status"
	    req_wifi_conf_status $BUF
	    echo $REQ_WIFI_CONF_STATUS_RESPONSE
	    $MIIO_SEND_LINE "$REQ_WIFI_CONF_STATUS_RESPONSE"
	elif contains $BUF "_internal.wifi_start"; then
	    wificonf_dir2=${BUF##*params\":\"}
	    wificonf_dir2=${wificonf_dir2%%\"*}
	    wificonf_file2=${wificonf_dir2}/wifi.conf

	    CMD=$WIFI_START_SCRIPT
	    RETRY=1
	    WIFI_SUCC=1
	    until [ $RETRY -gt $WIFI_MAX_RETRY ]
	    do
		WIFI_SUCC=1
		echo "Retry $RETRY: CMD=${CMD}"
		${CMD} && break
		let RETRY=$RETRY+1
		WIFI_SUCC=0
		sleep $WIFI_RETRY_INTERVAL
	    done

	    if [ $WIFI_SUCC -eq 1 ]; then
		msg="{\"method\":\"_internal.wifi_connected\"}"
		echo $msg
		$MIIO_SEND_LINE "$msg"
	   else
		rm $wificonf_file2
		CMD=$WIFI_START_SCRIPT
		echo "Back to AP mode, CMD=${CMD}"
		${CMD}
		msg="{\"method\":\"local.status\",\"params\":\"wifi_ap_mode_2\"}";
		echo $msg
		$MIIO_SEND_LINE "$msg"
	   fi
	elif contains $BUF "_internal.request_dinfo"; then
	    echo "Got _internal.request_dinfo"
	    request_dinfo $BUF
	    echo $RESPONSE_DINFO
	    $MIIO_SEND_LINE "$RESPONSE_DINFO"
	elif contains $BUF "_internal.request_dtoken"; then
	    echo "Got _internal.request_dtoken"
	    request_dtoken $BUF
	    echo $RESPONSE_DTOKEN
	    $MIIO_SEND_LINE "$RESPONSE_DTOKEN"
	else
	    sleep 1
	fi
    done
}

#sanity_check
send_helper_ready
main
