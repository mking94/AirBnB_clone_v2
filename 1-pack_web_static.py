#!/usr/bin/python3
""" Fabric script that generates a .tgz archive 
from the contents of the web_static """
from datetime import datetime
from fabric.api import local
from os.path import isdir ,exists


def do_pack:
    dt = datetime.utcnow()
    dt_str = "{}{}{}{}{}{}".format(dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.second)
    filepath = "versions/web_static_{}.tgz".format(dt_str)
    if isdir("versions") is False:
        local("mkdir versions")    
    local("tar -cvzf {} web_static".format(filepath))
    if exists(filepath):
        return filepath
    return None
