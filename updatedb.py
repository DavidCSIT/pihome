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

c.execute("UPDATE config set value = -2 WHERE ID = 'skip'")

conn.commit()

c.close()
conn.close()
