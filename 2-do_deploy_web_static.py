#!/usr/bin/python3
"""script that distributes an archive to web servers"""
from fabric.api import put, run, env
from os.path import exists
env.hosts = ['52.205.90.195', '54.197.207.11']


def do_deploy(archive_path):
    """distributes an archive to web servers
    Attributes:
        archive_path: path attribute
    """
    if exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        ext = file_name.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, ext))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, ext))
        run('rm -rf {}{}/web_static'.format(path, ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, ext))
        return True
    except:
        return False
