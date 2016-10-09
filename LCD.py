# LCD functions
import sys

sys.path.append("/home/pi/git/quick2wire-python-api")
from quick2wire.i2c import I2CMaster, writing_bytes, reading

address = 0x28
Tekst = [ 0x54, 0x65, 0x6d, 0x70, 0x31, 0x3d ]		#"Temp1="
Tekst1 = [ 0x20, 0x54, 0x65, 0x6d, 0x70, 0x33, 0x3d ]	#" Temp3="
Tekst2 = [ 0xfe, 0x47, 0x01, 0x02, 0x54, 0x65, 0x6d, 0x70, 0x32, 0x3d ]  # næste linie, pos 1, "Temp2="


def LCD_clear():
    # Write to LCD - clear displa and move cursor to start
    I2CWrite(0xFE)  #cmd prefix
    I2CWrite(0x58)  #clear LCD and cursor back up
    I2CWrite(0xFE)
#    I2CWrite(0x42)  #backlight ON
#    I2CWrite(0x00)  #ON minutes = indefinitely
    I2CWrite(0x46)  #backlight OFF
    I2CWrite(0xFE)  #cmd prefix
    I2CWrite(0x4B)  #cursor OFF
    

def LCD_write(string, line):
    vals = [ 0xFE, 0x47, 0x01, line ]   #cursor set at start of _line_
    for a in range(len(vals)):
        I2CWrite(vals[a])
    for b in string:
        I2CWrite(ord(b))

#    I2CWrite(0x30+(int(T1/10)))      
#    I2CWrite(0x30+(int(T1%10)))                 

def LCDupdate(T1, T2, T3):
    
    # Write to LCD - clear displa and move cursor to start
    I2CWrite(0xFE)
    I2CWrite(0x58)
                        
    # writing LCD line1 with "Temp1="
    for a in range(len(Tekst)):
            I2CWrite(Tekst[a])
    I2CWrite(0x30+(int(T1/10)))      
    I2CWrite(0x30+(int(T1%10)))             
                        
    #cont line wirting " Temp3=
    for a in range(len(Tekst1)):
            I2CWrite(Tekst1[a])
    I2CWrite(0x30+(int(T3/10)))      
    I2CWrite(0x30+(int(T3%10)))             
                        
    # writing LCD line 2 with Temp2
    for a in range(len(Tekst2)):
            I2CWrite(Tekst2[a])
    I2CWrite(0x30+(int(T2/10)))
    I2CWrite(0x30+(int(T2%10)))

    return 1

def I2CWrite(value1) :
    with I2CMaster() as bus:
        bus.transaction( writing_bytes(address, value1) )
    return 1

def I2CRead():
    with I2CMaster() as bus:
        read = bus.transaction( reading(address, 1) )[0]
    return read
