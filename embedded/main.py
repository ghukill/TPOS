# Complete project details at https://RandomNerdTutorials.com/micropython-hc-sr04-ultrasonic-esp32-esp8266/
# from hcsr04 import HCSR04

import network
from time import sleep

# ESP32
# sensor = HCSR04(trigger_pin="Y2", echo_pin="Y3", echo_timeout_us=10000)

# ESP8266
#sensor = HCSR04(trigger_pin=12, echo_pin=14, echo_timeout_us=10000)


# while True:
#
#     # # distance
#     # distance = sensor.distance_cm()
#     # print('Distance:', distance, 'cm')
#     # sleep(0.25)
#     test()

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('ruby-ddwrt2ghz', 'DumpsterTurkey')
while True:
    if wlan.isconnected():
        print('connected to wifi')
        break
    else:
        sleep(0.25)
