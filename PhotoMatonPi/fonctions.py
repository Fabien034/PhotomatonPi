# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright: Fabien Rosso

from __future__ import unicode_literals
from __future__ import print_function

import os

def ListDirectory(path):
    ''' Fonction listdirectory(path)
    Fait une liste de tous les fichiers dans le repertoire 'path'
    et des sous repertoires
    '''
    fichier=[]
    for root, dirs, files in os.walk(path):
        for i in files:
            fichier.append(os.path.join(root, i))
    return fichier
