# HumLog.py
import logging
import datetime, time
import RPi_I2C_driver
#import LCD
from GLog import GLog
from BME280 import BME280read
from DS18B20 import read_temp, OneW_init
from IFTTTlog import IFTTTGLog
from UBILog import UBILog
from LCD import *

logging.basicConfig(filename="BME280LOG.log", level=logging.INFO )


tNow = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
t = datetime.datetime.now()
Time = t.timetuple()
count = 0
values = (0,0,0)

deviceFile2, deviceFile3 = OneW_init()
#device_file3 = '/sys/bus/w1/devices/28-000004e01b0c/w1_slave'
#device_file2 = '/sys/bus/w1/devices/28-000005454cf7/w1_slave'

logging.info("Program started ")

print("1")
LCD_clear()
print("2")
LCD_write("abcd1234",1)
print("3")
LCD_write("date "+str(Time[2])+"/"+str(Time[1]) + " at " + str(Time[3]) + ":" + str(Time[3]),2 )
print("4")
interval = 10   # initialize interval to 10 seconds
try:
    while True:
        t = datetime.datetime.now()
        
        values = BME280read()
        TC_device2 = read_temp(deviceFile2)
        TC_device3 = read_temp(deviceFile3)

#        print(count, "On", t.day, "at", t.hour,':', t.minute, "measure ", float(values[2]),
#              "temp ds18b20 ", "#3", TC_device3, ", #2", TC_device2  )

        LCD_clear()
        LCD_write("date "+str(t.day)+"/"+str(t.month) + " at " + str(t.hour) + ":" + str(t.minute),1 )
        LCD_write("hP:" + str(int(float(values[0]))) + " rH:" + str(int(float(values[1]))) + " tC:" + str(int(float(values[2]))),2 )

#        interval = 900                   
#        GLog( t, float(values[0]), float(values[1]), float(values[2]), TC_device3, TC_device2 )
#        IFTTTGLog( t, float(values[0]), float(values[1]), float(values[2]), TC_device3, TC_device2 )
        old_interval = interval
        interval = UBILog(t, float(values[0]), float(values[1]), float(values[2]), TC_device3, TC_device2)       

        if interval != old_interval:
            print("new inteval set to ", interval)

        #time.sleep(300)
        for i in range(1, interval):      #prevent system hang by waiting range(30) seconds
            time.sleep(1)

        count = count + 1
        

except KeyboardInterrupt:

    print("Program interrupted by Keyboard!")
    logging.info("Program exit" )


print("Goodbye")
