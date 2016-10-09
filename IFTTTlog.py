# IFTTTlog
import time,datetime
import json
import logging
import urllib.request
import urllib.parse

from key import KEY

def IFTTTGLog(dT, hP, rH, tC, TC1, TC2 ):

        try:
            url = 'https://maker.ifttt.com/trigger/tempChanged/with/key/'+KEY
            values = {'value1':hP, 'value2':rH, 'value3':tC, 'value4':TC1, 'value5':TC2 }

            data = urllib.parse.urlencode(values)
            data = data.encode('utf-8')

            req = urllib.request.Request(url, data)
            #req.add_header('Content-type', 'application/json; charset=UTF-8')

#            print('sending now')
            response = urllib.request.urlopen(req)
#            print('sent')

            d = response.read()
#            print( d )

                
        except OSError as e:
            # 101 is "network is unreachable"
            print("Exception OSError occurred #", e, " at ", datetime.datetime.now() )
            time.sleep(10)
            logging.info("OSerror exception")


    
            

    


