# PhotoMaton
Création d'un Photomaton avec un raspberry

Installation
------------
* **Dépendances**

		sudo apt-get install gphoto2 
		sudo apt-get install libgphoto2-dev
		sudo pip3 install gphoto2		

	si vous ne disposé pas de Pip, vous le trouverez ici: <http://pypi.python.org/pypi/pip>
	
	Controle de l'APN via subprocess Gphoto: Attention RPi doit être configurer en français (raspi-config)
	
	**Fichier à suprimer pour l'utilisation de gphoto**

		sudo rm /usr/share/dbus-1/services/org.gtk.Private.GPhoto2VolumeMonitor.service
		sudo rm /usr/share/gvfs/mounts/gphoto2.mount
		sudo rm /usr/share/gvfs/remote-volume-monitors/gphoto2.monitor
		sudo rm /usr/lib/gvfs/gvfs-gphoto2-volume-monitor
		
	Redémarrer le Rpi
