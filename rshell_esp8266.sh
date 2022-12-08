if [ -z "$ESP8266_PORT" ]; then
    export ESP8266_PORT="/dev/ttyUSB0" # mac /dev/tty.usbserial-0001
fi

rshell --buffer-size=30 -p $ESP8266_PORT -a
