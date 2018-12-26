# Participer à ce projet

L'objectif de ce projet est de construire un environement de développement adapté à l'enseignement du language python dans l'enseignement secondaire.

C'est un travail collaboratif sous licence MIT initié par des enseignants du lycée Denis Diderot à Marseille.

Toute participation est la bienvenue tant sur le code que le coté pédagogique : remarques, retours de tests, codes, documentation...

Si vous considérez participer nous vous en remercions et fournissons ce guide pour vous aider.

## J'ai un problème, une idée, une remarque
Nous utilisons les issues github pour gérer cela. Vérifiez si votre cas est déja présent dans la liste d'issues et n'hésitez pas à en ouvrir si besoin.


## J'ai codé un truc, fixé un bug
Nous acceptons les Pull requests dans la branche `dev`.

Merci de commenter le code python en utilisant la [convention google](http://google.github.io/styleguide/pyguide.html):
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
Nous utilisons [sphinx](http://www.sphinx-doc.org/en/master/) et l'extension [napoleon](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/) pour construire la documentation à partir de ces docstrings.
