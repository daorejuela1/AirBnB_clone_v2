#!/usr/bin/python3
"""
Fab module to create a targ file of all my static files
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    function to pack in .tgz
    """
    local("mkdir versions")
    now = datetime.today()
    file_name = "web_static_{}{}{}{}{}{}".format(now.year, now.month,
                                                 now.day, now.hour,
                                                 now.minute, now.second)
    local("tar -cvzf versions/{}.tgz web_static".format(file_name))
