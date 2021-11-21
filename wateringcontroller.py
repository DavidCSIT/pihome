#!/usr/bin/env python3
import rainmaker        #supporting functions
from config import *    #import configuration variables
import sys              #capture arguments
import pymysql

def water_if_required() :
     # Connect to the database.
    conn = pymysql.connect(db=DATABASE,
        user=USER,
        passwd=PASSWD,
        host=HOST)
    c = conn.cursor()

    # load latest user input
    c.execute("SELECT * from config where id='skip'")
    data = c.fetchone()
    skip = int(data[1])

    skip = -2
    print(skip)

    # get latest forecast
    forecasts = rainmaker.get_forecast()

    # Check if manual watering required
    if skip == -1:
        rainmaker.log_and_notify(f"Watering Started Manual watering Garden")
        rainmaker.open_valve(WATERING_TIME,15)
        c.execute(f"UPDATE config set value='F' where id='heating';")
        conn.commit()
        c.execute(f"UPDATE config set value='0' where id='skip';")
        conn.commit()
    elif skip == -2:
        rainmaker.log_and_notify(f"Watering Started Manual watering Berries")
        rainmaker.open_valve(WATERING_TIME,21 )
        c.execute(f"UPDATE config set value='F' where id='heating';")
        conn.commit()
        c.execute(f"UPDATE config set value='0' where id='skip';")
        conn.commit()
    
        now = datetime.now()
         

water_if_required()

