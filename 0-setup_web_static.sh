#!/usr/bin/env bash
#Bash script to setup my websever for deployment on web_static

if ! [ -x "command -v nginx" ]; then
	apt-get update
	sudo apt-get install -y nginx
	sudo ufw allow 'Nginx HTTP'
	sudo service nginx start
fi

sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html

sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

if [ -L "/data/web_static/current" ]; then
	sudo rm -rf /data/web_static/current
fi
sudo mkdir -p /data/web_static/current
sudo ln -s -f /data/web_static/releasestest /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-available/default

sudo service nginx restart
