#!/usr/bin/python3
""" Fabric script that generates a .tgz archive
from the contents of the web_static """

from datetime import datetime
from fabric.api import local


def do_pack():
    """Function to compress files"""
    local("mkdir -p versions")
    file = local("tar -cvzf versions/web_static_{}.tgz web_static"
                 .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")),
                 capture=True)
    if result.failed:
        return None
    return file
