#!/usr/bin/env python3

import config

# Connect to the database.
import pymysql
conn = pymysql.connect(
    db='pihome',    
    user=config.USER,
    passwd=config.PASSWD,
    host='localhost')
c = conn.cursor()

#c.execute(f"SELECT rain FROM Forecast WHERE ForecastID = (SELECT MAX(ForecastID) from Forecast);")
#forecasts = [item[0] for item in c.fetchall()]
#print(forecasts)
c.execute("UPDATE config set value = -2 WHERE ID = 'skip'")
#c.execute("UPDATE config set value = 'F' WHERE ID = 'watering'")
#c.execute("UPDATE config set value = 'F' WHERE ID = 'heating'")
#c.execute("INSERT INTO config VALUES ('watering', 'F')")
#c.execute("INSERT INTO config VALUES ('heating', 'F')")

conn.commit()

c.close()
conn.close()
