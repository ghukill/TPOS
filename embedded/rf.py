
import machine
from machine import Pin, PWM
import time

class RFLinkTransmitter:
    def __init__(self, pin):
        self.pin = pin
        self.freq = 434000000

    def send(self, message):
        # set up the transmitter on the specified pin
        transmitter = Pin(self.pin, Pin.OUT)
        # create a PWM object with the specified frequency
        pwm = PWM(transmitter, freq=self.freq)
        # set the duty cycle to 50% to transmit the message
        pwm.duty(128)
        time.sleep_ms(len(message))
        # stop transmitting and clean up
        pwm.deinit()

class RFLinkReceiver:
    def __init__(self, pin):
        self.pin = pin
        self.freq = 434000000

    def receive(self):
        # set up the receiver on the specified pin
        receiver = Pin(self.pin, Pin.IN)
        # create a PWM object with the specified frequency
        pwm = PWM(receiver, freq=self.freq)
        # wait for the receiver to pick up a signal
        while pwm.duty() == 0:
            time.sleep_us(1)
        # read the message by measuring the duration of the signal
        start = time.ticks_us()
        while pwm.duty() > 0:
            time.sleep_us(1)
        end = time.ticks_us()
        # clean up and return the message
        pwm.deinit()
        return end - start