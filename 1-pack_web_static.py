#!/usr/bin/python3
"""
generates a .tgz archive from the contents of the web_static folder
Usage:
    fab -f 1-pack_web_static.py do_pack
"""

from fabric.api import *
from os import path
from datetime import datetime
from shlex import split

env.user = 'ubuntu'
env.hosts = ['3.233.232.127', '44.200.43.251']


def do_pack():
    """Packing a dir in .tgz"""
    d_now = datetime.now()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        d_now.year,
        d_now.month,
        d_now.day,
        d_now.hour,
        d_now.minute,
        d_now.second
    )

    print("Packing web_static to {}".format(output))

    if not path.exists('versions') or (
                                       path.exists('versions') and
                                       not path.isdir('versions')):
        local('mkdir -p versions')

    cmd_tar = 'tar -cvzf '
    p_name = 'versions/web_static_'
    p_name += '{:4}{:02}{:02}'.format(d_now.year, d_now.month, d_now.day)
    p_name += '{:02}{:02}{:02}'.format(d_now.hour, d_now.minute, d_now.second)
    p_name += '.tgz'
    cmd_tar += p_name
    cmd_tar += ' web_static'
    try:
        local(cmd_tar)
        return p_name
    except:
        return None
