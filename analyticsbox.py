
#!/usr/bin/python
# Example using a character LCD plate.

# import Adafruit_CharLCD
import omniture
import os
import time

script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir, "auth/key.txt")

with open (abs_file_path, "r") as myfile:
    myKey = myfile.read().split('\n')


analytics = omniture.authenticate(myKey[0], myKey[1])

def realtimeOrders():
    params = {
        "reportDescription": {
            "source": "realtime",
            "reportSuiteID": "avgcorporatepublicww",
            "metrics": [
                { "id": "orders" }
            ]
        }
    }
    response = analytics.request('Report', 'Run', params)
    period = response['report']['period']
    total = response['report']['totals'][0]
    print period + ': ' + total
    exit()

def unknownOrders():
    exit()


while True:
    realtimeOrders()
    time.sleep(30)