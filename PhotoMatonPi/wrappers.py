# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright: Fabien Rosso

#Version 0.1 - 15.08.2017



from __future__ import unicode_literals
from __future__ import print_function


import re
import os
import shutil
import pickle
import subprocess
import time 


class Wrapper(object):

    def __init__(self, subprocess):
        self._subprocess = subprocess

    def call(self, cmd):
        p = self._subprocess.Popen(cmd, shell=True,
                                   stdout=self._subprocess.PIPE,
                                   stderr=self._subprocess.PIPE)
        out, err = p.communicate()
        return p.returncode, out.rstrip(), err.rstrip()


class GPhoto(Wrapper):
    """ A class which wraps calls to the external gphoto2 process. """

    def __init__(self, subprocess):
        Wrapper.__init__(self, subprocess)
        self._CMD = 'gphoto2'
        self._shutter_choices = None
        self._iso_choices = None

    def capture_image_and_download(self):
        code, out, err = self.call(self._CMD + " --capture-image-and-download")
        if code != 0:
            raise Exception(err)
        filename = None
        for line in out.split(b'\n'):
            if line.startswith(b'Enregistrement du fichier en '):
                filename = line.split(b'Enregistrement du fichier en ')[1]
        return filename


class Photo():
    """Class definissant une photo caracterisee par:
    - Chemin (self.pathFile)
    - son nom (self.namefile)
    - son extension (self.extFile)
    - son dossier parent (self.parenPathFile)
    Fonction:
    - recupere la date de prise de vue (self.tag_date_time())
    - Deplace/renome le fichier dans un nouveau repertoire
      (self.move(newPath)) """

    def __init__(self, path):
        self.pathFile = path
        self.nameFile = os.path.split(self.pathFile)[1]
        self.extFile = os.path.splitext(self.pathFile)[1]
        self.parenPathFile = os.path.split(self.pathFile)[0]
        self.createDate = time.gmtime(os.path.getatime(self.pathFile))

    #def tag_date_time(self):
    #    """ Recupere la date de prise de vue dans les exif avec la lib exifread
    #    N'est plus utilise dans la V0.1.1.1"""
    #    # Lecture des Exif
    #    with open(self.pathFile, "rb") as f:
    #        tags = exifread.process_file(f)
    #    # Recupere la date de prise de vue
    #    try:
    #        tagsDateTime = tags['Image DateTime'].values
    #    except Exception, e:
    #        print("Erreur: ") + str(e)
    #    return tagsDateTime

    def move(self, newPath):
        """Deplace/Renome la photo dans un repertoire newPath"""
        shutil.move(self.pathFile, newPath)
        file = Photo(newPath)
        return file
