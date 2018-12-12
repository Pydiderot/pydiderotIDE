# Thonny

Ce répertoire contient la version de thonny utilisée par les élèves et les professeurs du [lycée Denis Diderot](http://www.lyc-diderot.ac-aix-marseille.fr/spip/) à Marseille afin de travailler, entre autres, sur la partie algorithmique et programmation.

Le langage de programmation est python version 3.6.4 et nous utilisons la version 2.1.17 de Thonny.

La documentation (en cours de construction) est disponible [ici](https://thonny.readthedocs.io/).

thonny est un [IDE](https://fr.wikipedia.org/wiki/Environnement_de_d%C3%A9veloppement) python simple téléchargeable sur https://thonny.org/.

## Quoi de neuf?
Les modifications effectuées par l'équipe de math sont:
- [customize.py](https://github.com/cspaier/thonny/blob/diderot/Thonny/Lib/site-packages/thonny/customize.py): Le dossier de configuration est dans `%HOMESHARE%/python/.thonny`
- [configuration.ini](https://github.com/cspaier/thonny/blob/diderot/Thonny/Lib/site-packages/thonny/user_dir_template/configuration.ini): Utilisation de l'environement python du frontend.
- [running.py](https://github.com/cspaier/thonny/blob/diderot/Thonny/Lib/site-packages/thonny/running.py#L41): Le dossier de travail est `%HOMESHARE%/python/`

À ce jour, les modifications permettent de travailler sous Windows©.

Les librairies suivantes ont étés ajoutées :
- [graphique](https://github.com/cspaier/thonny/blob/diderot/Thonny/Lib/site-packages/graphique.py) : Une version modifiée de cette [librairie](https://www.pedagogie.ac-aix-marseille.fr/jcms/c_122350/fr/ressources-graphiques-pour-python). Permet l'affichage d'un repère du plan intéractif (zoom, déplacer). La documentation est dans le [wiki](https://github.com/cspaier/thonny/wiki/Graphique).
- [lycee](https://github.com/cspaier/thonny/blob/diderot/Thonny/Lib/site-packages/lycee.py) : Une version modifiée de cette [librairie](http://download.tuxfamily.org/amienspython/lycee.py). Regroupe les fonctions principales que sont amener à utiliser les élèves de lycée en mathématiques (toutes filières confondues). 
- [lycée graph](https://github.com/cspaier/thonny/blob/diderot/Thonny/Lib/site-packages/lycee_graph.py) : une tentative d'affichage graphique dynamique.

## Questions fréquentes
- **Comment télécharger et utiliser thonny?** 
Télécharger le dossier compréssé en zip avec ce [lien](https://github.com/cspaier/thonny/archive/diderot.zip). Le décomprésser et double cliquer sur le raccourci `thonny - raccourci`. Cela fonctionne sous Windows© uniquement.
- **Peut-on importer ses propres librairies avec thonny?**
 Oui! Le dossier de travail est le dossier `python` qui se trouve dans votre dossier personnel. Il suffit d'y mettre un fichier `exemple.py` pour pouvoir l'importer avec la commande `from exemple import *`

- **Et pour linux/MacOS ?** Il vous faut installer thonny par vos propre moyens en suivant le [site officiel](https://thonny.org) et ensuite rajouter les librairies du lycée dans votre dossier personel.

## Les versions
### La branche Diderot
C'est la version téléchargeable et installée sur les machines du lycée Diderot.
### La branche dév
La version en développement. N'hésitez pas à communiquer vos remarques et critiques.
