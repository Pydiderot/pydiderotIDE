# thonny

Ce repertoire contient la version de thonny utilisée par le [lycée Denis Diderot](http://www.lyc-diderot.ac-aix-marseille.fr/spip/) à Marseille.

thonny est un [IDE](https://fr.wikipedia.org/wiki/Environnement_de_d%C3%A9veloppement) python simple téléchargeable sur https://thonny.org/.

## Quoi de neuf?
Les modifications effectuées par l'équipe de math sont:
- customize.py: Le dossier de configuration est dans `%HOMESHARE%/python/.thonny`
- configuration: Utilisation de l'environement python du frontend.
- running.py: Le dossier de travail est `%HOMESHARE%/python/`


Les librairies suivantes ont étés ajoutées:
- graphique:
- lycee:
- lycée graph:

## Questions fréquentes

- Peut-on importer ses propres librairies avec thonny?
Oui! Le dossier de travail est le dossier `python` qui se trouve dans votre dossier personnel. Il suffit d'y mettre un fichier `exemple.py` pour pouvoir l'importer avec la commande `from exemple import *`
