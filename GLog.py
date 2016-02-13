# GLog
import time,datetime
import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials


def GLog(dT, hP, rH, tC):

    retry = 3
    while retry > 0:
    
        try:

            json_key = json.load(open('Uploader-8ffdcddb7d70.json'))
            scope = ['https://spreadsheets.google.com/feeds']

            credentials = SignedJwtAssertionCredentials(json_key['client_email'],
                                                 json_key['private_key'].encode(),
                                                 scope )
            #raise  gspread.exceptions.HTTPError()
        
            gc = gspread.authorize(credentials)
            wks = gc.open("TestOauthSheet2").sheet1

            values = [dT, 'BME280', hP, rH, tC]

            wks.append_row(values)

            #print( "exception not hit" )

            retry = 0
            

        except gspread.exceptions.HTTPError:
            time.sleep(5)
            print("exception caught no ", retry, " at ", datetime.datetime.now() )
            retry -= 1



    
            

    


