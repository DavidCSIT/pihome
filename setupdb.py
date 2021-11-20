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

# Drop tables if requried
c.execute("DROP TABLE IF EXISTS MoistureReading;")
c.execute("DROP TABLE IF EXISTS Forecast")
c.execute("DROP TABLE IF EXISTS config")

# Create tables
c.execute(
    "CREATE TABLE MoistureReading (RecordingID int, RecordID int, DateRecorded datetime, AnalogMoisture int, SoilMoisture int, Humidity int);"
)
c.execute(
    "CREATE TABLE Forecast (ForecastID int, RecordID int, DateRecorded datetime, rain float);"
)

c.execute("CREATE TABLE config (id varchar(20), value varchar(20) )")
c.execute("ALTER TABLE `pihome`.`config` ADD UNIQUE `ID_Index` (`id`);")
c.execute("INSERT INTO config VALUES ('skip', 0)")
c.execute("INSERT INTO config VALUES ('version', 1)")
c.execute("INSERT INTO config VALUES ('override', 1)")
c.execute("INSERT INTO config VALUES ('temp', 20)")
c.execute("INSERT INTO config VALUES ('humidity', 1)")
c.execute("INSERT INTO config VALUES ('mintemp', 10)")
c.execute("INSERT INTO config VALUES ('heating', 'F')")
c.execute("INSERT INTO config VALUES ('watering', 'F')")

conn.commit()