# Thonny

Ce repertoire contient la version de thonny utilisée par le [lycée Denis Diderot](http://www.lyc-diderot.ac-aix-marseille.fr/spip/) à Marseille.

thonny est un [IDE](https://fr.wikipedia.org/wiki/Environnement_de_d%C3%A9veloppement) python simple téléchargeable sur https://thonny.org/.

## Quoi de neuf?
Les modifications effectuées par l'équipe de math sont:
- [customize.py](https://github.com/cspaier/thonny/blob/diderot/Thonny/Lib/site-packages/thonny/customize.py): Le dossier de configuration est dans `%HOMESHARE%/python/.thonny`
- [configuration.ini](https://github.com/cspaier/thonny/blob/diderot/Thonny/Lib/site-packages/thonny/user_dir_template/configuration.ini): Utilisation de l'environement python du frontend.
- [running.py](https://github.com/cspaier/thonny/blob/diderot/Thonny/Lib/site-packages/thonny/running.py): Le dossier de travail est `%HOMESHARE%/python/`


Les librairies suivantes ont étés ajoutées:
- [graphique](https://github.com/cspaier/thonny/blob/diderot/Thonny/Lib/site-packages/graphique.py):Une version modifiée de cette [librairie](https://www.pedagogie.ac-aix-marseille.fr/jcms/c_122350/fr/ressources-graphiques-pour-python). Permet l'affichage d'un repère du plan intéractif (zoom, déplacer).
- [lycee](https://github.com/cspaier/thonny/blob/diderot/Thonny/Lib/site-packages/lycee.py):
- [lycée graph](https://github.com/cspaier/thonny/blob/diderot/Thonny/Lib/site-packages/lycee_graph.py):

## Questions fréquentes
- **Comment télécharger et utiliser thonny?** 
Télécharger le dossier compréssé en zip avec ce [lien](https://github.com/cspaier/thonny/archive/diderot.zip). Le décomprésser et double cliquer sur le raccourci `thonny - raccourci`.
- **Peut-on importer ses propres librairies avec thonny?**
 Oui! Le dossier de travail est le dossier `python` qui se trouve dans votre dossier personnel. Il suffit d'y mettre un fichier `exemple.py` pour pouvoir l'importer avec la commande `from exemple import *`
