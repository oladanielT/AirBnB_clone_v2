#!/usr/bin/bash
"""
Bash script that sets up your web servers for the deployment of web_static
"""

sudo apt update -y
sudo apt install nginx
sudo service nginx restart


sudo mkdir /data
sudo mkdir /data/web_static
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html

ln -s -f /data/web_static/current /data/web_static/releases/test/

sudo chown ubuntu:ubuntu 
