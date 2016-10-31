# UBILog.py
from ubidots import ApiClient
from key import ubiKEY
import logging

def UBILog(dT, hP, rH, tC, TC1, TC2 ):

        try:

                api = ApiClient(ubiKEY)

                varTemperature = api.get_variable('57f814887625420821011130')
                varHumidity = api.get_variable('57f81f3f762542423c82b54a')
                varInterval = api.get_variable('57f89eb476254264592de214')
                varT_DS18b20_1 = api.get_variable('57f948e37625425f615546dc')
                varT_DS18b20_2 = api.get_variable('57f9492d7625426071c1d3ee')
        
                # save values to ubidots cloud
                response1 = varTemperature.save_value({'value':tC})
                response2 = varHumidity.save_value({'value':rH})
                response3 = varT_DS18b20_1.save_value({'value':TC1})
                response4 = varT_DS18b20_2.save_value({'value':TC2})

                #get value from ubidots cloud

                intInterval = int(varInterval.get_values(1)[0]['value'])
                
                return intInterval
        
                
        except UbidotsError400 as e:
                print("Code Exception: Error400 in UBILog.py", e.message, " and the details: ", e.detail)

        except UbidotsError404 as e:
                print("Code exception: Error404 in UBILog.py: ", e.message, " and the details: ", e.detail)

        except:
                print("generel exception ")
                return 30 #wait 30secs for next data upload


    
            

    


