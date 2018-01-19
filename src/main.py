# -*- coding: utf-8 -*-
import hashlib
import os

for path, subdirs, files in os.walk(unicode("//192.168.30.100/nohs/171226_rohs_miniPC_backup")):
    for name in files:
        file_path = os.path.join(path, name)
        print file_path
        filehash = hashlib.md5()
        filehash.update(open(file_path).read())
        print filehash.hexdigest()