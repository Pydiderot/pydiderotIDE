# Graphique

## A propos

:download:`graphique.py </../Thonny/Lib/site-packages/graphique.py>`

Cette librairie permet l'affichage d'une fenêtre graphique dynamique et fournie des fonctions permettant d'y afficher des objets géométriques simples (point, cercle, segment, vecteur, rectangle).

Basée sur pygame, vous pouvez également récupérer les événements clavier ou souris pour interagir avec l'utilisateur.

Vous pouvez, par exemple, l'utiliser pour construire un jeux de type pong.


## Utilisation

Voici un exemple qui affiche une fenêtre graphique traversée en diagonale par un point.

```python
# On importe la librairie
from graphique import *
# Nous aurons également de la librairie time
import time

# On initialise les coordonnées du point au coin haut gauche de la fenêtre
x = 0
y = 0
# On initialise les coordonnées du vecteur vitesse
v_x = 1
v_y = 1

# On créé la fenêtre graphique
creer_fenetre()

# Boucle principale
while 1:
    # Il est important d’appeler  la fonction evenements() qui gère la fermeture de la fenêtre
    evenements()

    # Trace un cercle au coordonnées (x,y)
    trace_cercle(x, y)
    # Attend un dixième de secondes
    time.sleep(0.1)
    # Efface le cercle
    trace_cercle(x, y, couleur=blanc)
    # Ajoute le vecteur vitesse aux coordonnées du point
    x += v_x
    y += v_y
```


## Documentation

.. automodule:: graphique
    :members:
    :member-order: bysource

.. eof
