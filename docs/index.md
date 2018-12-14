# A propos
Ce site documente l'environnement de développement utilisées par les élèves et les professeurs du lycée Denis Diderot à Marseille afin de travailler, entre autres, sur la partie algorithmique et programmation. Le projet est hébergé sur ce dépot [github](https://github.com/cspaier/thonny).

# Environnement
Thonny est un environnement de développement python simple téléchargeable sur [https://thonny.org/](https://thonny.org/).

Le langage de programmation est python version 3.6.4. Nous utilisons la version 2.1.17 de Thonny avec Tk 8.6.6.


![](https://thonny.org/img/screenshot.png)


# Installation
Télécharger le dossier compréssé en zip avec ce [lien](https://github.com/cspaier/thonny/archive/diderot.zip). Le décomprésser et double cliquer sur le raccourci `thonny - raccourci`. Cela fonctionne sous Windows© uniquement.

Si vous êtes sous Linux ou MacOSX, il vous faut installer thonny par vos propre moyens en suivant le [site officiel](https://thonny.org) et ensuite rajouter les librairies du lycée dans votre dossier personel.

# Utilisation

Thonny est simple d'utilisation. Ses fonctionnalitées sont documentées, en anglais, sur son [site internet](https://thonny.org/).
Voici quelques remarques utiles.



## Affichage des variables
<div style="float: right;margin-top:-50px!important;"> ![variables](https://thonny.org/img/variables.png)</div>
Thony propose un affichage dynamique du contenu des variables qui peut être particulierement utile dans un cadre pédagogique.

Son utilisation n'est ***pas compatible avec l'import de librairies***. En effet, l'onglet affichera le contenu de toutes les fonctions et variables importées ce qui peut ralentir considérablement l'utilisation.

## Importer des Librairies
### Sous Windows©
Le dossier de travail est le dossier `python` qui se trouve dans votre dossier personnel. Il suffit d'y mettre un fichier `exemple.py` pour pouvoir l'importer avec la commande `from exemple import *`

### Sous Unix
Vous utilisez la version officielle de thonny. Le dossier de travail est donc votre dossier personnel.

# Librairies
Afin de faciliter l'apprentissage de python dans l'enseignement secondaire, nous construisons quelques librairies qui ont pour objectif de cacher certaines difficultés liées au langage de programmation afin de pouvoir cibler certains points pédagogiques.

- [graphique](librairies/graphique.md): Permet l'affichage d'un repère du plan intéractif (zoom, déplacer).
- [entree_tk](librairies/entree_tk.md): Fonctions d'entrées utilisateur avec des fenêtres tkinter. Fournie également une fonction convertissant l'entrée en nombre réel de type `float`.
- [lycee](https://github.com/cspaier/thonny/blob/diderot/Thonny/Lib/site-packages/lycee.py) : Une version modifiée de cette [librairie](http://download.tuxfamily.org/amienspython/lycee.py). Regroupe les fonctions principales que sont amener à utiliser les élèves de lycée en mathématiques (toutes filières confondues).
- [lycée graph](https://github.com/cspaier/thonny/blob/diderot/Thonny/Lib/site-packages/lycee_graph.py) : une tentative d'affichage graphique dynamique.


# Quoi de neuf?

Les modifications effectuées par l'équipe de math sont:

- [customize.py](https://github.com/cspaier/thonny/blob/diderot/Thonny/Lib/site-packages/thonny/customize.py): Le dossier de configuration est dans `%HOMESHARE%/python/.thonny`
- [configuration.ini](https://github.com/cspaier/thonny/blob/diderot/Thonny/Lib/site-packages/thonny/user_dir_template/configuration.ini): Utilisation de l'environement python du frontend.
- [running.py](https://github.com/cspaier/thonny/blob/diderot/Thonny/Lib/site-packages/thonny/running.py#L41): Le dossier de travail est `%HOMESHARE%/python/`

À ce jour, les modifications permettent de travailler sous Windows©.


# Les versions
- La branche ***Diderot***: C'est la version téléchargeable et installée sur les machines du lycée Diderot.
- La branche ***dev***: La version en développement. N'hésitez pas à communiquer vos remarques et critiques.
