#!/usr/bin/env python3
import rainmaker        #supporting functions
from config import *    #import configuration variables
import sys              #capture arguments
import pymysql
from time import sleep

# load latest user input if any
conn = rainmaker.create_db_connection()
c = conn.cursor() 
c.execute("SELECT * from config where id='skip'")
data = c.fetchone()
skip = int(data[1])

# check if this watering should be skipped
if skip > 0:
    rainmaker.log_and_notify(f"no watering today skipping {skip - 1} more watering")
    c.execute(f"UPDATE config SET value = {skip - 1} WHERE id='skip'")
    conn.commit()
else:
    rainmaker.record_forecast()
    forecasts = rainmaker.get_forecast()
    
    if sum(forecasts[:13]) < RAIN_FORECAST_12HRS_MIN:
        rainmaker.open_valve(WATERING_TIME,15)

        # open 2nd valve
        # rainmaker.open_valve(WATERING_TIME,21)
        # c.execute(f"UPDATE config set value='0' where id='skip';")
        # conn.commit()
    else:
        rainmaker.log_and_notify(f"no watering today there is {sum(forecasts[:13])} rain forecast in the next 12 hours")

c.close()
conn.close()
