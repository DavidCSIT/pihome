#!/usr/bin/env python3
import rainmaker    #supporting functions
import config       #import configuration variables
import sys          #capture arguments

def water_if_required() :
    #if argument is provided water now
    if len(sys.argv) > 1:
        rainmaker.log_and_notify(f"Watering Started Manual watering")
        rainmaker.open_valve(config.WATERING_TIME)
        quit()
    else:
        rainmaker.log_and_notify(f"test")
        rainmaker.open_valve(config.WATERING_TIME)
        quit()
    
    #get latest forecast
    #forecasts = rainmaker.get_forecast()
   
water_if_required()

