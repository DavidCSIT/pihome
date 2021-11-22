#!/usr/bin/env python3
from time import sleep
from datetime import datetime
import RPi.GPIO as GPIO
import sys
import os
import config
import pymysql

def main():
   
 # Connect to the database.
    conn = pymysql.connect(db=DATABASE,
        user=USER,
        passwd=PASSWD,
        host=HOST)
    c = conn.cursor()
        
    relay = GroveRelay(5)

    while True:
        now = datetime.now()
        log_time = datetime.now().strftime("%H.%M.%S")

        c.execute(f"SELECT value from config where id='temp';")
        data = c.fetchone()
        temp = int(data[0])

        c.execute(f"SELECT value from config where id='mintemp';")
        data = c.fetchone()
        mintemp = int(data[0])

        c.execute(f"SELECT value from config where id='humidity';")
        data = c.fetchone()
        humidity = int(data[0])
 
        c.execute(f"SELECT value from config where id='override';")
        data = c.fetchone()
        override = int(data[0])  
        
        values = f"temp {temp}{DEGREE_SIGN} mintemp {mintemp}{DEGREE_SIGN} humidity {humidity}%"
       
        if (override != 0 ):
            c.execute(f"UPDATE config set value='0' where id='override';")
            c.execute(f"UPDATE config set value='T' where id='heating';")
            conn.commit()
            log(f"Manual {override} hour {values}")
            relay.on()
            sleep(override*60*60)
            relay.off()
            c.execute(f"UPDATE config set value='F' where id='heating';")
            conn.commit()
        elif (temp <= mintemp):
            relay.on()
            c.execute(f"UPDATE config set value='T' where id='heating';")
            conn.commit()
            log(f"Below min temp Heating on {values}")
            sleep(MIN_RUN_TIME)       
        else:
            c.execute(f"UPDATE config set value='F' where id='heating';")
            conn.commit()
            relay.off()
            log(f"All G temperature {values}")
            sleep(60)
   
def log(message, important=False):
       
    txt = open(f'{HOME}log.txt', "a")
    log_time = datetime.now().strftime("%H.%M.%S")
    message = f"{log_time} {message}"
    print(message)
    txt.write(f"{message} \n")
   
main()
