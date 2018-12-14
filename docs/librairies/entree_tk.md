## A propos
Cette librairie fournie des fonctions d'entrées utilisateur affichant une fenêtre avec un champ de saisie texte. Le code est disponible [ici](https://github.com/cspaier/thonny/blob/diderot/Thonny/Lib/site-packages/entree_tk.py).

Nous constatons qu'un utilisateur peu expérimenté peut être surpris par l'invite d'entrée peu interactive de la console python et proposons cette librairie comme solution.

Concrètement cela peut remplacer avantageusement la fonction python `input()` dans un cadre pédagogique.

Cette librairie fournie également une fonction `demander_reel()` dont la sortie est un nombre réel de type `float`.

## utilisation
```py
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
### demander_texte
```demander_texte(titre="Entrez un texte", message=None)```

Ouvre une fenêtre tkinter avec le titre "titre" et attend une chaîne de caractères de la part de l'utilisateur.
La sortie est la chaîne de caractères (type `str`) entrée par l'utilisateur.

Parametres:

- `titre` (optionel): Une chaîne de caractères représentant le titre de la fenêtre. La valeur par défaut est "Entrez un texte".
- `message` (optionel): Une chaine de caractères. Si présente, la fenêtre aura un champ de texte contenant ce message. La valeur par défaut est `None`.

### demander_reel
```demander_texte(titre="Entrez un nombre réel")```

Ouvre une fenêtre tkinter avec le titre "titre" et attend un nombre réel de la part de l'utilisateur.
La sortie est le nombre réel (type `float`) entré par l'utilisateur.

Si l'utilisateur n'entre pas un nombre réel, il sera invité de nouveau à rentrer une valeur avec un message d'erreur "La donnée est incorrecte".

Parametres:

- `titre` (optionel): Une chaîne de caractères représentant le titre de la fenêtre. La valeur par défaut est "Entrez un nombre réel".
