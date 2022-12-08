# https://randomnerdtutorials.com/flashing-micropython-firmware-esptool-py-esp32-esp8266/

if [ -z "$ESP8266_PORT" ]; then
    export ESP8266_PORT="/dev/ttyUSB0" # mac /dev/tty.usbserial-0001
fi

echo "clearing flash"
esptool.py --chip esp8266 --port $ESP8266_PORT erase_flash

echo "adding firmware"
esptool.py --chip esp8266 --port $ESP8266_PORT write_flash --flash_mode dio --flash_size detect 0x0 firmwares/esp8266-20220618-v1.19.1.bin