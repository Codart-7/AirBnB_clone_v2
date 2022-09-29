#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

# install nginx web server 
sudo apt-get update
sudo apt-get install -y nginx

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

sudo chown -R ubuntu:ubuntu /data/

echo -e "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" > /data/web_static/releases/test/index.html


# Create symlink, override if already exists
ln -sfn /data/web_static/releases/test /data/web_static/current

if grep -q hbnb_static /etc/nginx/sites-available/default
then
    echo ""
else
    sudo sed -i '/:80 default_server/a \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
fi

sudo service nginx restart
