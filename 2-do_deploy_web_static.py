#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that
distributes an archive to the web servers
"""
from os import path
from fabric.api import put, run, env, local
env.hosts = ['34.73.100.15', '184.72.175.91']


def deploy(archive_path):
    """ Function that distribute an archive to a server """
    if path.isfile(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        extension = file_n.split(".")[0]
        p = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(p, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, p, extension))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(p, extension))
        run('rm -rf {}{}/web_static'.format(p, extension))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(p, extention))
        return True
    except BaseException:
        return False
