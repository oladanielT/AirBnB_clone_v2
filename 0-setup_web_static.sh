#!/usr/bin/env bash
#Bash script to setup my websever for deployment on web_static

if ! [ -x "command -v nginx" ]; then
	apt-get update
	sudo apt-get install -y nginx
	sudo ufw allow 'Nginx HTTP'
fi

mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

if [ -L "/data/web_static/current" ]; then
	rm /data/web_static/current
fi
mkdir -p /data/web_static/current
sudo ln -s -f /data/web_static/release/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sed -i '/listen 80 default_server/a location /hbnb_static {alias /data/web_static/current/;}' /etc/nginx/sites-available/default

sudo service nginx restart
