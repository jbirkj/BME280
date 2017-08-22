# HumLog.py
import logging
import datetime, time
import sys
import RPi.GPIO as GPIO


from UBI_Bubble_Log import UBILog
from ubidots import ApiClient
#from LCD import *

logging.basicConfig(filename="UbiBubbleLog.log", level=logging.INFO )

GPIO.setmode(GPIO.BCM)

PIR_PIN = 7
PhotoPIN = 17
GPIO.setup(PhotoPIN, GPIO.IN)


tNow = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
t = datetime.datetime.now()
Time = t.timetuple()
count = 0
BubCount = 0

logging.info("Program started ")

print("1")
#LCD_clear()
print("2")
#LCD_write("abcd1234",1)
print("3")
interval = 10   # initialize interval to 10 seconds

def MOTION(PIR_PIN):
    global BubCount
#    print("Motion detected" + str(BubCount))
    BubCount +=1
#    LCD_write(", now " + str(BubCount),2 )
    
    

print("starting...")

GPIO.add_event_detect(PhotoPIN, GPIO.RISING, callback=MOTION, bouncetime=200)
#GPIO.add_event_detect(PhotoPIN, GPIO.BOTH, callback=MOTION, bouncetime=200)

while True: 
    try:

#        print("entering loop")
        '''       
        if GPIO.input(PIR_PIN):
            print("Motion detected")
            BubCount +=1
        '''        
        time.sleep(900)    #1800 = half hour

        t = datetime.datetime.now()
        
#        LCD_clear()
#        LCD_write("date "+str(t.day)+"/"+str(t.month) + " at " + str(t.hour) + ":" + str(t.minute),1 )
#        LCD_write("last bubble count:" + str(BubCount),2 )

        old_interval = interval
        interval = UBILog(BubCount)       
        '''
        if interval != old_interval:
            print("new inteval set to ", interval)

        #time.sleep(300)
        for i in range(1, interval):      #prevent system hang by waiting range(30) seconds
            time.sleep(1)
        '''
        count = count + 1
        BubCount = 0
        

    except KeyboardInterrupt:
        print("Program interrupted by Keyboard!")
        logging.info("Program exit" )
        break
    

#    except UbidotsError400 as e:
#            print("Code Exception: Error400 in BubbleLog.py", e.message, " and the details: ", e.detail)
#
#    except UbidotsError403 as e:
#            print("Code exception: Error403 in BubbleLog.py: ", e.message, " and the details: ", e.detail)
#
#    except UbidotsError404 as e:
#            print("Code exception: Error404 in BubbleLog.py: ", e.message, " and the details: ", e.detail)
#
#    except UbidotsError405 as e:
#            print("Code exception: Error405 in BubbleLog.py: ", e.message, " and the details: ", e.detail)
    except:
        print("unknown exception in BubbleLog.py :", sys.exc_info()[0])
        interval = 40   #retry in 40 secs

print("Goodbye")
