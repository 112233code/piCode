import board
import os
import time
import busio
from time import sleep
import Adafruit_ADS1x15
while 1:
    i2c = busio.I2C(board.SCL, board.SDA)
    adc = Adafruit_ADS1x15.ADS1115()
    ADS.gain =2
    value = adc.read_adc(0, gain=GAIN)
    volt = (value/65536*4.6)
    tds  = (-37.2)*volt*volt*volt + (533.4)*volt*volt + (121.8)*volt + 2.8
    print("TDS value is ",tds,"ppm")
    time.sleep(1)