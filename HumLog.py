# HumLog.py

import datetime, time
from GLog import GLog
from BME280 import BME280read

tNow = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
t = datetime.datetime.now()
count = 0

try:

    while True:

       
        values = BME280read()
        
        GLog( t, float(values[0]), float(values[1]), float(values[2])  )
        
        print(count, t.hour,':', t.minute, "measure ", float(values[2]) )
        #time.sleep(60)
        count = count + 1

except KeyboardInterrupt:

    print("Program interrupted by Keyboard!")

print("Goodbye")
