# GLog
import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials


def GLog(dT, hP, rH, tC):
    json_key = json.load(open('Uploader-8ffdcddb7d70.json'))
    scope = ['https://spreadsheets.google.com/feeds']

    credentials = SignedJwtAssertionCredentials(json_key['client_email'],
                                             json_key['private_key'].encode(),
                                             scope )

    gc = gspread.authorize(credentials)
    wks = gc.open("TestOauthSheet").sheet1

    values = [dT, 'BME280', hP, rH, tC]

    wks.append_row(values)

    


