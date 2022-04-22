import board
import os
import time
import busio
from time import sleep
import Adafruit_ADS1x15
adc = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)
Gain = 1
count = 0
while 1:
    count += 1
    print (count)
    value = [0]
    value[0] = adc.read_adc(0, gain=Gain)
    volt = value[0]* 4.06 / 32768 
    Ph  = (-3.125)*volt + 15.0625
    print("Ph value is ",Ph,"ph")
    time.sleep(1)

