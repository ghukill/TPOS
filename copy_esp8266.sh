if [ -z "$ESP8266_PORT" ]; then
    echo "defaults..."
    export ESP8266_PORT="/dev/ttyUSB0" # mac /dev/tty.usbserial-0001
fi

echo "copy config.json"
ampy --port $ESP8266_PORT put embedded/config.json

# copy wifi lib
echo "copying wifi libs"
ampy --port $ESP8266_PORT put embedded/wifi.py

# copy sonar lib
echo "copying sonar libs"
ampy --port $ESP8266_PORT put embedded/lib/hcsr04.py

echo "copying main.py"
ampy --port $ESP8266_PORT put embedded/main.py

echo "rebooting"
ampy --port $ESP8266_PORT reset