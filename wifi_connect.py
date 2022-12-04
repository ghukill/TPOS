
import network
import time
import urequests

def wifi_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect('ruby-ddwrt2ghz', 'DumpsterTurkey')
    while True:
        if wlan.isconnected():
            break
        else:
            time.sleep(1)

def update_door(is_open=1):
    response = urequests.post('http://192.168.1.123:5000', data={'door_open':is_open})
    print(response.text)
