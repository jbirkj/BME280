# HumLog.py

import datetime, time
from GLog import GLog
from BME280 import BME280read
from DS18B20 import read_temp, OneW_init

tNow = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
t = datetime.datetime.now()
count = 0
values = (0,0,0)

deviceFile2, deviceFile3 = OneW_init()
#device_file3 = '/sys/bus/w1/devices/28-000004e01b0c/w1_slave'
#device_file2 = '/sys/bus/w1/devices/28-000005454cf7/w1_slave'

try:
    while True:
        t = datetime.datetime.now()
        
        values = BME280read()
        TC_device2 = read_temp(deviceFile2)
        TC_device3 = read_temp(deviceFile3)
        
        GLog( t, float(values[0]), float(values[1]), float(values[2]), TC_device3, TC_device2 )
        
        print(count, "On", t.day, "at", t.hour,':', t.minute, "measure ", float(values[2]),
              "temp ds18b20 ", "#3", TC_device3, ", #2", TC_device2  )

        #time.sleep(300)
        for i in range(1, 30):      #prevent system hang by waiting range(30) seconds
            time.sleep(1)

        count = count + 1
        

except KeyboardInterrupt:

    print("Program interrupted by Keyboard!")

print("Goodbye")
