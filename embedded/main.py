# Complete project details at https://RandomNerdTutorials.com/micropython-hc-sr04-ultrasonic-esp32-esp8266/

from collections import deque
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

# setup sonar
sensor = HCSR04(trigger_pin=12, echo_pin=14, echo_timeout_us=10000) # ESP8266 chip


def update_distance(d):
    url = "%s/stairs/distance?distance=%s" % (config["api"]["url_base"].rstrip("/"), d)
    try:
        urequests.get(url)
    except Exception as e:
        print("error sending API request: %s" % str(e))

# main loop
sent = False

# set update time and refresh time, which determines queue size
update_time = 5
read_time = 0.25
queue_len = int(update_time / read_time)

# create queue
d = deque((), queue_len)

while True:

    # if queue full, dump to db
    if len(d) == queue_len:
        distances = [d.popleft() for _ in range(queue_len)]
        distances = [d for d in distances if d > 0]
        try:
            avg_distance = round((sum(distances) / len(distances)), 2)
        except ZeroDivisionError:
            continue
        print("SENDING AVG:", avg_distance)
        update_distance(avg_distance)

    # get distance and push to queue
    distance = sensor.distance_cm()
    d.append(distance)

    # sleep
    sleep(0.25)







