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
