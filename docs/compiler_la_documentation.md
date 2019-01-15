# Compiler la documentation

## Comment ca marche?
La documentation de ce projet est construire avec [Sphinx](https://www.sphinx-doc.org/) à partir du dossier [doc](https://github.com/cspaier/pydiderot/tree/dev/docs) du dépot github. [Readthedocs](https://readthedocs.org/) compile automatiquement cela en [html](https://readthedocs.org/projects/pydiderot/downloads/htmlzip/latest/), [pdf](https://readthedocs.org/projects/pydiderot/downloads/pdf/latest/), et [epub](https://readthedocs.org/projects/pydiderot/downloads/epub/latest/) à chaque modification  et héberge le html sur https://pydiderot.readthedocs.io/.


## Je veux tester en local!

C'est bien normal. Lorsque l'on travail le format et la mise en page d'un document (html ou latex), il peut être frustrant d'attendre entre une et dix minutes que readthedocs compile notre code. De plus, comme toute compilation, si les sources ne respectent pas le format attendu, on peut facilement rencontrer des erreurs.

Ce qui suit explique comment compiler la documentation sur votre ordinateur personnel. Si vous êtes familiers avec la console unix, cela ne devrait pas poser de problème technique.


### 1. Installer Sphinx et m2r
Vous allez avoir besoin d'installer sphinx dans votre environnement python.

Il est conseillé de créer un environnement python dédié à cela: `python3 -m venv venv`
Vous pouvez ensuite activer l’environnement avec `source venv/bin/activate` et le désactiver avec `deactivate`. Activons le.

Installez ensuite [Sphinx](https://www.sphinx-doc.org/), le [theme readthedocs](https://sphinx-rtd-theme.readthedocs.io/) et l'extension [m2r](https://github.com/miyakogi/m2r) qui nous permet d'écrire en markdown: `pip install sphinx sphinx_rtd_theme m2r`


### 2. Cloner le dépôt
Il faut commencer par cloner le dépôt ou votre fork:

- si vous êtes un collaborateur et avez les droits d'écriture sur notre dépot: `git clone https://github.com/cspaier/pydiderot.git`
- sinon clonez votre fork: `git clone https://github.com/VOTRENOMDUTILISATEURGITHUB/pydiderot.git`

Le téléchargement peut être long car le projet est un peu lourd.

Placez vous ensuite dans le dossier `pydiderot/thonny/docs/` créé. Touts les chemins suivants seront relatifs à ce dossier.


### 3. Compilez

#### En HTML
Il suffit d'invoquer la commande `make html`.
Le résultat est disponible dans le dossier `_build/html/`. Le fichier `index.html` est le document racine.

#### En pdf grâce à latex
  1. générer les fichiers latex: `make latex`
  2. générer les pdf: `make latexpdf`

Le résultat est disponible dans le dossier `_build/html/index.html`. Le fichier principal est `pydiderot.pdf`.

### 4. Configuration
Le fichier de configuration est `conf.py`.
On y trouve en particulier une partie `# -- Options for LaTeX output --` qui permet de configurer le rendu latex. Il peut être bon de parcourir la documentation [latex de sphinx](https://www.sphinx-doc.org/en/master/latex.html) et en particulier ce qui concerne [latex_elements](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-latex_elements).
