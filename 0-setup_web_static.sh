#!/usr/bin/env bash
#this script configures nginx in a new server
sudo apt-get -y update
sudo apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/releases/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
add_location="location /hbnb_static/ {
    alias /data/web_static/current/;
    autoindex off;
}"
sed -i "/server_name localhost;/a ${add_location}"
sudo service nginx restart
