# HumLog.py
import logging
import datetime, time
import sys
import RPi.GPIO as GPIO


from UBI_Bubble_Log import UBILog
from ubidots import ApiClient
from LCD import *
from DS18B20 import read_temp, OneW_init

logging.basicConfig(filename="UbiBubbleLog.log", level=logging.INFO )

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

PhotoPIN = 11
GPIO.setup(PhotoPIN, GPIO.IN)
heatPin = 10
GPIO.setup(heatPin, GPIO.OUT, initial=1)
coolPin = 12
GPIO.setup(coolPin, GPIO.OUT, initial=1)

deviceFile2, deviceFile3 = OneW_init()

tNow = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
t = datetime.datetime.now()
Time = t.timetuple()
count = 0
BubCount = 0
FermentTarget = float(sys.argv[1])

logging.info("Program started ")

print("1")
LCD_clear()
print("2")
LCD_write("abcd1234",1)
print("3")
interval = 10   # initialize interval to 10 seconds

def MOTION(PhotoPIN):
    global BubCount
    BubCount +=1
#    print("Motion detected" + str(BubCount))
    LCD_write(", now " + str(BubCount),2 )

GPIO.add_event_detect(PhotoPIN, GPIO.RISING, callback=MOTION, bouncetime=200)
#GPIO.add_event_detect(PhotoPIN, GPIO.BOTH, callback=MOTION, bouncetime=200)
    
def adjustTemp(pin, secs):
    GPIO.output(pin, GPIO.LOW)   #start heat
    while secs:
        time.sleep(1)
        secs -=1
    GPIO.output(pin, GPIO.HIGH)  #end heat

print("starting... target = " + str(FermentTarget))

while True: 
    try:
        time.sleep(10)    #1800 = half hour
            
        t = datetime.datetime.now()

        TC_device2 = read_temp(deviceFile2)
        TC_device3 = read_temp(deviceFile3) #ferment temperature

        print( "measure temp ds18b20 ", "#3", TC_device3, ", #2", TC_device2  )       
        LCD_clear()
        LCD_write("date "+str(t.day)+"/"+str(t.month) + " at " + str(t.hour) + ":" + str(t.minute),1 )
        LCD_write("last bubble count:" + str(BubCount),2 )

        if TC_device3 < (FermentTarget-0.5):
            adjustTemp(heatPin, 3)
        elif TC_device3 > (FermentTarget+0.5):
            adjustTemp(coolPin, 3)


        old_interval = interval
        interval = UBILog(BubCount, TC_device2, TC_device3)       #(bubbles, room, ferment)
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
