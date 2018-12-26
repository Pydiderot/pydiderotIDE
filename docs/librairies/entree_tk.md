# Entree_tk
## A propos
Cette librairie fournie des fonctions d'entrées utilisateur affichant une fenêtre avec un champ de saisie texte. Le code est disponible [ici](https://github.com/cspaier/thonny/blob/diderot/Thonny/Lib/site-packages/entree_tk.py).

Nous constatons qu'un utilisateur peu expérimenté peut être surpris par l'invite d'entrée peu interactive de la console python et proposons cette librairie comme solution.

Concrètement cela peut remplacer avantageusement la fonction python `input()` dans un cadre pédagogique.

Cette librairie fournie également une fonction `demander_reel()` dont la sortie est un nombre réel de type `float`.

## utilisation
```python
# on importe la librairie
from entree_tk import *

# On demande une chaîne de caractères à l'utilisateur que l'on stocke dans la variable x
x = demander_texte()
# x est une chaîne de caractère: str

# On demande un nombre réel à l'utilisateur que l'on stocke dans la variable y
y = demander_reel()
# y est un nombre réel: float
```

## Documentation

.. automodule:: entree_tk
    :members:
    :member-order: bysource

.. eof
