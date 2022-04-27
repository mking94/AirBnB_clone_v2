#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
myvar=$(dpkg -s nginx 2> /dev/null | grep Status)
if [ "$myvar" != "Status: install ok installed" ]
then
    apt-get update && apt-get install -y nginx
fi
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir /data/web_static/shared
sudo echo -e "<html>\n<head>\n<title>index</title>\n</head>\n<body>\nHolberton School\n</body>\n</html>" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
