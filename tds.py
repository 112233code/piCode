import board
import os
import time
import busio
from time import sleep
import Adafruit_ADS1x15.ADS1115 as ADS
from Adafruit_ADS1x15.analog_in import AnalogIn
while 1:
    i2c = busio.I2C(board.SCL, board.SDA)
    ads = ADS.ADS1115(i2c)
    ADS.gain =2
    chan = AnalogIn(ADS, ADS.P3)
    value = chan.value
    volt = (value/65536*4.6)
    tds  = (-37.2)*volt*volt*volt + (533.4)*volt*volt + (121.8)*volt + 2.8
    print("TDS value is ",tds,"ppm")
    time.sleep(1)