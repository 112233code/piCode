import board
import os
import time
import busio
from time import sleep
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
while 1:
    i2c = busio.I2C(board.SCL, board.SDA)
    ads = ADS.ADS1115(i2c)
    ads.gain =2
    chan = AnalogIn(ads, ADS.P1)
    value = chan.value
    volt = (value/65536*4.6)
    Ph  = (-18.75)*volt + 15.53
    print("Ph value is ",ph,"ph")
    time.sleep(1)