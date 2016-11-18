# UBILog.py
from ubidots import ApiClient
from key import ubiKEY
import logging

def UBILog( BC ):

        try:
                api = ApiClient(ubiKEY)
                
        except UbidotsError400 as e:
                print("Code Exception: Error400 in UBILog.py" + e.message + " and the details: " + e.detail)

        except UbidotsError403 as e:
                print("Code exception: Error403 in UBILog.py: " + e.message + " and the details: " + e.detail)

        except UbidotsError404 as e:
                print("Code exception: Error404 in UBILog.py: " + e.message + " and the details: " + e.detail)

        except UbidotsError405 as e:
                print("Code exception: Error405 in BubbleLog.py: " + e.message + " and the details: " + e.detail)

        varBubbles = api.get_variable('5820ee3276254272738bb134')
#                varInterval = api.get_variable('57f89eb476254264592de214')
                
                # save values to ubidots cloud
        response1 = varBubbles.save_value({'value':BC})
                
                #get value from ubidots cloud
#                intInterval = int(varInterval.get_values(1)[0]['value'])
                
#                return intInterval

    
            

    


