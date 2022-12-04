# https://randomnerdtutorials.com/flashing-micropython-firmware-esptool-py-esp32-esp8266/

echo "clearing flash"
esptool.py --chip esp8266 --port /dev/ttyUSB0 erase_flash

echo "adding firmware"
esptool.py --chip esp8266 --port /dev/ttyUSB0 write_flash --flash_mode dio --flash_size detect 0x0 ~/dev/sandbox/espx/firmwares/esp8266-20220618-v1.19.1.bin