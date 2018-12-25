# Graphique
## A propos
Cette [bibliothèque](https://github.com/cspaier/thonny/blob/diderot/Thonny/Lib/site-packages/graphique.py) facilite l'affichage d'une fenêtre munie d'un repère interactif (zoom, déplacement). Des fonctions sont disponibles pour tracer des objets géométriques simples.

C'est une Version légèrement modifiée de [cette librairie](https://www.pedagogie.ac-aix-marseille.fr/jcms/c_122350/fr/ressources-graphiques-pour-python) écrite par Olivier Brebant en 2011 et publié par l'académie d'Aix-Marseille en 2012, sous licence MIT depuis novembre 2018.


## A quoi ca sert?
A tracer un graphique **non dynamique** muni (ou non) d'un repère.
On peut par exemple construire facilement un [traceur de courbes](https://gist.github.com/cspaier/3c67ddb66218ee53e7deaef6a61aeb8a).

Par non dynamique, j’entends qu'on ne peut pas facilement utiliser cette librairie pour interagir directement avec les objets. Par exemple cette librairie n'est pas adaptée au codage d'un jeu de type pong ou même d'un objet en mouvement.


## Comment l'utiliser

```python
# On importe la librairie
from graphique import *

# On initialise la fenetre
creer_fenetre()

# On créé des objects geométriques
trace_point(5,3)
trace_segment(-10,-4,8,7,couleur='red', taille = 2)
trace_rectangle(1,1,8,4,couleur='black', taille = 4, remplissage='yellow')
trace_point(5,5,couleur='blue',taille=5)
trace_point(6,7,couleur='blue',taille=5,forme='croix')
trace_texte(-3,3,"Un texte",couleur = 'blue')

# On affiche la fenetre
affiche_graphique()
```
```eval_rst
.. note::
    Il faut désactiver [l'affichage de variables](../#affichage-des-variables) dans thonny pour pouvoir utiliser cette librairie.
```



## Techniquement

Le coté non dynamique mentionné plus haut vient de l'utilisation de Tkinter. C'est [techniquement possible](https://stackoverflow.com/questions/459083/how-do-you-run-your-own-code-alongside-tkinters-event-loop) avec la méthode [after](http://effbot.org/tkinterbook/widget.htm#Tkinter.Widget.after-method) mais pas réaliste dans un cadre pédagogique.

La principale modification par rapport à la version de Olivier Brebant est de créer une variable globale `fenetre`.
Cela simplifie l'utilisation pour les élèves auquel on cache le coté méthodes et attributs de la programmation orientée objet. Concrètement, on passe d'une utilisation:

```python
fen = creer_fenetre()
fen.trace_point(5,5,couleur='blue',taille=5)
fen.loop()
```

à
```python
creer_fenetre()
trace_point(5,5,couleur='blue',taille=5)
affiche_fenetre()
```

Par contre cela limite l'utilisation de cette librairie à une unique instance de l’objet `fenetre`. Limitation raisonnable dans un cadre pédagogique. Faux, contre exemple avec  [2fenetresEnMemeTemps.py](https://gist.github.com/al-coloic/c158ed66dd2b627049f5ad2562355fa7).   

## Documentation
```eval_rst
    .. automodule:: graphique
        :members:
        :member-order: bysource
```
