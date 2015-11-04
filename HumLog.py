# HumLog.py

import datetime, time
from GLog import GLog
from BME280 import BME280read

tNow = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
t = datetime.datetime.now()

try:

    while True:

        t = datetime.datetime.now()
        
        values = BME280read()
        GLog( t, float(values[0]), float(values[1]), float(values[2])  )
        #print(values)

        time.sleep(5)

except KeyboardInterrupt:

    print("Program interrupted by Keyboard!")

print("Goodbye")
