#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from
the contents of the web_static folder of your AirBnB
Clone repo, using the function do_pack.
"""
from fabric.api import *
from datetime import datetime
import os

def do_pack():
    local('sudo mkdir -p versions')

    now = datetime.now()
    t_str = now.strftime("%Y%m%d%H%M%S")

    create = local(f'tar -cvzf versions/web_static_{t_str}.tgz web_static')
    s = f'versions/web_static_{t_str}.tgz'
    size_b = os.path.getsize(s)
    if create is not None:
        print(f'web_static packed: {s} -> {size_b}Bytes')
        return create
    else:
        return None
