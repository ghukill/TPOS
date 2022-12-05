""""""
import network
import time


def wifi_connect(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    for x in range(600):  # try for 5 minutes
        if wlan.isconnected():
            print("wifi connected")
            return True
        else:
            time.sleep(0.5)
    return False
