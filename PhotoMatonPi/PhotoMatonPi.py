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
    capture_image()


if __name__ == "__main__":
    main()