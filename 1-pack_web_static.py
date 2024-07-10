#!/usr/bin/env python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack.
"""

from fabric.api import *
from datetime import datetime
import os


def do_pack():
    local('sudo mkdir -p versions')

    t = datetime.now()
    t_str = t.strftime("%Y%m%d%H%M%S")
    print(t_str)

    local(f'tar -cvzf versions/web_static_{t_str}.tgz web_static')
    f_size =f'versions/web_static_{t_str}.tgz'
    size = os.path.getsize(f_size)
    
    print(f'web_static packed: {f_size} -> {size}Bytes')
