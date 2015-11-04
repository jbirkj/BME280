#BME280
from subprocess import Popen, PIPE


def BME280read():
    proc = Popen('read_bme280 --i2c-address 0x76', shell=True, stdout=PIPE,
             universal_newlines=True)               # uni_newline is to return string and not byte format
    stdoutvalue = proc.communicate()
#    tempread = str(stdoutvalue[0]).split()[0]       # remove stderr [1]

    hPa = str(stdoutvalue[0]).split()[0]
    relH = str(stdoutvalue[0]).split()[2]
    temp = str(stdoutvalue[0]).split()[4]

    return hPa, relH, temp

