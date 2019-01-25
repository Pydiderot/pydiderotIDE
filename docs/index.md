# Python à Diderot
## A propos
Ce site documente l'environnement de développement utilisées par les élèves et les professeurs du lycée Denis Diderot à Marseille afin de travailler, entre autres, sur la partie algorithmique et programmation. Le projet est hébergé sur ce dépôt [github](https://github.com/cspaier/thonny).

## Environnement
Nous l'utilisons l'environnement de développement python  [Thonny](https://thonny.org/) (version 3.0.8) disponible sous licence MIT.

Le langage de programmation est python version 3.7.1rc1 avec Tk 8.6.8.


![](https://thonny.org/img/screenshot.png)


## Installation
Télécharger le dossier compressé en zip avec ce [lien](https://github.com/cspaier/thonny/archive/diderot.zip). Le décompresser et double cliquer sur le raccourci `thonny - raccourci`. Cela fonctionne sous Windows© uniquement.

Si vous êtes sous Linux ou MacOSX, il vous faut installer thonny par vos propre moyens en suivant le [site officiel](https://thonny.org). Vous pouvez ensuite télécharger les librairies du lycée [ici](_static/diderot.zip) et les rajouter dans votre dossier personnel.


## Utilisation

Thonny est simple d'utilisation. Ses fonctionnalités sont documentées, en anglais, sur son [site internet](https://thonny.org/).
Voici quelques remarques utiles.



### Affichage des variables
.. image:: https://thonny.org/img/variables.png
  :align: right

Thony propose un affichage dynamique du contenu des variables qui peut être particulièrement utile dans un cadre pédagogique.

Son utilisation n'est **pas compatible avec l'import de librairies**. En effet, l'onglet affichera le contenu de toutes les fonctions et variables importées ce qui peut ralentir considérablement l'utilisation.

### Importer des Librairies
* **Sous Windows©**: Le dossier de travail est le dossier `python` qui se trouve dans votre dossier personnel. Il suffit d'y mettre un fichier `exemple.py` pour pouvoir l'importer avec la commande `from exemple import *`

* **Sous Unix**: Vous utilisez la version officielle de thonny. Le dossier de travail est donc votre dossier personnel.

## Librairies
Afin de faciliter l'apprentissage de python dans l'enseignement secondaire, nous construisons quelques librairies qui ont pour objectif de cacher certaines difficultés liées au langage de programmation afin de pouvoir cibler certains points pédagogiques. Vous pouvez télécharger nos librairies zippées [ici](_static/diderot.zip).

- [repere](/librairies/graphique/): Permet l'affichage d'un repère du plan interactif (zoom, déplacer).
- [entree](/librairies/entree/): Fonctions d'entrées utilisateur avec des fenêtres tkinter.
- [lycee](/libraries/lycee/) : Regroupe les fonctions principales que sont amenés à utiliser les élèves de lycée en mathématiques (toutes filières confondues).
- [graphique](/librairies/graphique): Permet l'affichage d'une fenêtre graphique dynamique et une gestion simplifiée des entrées clavier et souris.


## Quoi de neuf?

Les modifications effectuées par l'équipe de math sont:

- Ajout de la librairies [pygame 1.9.4](https://www.pygame.org/).

- [customize.py](https://github.com/cspaier/thonny/blob/diderot/Thonny/Lib/site-packages/thonny/customize.py): Le dossier de configuration est dans `%HOMESHARE%/python/.thonny`
- [configuration.ini](https://github.com/cspaier/thonny/blob/diderot/Thonny/Lib/site-packages/thonny/user_dir_template/configuration.ini): Utilisation de l'environnement python du frontend.
- [workbench.py](https://github.com/cspaier/thonny/blob/f1c57d3062d60841dea3bdf7e2af93243cd742c9/Thonny/Lib/site-packages/thonny/workbench.py#L205-L208): Le dossier de travail est `%HOMESHARE%/python/`

À ce jour, les modifications permettent de travailler sous Windows©.


## Les versions
- La branche **Diderot**: C'est la version téléchargeable et installée sur les machines du lycée Diderot.
- La branche **dev**: La version en développement. N'hésitez pas à communiquer vos remarques et critiques.
- La branche **thonny-2.17.0** contient la version 2.17.0 de thonny utilisée au lycée jusqu'à janvier 2019.

## Participez!
Ce projet est un travail collaboratif initié par des enseignants du lycée Diderot à Marseille. Nous serions ravis de travailler avec vous et toute aide est la bienvenue. Si vous souhaitez participer, lisez notre [fichier contributing](https://github.com/cspaier/pydiderot/blob/dev/CONTRIBUTING.md).
