#!/usr/bin/python3
"""
creates and distributes an archive to web servers
"""
from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['52.205.90.195', '54.197.207.11']


def do_pack():
    """generate tgz file"""
    now = datetime.now()
    archive = 'web_static_' + now.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'

    local('mkdir -p versions')
    result = local('tar -cvzf versions/{} web_static'.format(archive))

    if result is not None:
        return archive
    else:
        return None


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except Exception as e:
        return False


def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
