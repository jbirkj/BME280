# GLog
import time,datetime
import json
import gspread
import logging
from oauth2client.client import SignedJwtAssertionCredentials


def GLog(dT, hP, rH, tC, TC1, TC2 ):

        logging.basicConfig(filename="GLog.log", level=logging.INFO)

        try:

            json_key = json.load(open('Uploader-8ffdcddb7d70.json'))
            scope = ['https://spreadsheets.google.com/feeds']

            credentials = SignedJwtAssertionCredentials(json_key['client_email'],
                                                 json_key['private_key'].encode(),
                                                 scope )
            #raise  gspread.exceptions.HTTPError()
        
            gc = gspread.authorize(credentials)
            wks = gc.open("TestOauthSheet2").sheet1

            values = [dT, 'BME280', hP, rH, tC, 'DS18B20', TC1, TC2]

            wks.append_row(values)

            #print( "exception not hit" )

        except gspread.exceptions.HTTPError:
            time.sleep(10)
            print("exception gspread HTTPError caught at ", datetime.datetime.now() )
            logging.info("gspread exception")

        except OSError as e:
            # 101 is "network is unreachable"
            print("Exception OSError occurred #", e, " at ", datetime.datetime.now() )
            time.sleep(10)
            logging.info("OSerror exception")


    
            

    


