# UBILog.py
from ubidots import ApiClient
from key import ubiKEY
import logging

def UBILog( BC, Temp1, Temp2 ):

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
        varBubTemp2 = api.get_variable('58879f4476254260ed35e396')	#room temp (raw component)
        
        varBubTemp3 = api.get_variable('57f9492d7625426071c1d3ee')	#fermentor temp (metal tip probe)
        
                
                # save values to ubidots cloud
        response1 = varBubbles.save_value({'value':BC})
        response2 = varBubTemp2.save_value({'value':Temp1})
        response3 = varBubTemp3.save_value({'value':Temp2})
                
                #get value from ubidots cloud
#                intInterval = int(varInterval.get_values(1)[0]['value'])
                
#                return intInterval

    
            

    


