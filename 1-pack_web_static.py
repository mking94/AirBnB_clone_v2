#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the contents of the web_static """
import os.path
from datetime import datetime
from fabric.api import local

def do_pack:
    local("mkdir -p versions");
    dt = datetime.utcnow()
    filepath = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if local("tar -cvzf {} web_static".format(filepath)).failed is True:
        return None
    return filepath
