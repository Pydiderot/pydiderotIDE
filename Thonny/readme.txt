Thonny portable version 2.1.17
Python 3.6.4
Tk 8.6.6


Au lancement, Thonny va vérifier l’existence d'un dossier ".thonny\" dans le dossier personnel de l'utilisateur.
S’il n’existe pas, il sera créé automatiquement. Ce dossier contient la configuration de Thonny pour l'utilisateur: fichiers ouverts, répertoire de travail...

Si vous voulez l'utiliser sur une clef usb et que ce dossier de configuration soit sur la clef et non dans le dossier personnel de l'utilisateur:
ouvrir "/lib/sitepackage/thonny/customize.py" et décommenter les lignes suivantes:

#user_dir = os.path.join(os.path.dirname(__file__), "..", "..", "..", ".thonny")
#os.environ["THONNY_USER_DIR"] = os.path.abspath(user_dir)

#thonny.THONNY_USER_DIR = os.path.abspath(user_dir)




Il est configuré pour utiliser l'environnement python présent dans le dossier.