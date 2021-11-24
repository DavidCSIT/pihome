#!/usr/bin/env python3
import rainmaker        #supporting functions
from config import *    #import configuration variables
import sys              #capture arguments
import pymysql
from time import sleep

def water_if_required_scheduled() :

    # Connect to the database.
    conn = pymysql.connect(db=DATABASE,
        user=USER,
        passwd=PASSWD,
        host=HOST)
    c = conn.cursor()

    # get latest forecast
    forecasts = rainmaker.get_forecast()

    # load latest user input if any
    c.execute("SELECT * from config where id='skip'")
    data = c.fetchone()
    skip = int(data[1])

    # check if this watering should be skipped
    if skip > 2:
        rainmaker.log_and_notify(f"no watering today skipping {skip - 1} more watering")
        c.execute(f"UPDATE config SET value = {skip - 1} WHERE id='skip'")
        conn.commit()
    else:
        rainmaker.open_valve(WATERING_TIME,15)
        c.execute(f"UPDATE config set value='0' where id='skip';")
        conn.commit()

        rainmaker.open_valve(WATERING_TIME,21)
        c.execute(f"UPDATE config set value='0' where id='skip';")
        conn.commit()

    c.close()
    conn.close()

water_if_required_scheduled()

