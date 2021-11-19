#!/usr/bin/env python3
from config import *
from time import sleep
import seeed_dht
import seeed_dht
from datetime import datetime
from grove.gpio import GPIO
import pymysql
from groverelay import GroveRelay

def main():
    sensor = seeed_dht.DHT("11", 12)
    relay = GroveRelay(5)
   
 # Connect to the database.
    conn = pymysql.connect(db=DATABASE,
        user=USER,
        passwd=PASSWD,
        host=HOST)
    c = conn.cursor()
   
    while True:
        sleep(60)
        now = datetime.now()
        humidity, temp = sensor.read()

        c.execute(f"SELECT value from config where id='override';")
        data = c.fetchone()
        override = data[0]
      
        if (now.hour >= MORNING_START_TIME and now.hour < MORNING_END_TIME):
            mintemp = MORNING_TARGET_TEMP
        elif (now.hour >= EVENING_START_TIME and now.hour < EVENING_END_TIME):
            mintemp = EVENING_TARGET_TEMP
        else:
            mintemp = MIN_TEMP
        
        c.execute(f"UPDATE config set value='{mintemp}' where id='mintemp';")
        c.execute(f"UPDATE config set value='{temp}' where id='temp';")
        c.execute(f"UPDATE config set value='{humidity}' where id='humidity';")
        conn.commit()
        print(f"temp {temp}{DEGREE_SIGN} mintemp {mintemp}{DEGREE_SIGN} humidity {humidity}%" )
   
main()
