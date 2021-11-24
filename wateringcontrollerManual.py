#!/usr/bin/env python3
import rainmaker        #supporting functions
from config import *    #import configuration variables
import sys              #capture arguments
import pymysql
from time import sleep

def water_if_required_manual() :

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

    # Check if manual watering required
    if skip == -1:
        rainmaker.open_valve(WATERING_TIME,15)
        c.execute(f"UPDATE config set value='0' where id='skip';")
        conn.commit()
    elif skip == -2:
        rainmaker.open_valve(WATERING_TIME,21 )
        c.execute(f"UPDATE config set value='0' where id='skip';")
        conn.commit()
    else:
        rainmaker.log_and_notify(f"Manual watering not required")

    c.close()
    conn.close()

water_if_required_manual()

