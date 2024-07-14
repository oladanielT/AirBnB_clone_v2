#!/usr/bin/bash
"""
Bash script that sets up your web servers for the deployment of web_static
"""

sudo apt update -y
sudo apt install nginx
sudo service nginx start


sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test
sudo touch /data/web_static/releases/test/index.html
echo '<html>
<head>
</head>
<body>
    Holberton School
</body>
</html>' | sudo tee /data/web_static/releases/test/index.html

rm /data/web_static/current
ln -sfn /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

config_file="/etc/nginx/sites-available/default"
sed -i '/^}/i \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' "$config_file"
service nginx restart
exit 0
