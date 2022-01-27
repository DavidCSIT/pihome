#!/usr/bin/env python3

# Importing configeration
from datetime import time
import config
import socket

# Importing supporting functions
import rainmaker

# Importing modules
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def index():

    conn = rainmaker.create_db_connection()
    c = conn.cursor() 
    c.execute("select * from config;")
    result = c.fetchall()
    config_dict = {}
    for x in result:
        config_dict.update({x[0] : x[1]})
    c.close()
    conn.close()
    
    remote_ip_address = request.remote_addr
    # host_name = request.host.split(':')[0]
    # host_ip_address = request.host.split(':')[0]
    server_network_ip_address = "10.170.180"


    remote_ip_address_array = remote_ip_address.split(".")
    server_network_ip_address_array = server_network_ip_address.split(".")

    print (remote_ip_address_array)
    print (server_network_ip_address_array)

    temp = remote_ip_address_array   
    min = server_network_ip_address_array

    # temp = config_dict["temp"]    
    # min = config_dict["mintemp"]
    humidity = config_dict["humidity"]

    if (config_dict['heating']=="T"):
        border_heating = "border-danger"
    
    if (config_dict['watering']=="T" ) :
        border_watering = "border-success"
    

    return render_template('index.html', **locals())

@app.route('/process', methods=['POST'])
def override():
    conn = rainmaker.create_db_connection()
    c = conn.cursor() 

    #update DB based on button pushed
    button = request.form.get("button")
    if (button=="Water Vegs"):
        c.execute("UPDATE config set value='-1' where id='skip';")
        c.execute("UPDATE config set value='T' where id='watering';")
    elif (button=="Water Berries"):
        c.execute("UPDATE config set value='-2' where id='skip';")
        c.execute("UPDATE config set value='T' where id='watering';")
    elif (button=="Skip One"):
        c.execute("UPDATE config set value='1' where id='skip';")
    elif (button=="Skip Two"):
        c.execute("UPDATE config set value='2' where id='skip';")  
    elif (button=="Heat 1 Hour"):
        c.execute("UPDATE config set value='1' where id='override';")  
        c.execute("UPDATE config set value='T' where id='heating';")
    elif (button=="Heat 2 Hours"):
        c.execute("UPDATE config set value='2' where id='override';")
        c.execute("UPDATE config set value='T' where id='heating';")  
    else:
        print ("button not found")

    conn.commit()
    c.close()
    conn.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')