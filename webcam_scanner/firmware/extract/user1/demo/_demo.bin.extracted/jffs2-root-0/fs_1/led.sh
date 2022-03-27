#!/bin/sh

echo 38 > /sys/class/gpio/export
echo 39 > /sys/class/gpio/export

echo out > /sys/class/gpio/gpio38/direction
echo out > /sys/class/gpio/gpio39/direction

while true
do
        echo 1 > /sys/class/gpio/gpio39/value
        echo 1 > /sys/class/gpio/gpio38/value
        sleep 1
        echo 0 > /sys/class/gpio/gpio39/value
        echo 0 > /sys/class/gpio/gpio38/value 
        sleep 1
done
