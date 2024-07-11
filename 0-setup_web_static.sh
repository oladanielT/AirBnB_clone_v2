#!/usr/bin/bash
"""
Bash script that sets up your web servers for the deployment of web_static
"""

sudo apt update -y
sudo apt install nginx
sudo service nginx restart


sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/{releases,test}
sudo touch /data/web_static/releases/test/index.html
echo '<html lang="en">
<head>
</head>
<body>
    Holberton School
</body>
</html>' | sudo tee /data/web_static/releases/test/index.html >/dev/null
sudo ln -sfn /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

config_block="location /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}"
sudo sed -i "/server_name _;/a $config_block" /etc/nginx/sites-available/default
sudo service nginx restart
