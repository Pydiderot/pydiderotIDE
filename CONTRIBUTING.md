# Participer à ce projet

L'objectif de ce projet est de construire un environnement de développement adapté à l'enseignement du langage python dans l'enseignement secondaire.

C'est un travail collaboratif sous licence MIT initié par des enseignants du lycée Denis Diderot à Marseille.

Toute participation est la bienvenue tant sur le code que le coté pédagogique : remarques, retours de tests, codes, documentation...

Si vous considérez participer nous vous en remercions et fournissons ce guide pour vous aider.

## J'ai un problème, une idée, une remarque
Nous utilisons les issues github pour gérer cela. Vérifiez si votre cas est déjà présent dans la liste d'issues et n'hésitez pas à en ouvrir si besoin.


## J'ai codé un truc, fixé un bug
Nous acceptons les Pull requests dans la branche `dev`.

Merci de commenter le code python en utilisant la [convention google](http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings):
```python
def trace_texte(x, y, texte, couleur='black'):
    """Trace un texte dans la fenêtre graphique au coordonées `x, y`.

    Arguments:
        x (float): abscisse du point
        y (float): ordonnée du point
        texte (str): Texte à placer dans la fenêtre graphique
        couleur (str, optionel): Couleur du texte ('black' par défaut)

    """
```
Nous utilisons [sphinx](http://www.sphinx-doc.org/) et l'extension [napoleon](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/) pour construire la documentation à partir de ces doc-strings.

## Je veux aider à documenter
La documentation de ce projet est construire avec [Sphinx](https://www.sphinx-doc.org/) à partir du dossier [doc](https://github.com/cspaier/pydiderot/tree/dev/docs) du dépôt github. N'hésitez pas à proposer des ajouts ou corrections!

Si vous souhaitez tester la documentation sur votre ordinateur, jetez un œil à [ce document](https://pydiderot.readthedocs.io/compiler_la_documentation/).
