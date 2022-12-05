# Complete project details at https://RandomNerdTutorials.com/micropython-hc-sr04-ultrasonic-esp32-esp8266/

import json
from time import sleep
import urequests

from hcsr04 import HCSR04
from wifi import wifi_connect

# load config
try:
    with open("config.json", "r") as f:
        config = json.loads(f.read())
        print("config successfully loaded")
except Exception as e:
    print("error loading config: %s" % str(e))

# connect to wifi
wifi_connect(config["wifi"]["ssid"], config["wifi"]["password"])

# TODO: move to module
# setup sonar
# ESP32 chip
# sensor = HCSR04(trigger_pin="Y2", echo_pin="Y3", echo_timeout_us=10000)
# ESP8266 chip
sensor = HCSR04(trigger_pin=12, echo_pin=14, echo_timeout_us=10000)
while True:

    # get distance
    distance = sensor.distance_cm()
    print("Distance:", distance, "cm")

    # send API call
    url = "%s/?distance=%s" % (config["api"]["url_base"].rstrip("/"), distance)
    print(url)
    try:
        urequests.get(url)
    except Exception as e:
        print("error sending API request: %s" % str(e))

    sleep(2)
