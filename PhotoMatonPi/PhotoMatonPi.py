# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright: Fabien Rosso

from __future__ import unicode_literals
from __future__ import print_function


# Debug VisualStudio
#import ptvsd
#ptvsd.enable_attach('my_secret')
# Activez la ligne de code ci-dessous uniquement si vous souhaitez que l'application attende jusqu'à ce que le débogueur l'ait attaché 
# ptvsd.wait_for_attach()

import os
import subprocess
import pickle

from datetime import datetime
import time
from time import sleep

from wrappers import *
from fonctions import *


def main():
    # Création du dossier attente de traitement
    WAITPATH = os.path.join(os.path.expanduser("~"), "Pictures", "Attente")
    if not os.path.exists(WAITPATH):
        os.makedirs(WAITPATH, mode=0o777)
    # inscription class
    camera = GPhoto(subprocess)    
    fileName = camera.capture_image_and_download()
    # inscription de la class Photo
    file = Photo(os.path.join(os.path.expanduser("~"),"PhotoMatonPi", fileName))
    timeLapsStart = False
    # Creation du nouveau nom
    newPathFile = os.path.join(WAITPATH,str('{0}{1}'.format(datetimeShot.strftime("%y%m%d-%H%M%S"),file.extFile)))
    # Deplace/rennome la photo
    file = file.move(newPathFile)


if __name__ == "__main__":
    main()