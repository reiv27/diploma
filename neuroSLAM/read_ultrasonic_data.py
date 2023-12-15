import sys
import time
import serial
import numpy as np


arduino = serial.Serial('/dev/ttyUSB0', 9600)
time.sleep(2)
data_file = open(f'data/{sys.argv[1]}/{sys.argv[2]}.txt', 'w')

while True:
    python = arduino.readline()
    string = python.decode().rstrip()
    #triplet = tuple(map(np.uint16, string.split()))
    data_file.write(f'{string}\n')
    print(string)

data_file.close()
arduino.close()
