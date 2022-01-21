#!/usr/bin/env python3

# Importing configeration
from datetime import time
import config

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

    temp = config_dict["temp"]
    min = config_dict["mintemp"]
    humidity = config_dict["humidity"]

    if (config_dict['heating']=="T"):
        border_heating = "border-danger"
    
    if (config_dict['watering']=="T" or config_dict['skip']=="-1" or config_dict['skip']=="-2") :
        border_watering = "border-success"

    return render_template('index.html', **locals())

@app.route('/process', methods=['POST'])
def override():

    #update DB based on button pushed

    button = request.form.get("button")
    if (button=="Water Vegs"):
        sql = "UPDATE config set value='-1' where id='skip';"
    else:
        sql = "UPDATE config set value='F' where id='watering';"

    # if (!empty($_POST["waterVegs"]))
    #     $sql = "UPDATE config set value='-1' where id='skip'";
    # elseif (!empty($_POST["waterBerries"]))
    #     $sql = "UPDATE config set value='-2' where id='skip'";
    # elseif (!empty($_POST["skip1"]))
    #     $sql = "UPDATE config set value='1' where id='skip'";
    # elseif (!empty($_POST["skip2"]))
    #     $sql = "UPDATE config set value='2' where id='skip'";
    # elseif (!empty($_POST["heat1"]))
    #     $sql = "UPDATE config set value='1' where id='override'";
    # elseif (!empty($_POST["heat2"]))
    #     $sql = "UPDATE config set value='2' where id='override'";
    # else {
    #     print("what?");
    #     exit();
    # }
    
    conn = rainmaker.create_db_connection()
    c = conn.cursor() 
    c.execute(sql)
    conn.commit()
    c.close()
    conn.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')