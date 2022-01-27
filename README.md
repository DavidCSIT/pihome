Auto Update Raspberry Pi

nano update.sh
    #!/bin/sh
    sudo apt-get update && sudo apt-get upgrade -y
    sudo rpi-update -y
    sudo apt-get autoremove -y
    sudo apt-get autoclean -y
    sudo reboot

Adjust Permission to Allow Execution
    chmod +x update.sh

Create a Log Directory
mkdir logs
touch ./logs/cronlog

crontab -e
    0 0 * * SAT sh /home/pi/update.sh 2>/home/pi/logs/cronlog   

sudo apt-get install mariadb-server msmtp msmtp-mta -y
sudo mysql_secure_installation

sudo mariadb
    create database pihome;
    create user pihome@localhost identified by 'SecurePasswordOfYourChoice'; 
    grant all on pihome.* to pihome@localhost;

sudo pip3 install selenium beautifulsoup4 pymysql GPIO

sudo apt install apache2 -y
sudo apt install php libapache2-mod-php php-mysql -y
sudo systemctl enable apache2.service  

setup ssh

sudo rm -rf /var/www/html/*

sudo usermod -a -G gpio pi
sudo usermod -a -G gpio www-data
sudo usermod -a -G www-data pi
sudo usermod 773 /var/www/html

logoff logon

cd /var/www/html/*

git clone git@github.com:DavidCSIT/pihome.git .

update config

setupdb.py

sudo systemctl restart apache2

sudo cp ~/pihome/public/*  /var/www/html
sudo chown www-data:www-data /var/www/html 
sudo usermod -a -G gpio pi

To host on Apache from improved security 
adapted from https://www.codementor.io/@abhishake/minimal-apache-configuration-for-deploying-a-flask-app-ubuntu-18-04-phu50a7ft

sudo apt install apache2 libapache2-mod-wsgi-py3 python-dev -y

update webapp.wsgi
    sys.path.insert(0, '/home/pi/pihome') change to your path
    application.secret_key = 'pihome'  change to a secure key of your choice

create the Apache config file for our flask application

cd /etc/apache2/sites-available

sudo nano pihome.conf

<VirtualHost *:80>
     # Add machine's IP address (use ifconfig command)
     ServerName 10.170.180.104
     # Give an alias to to start your website url with
     WSGIScriptAlias / /home/pi/pihome/webapp.wsgi
     <Directory /home/pi/pihome/>
     		# set permissions as per apache2.conf file
            Options FollowSymLinks
            AllowOverride None
            Require all granted
     </Directory>
     ErrorLog ${APACHE_LOG_DIR}/error.log
     LogLevel warn
     CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

sudo a2ensite pihome.conf
sudo systemctl reload apache2

