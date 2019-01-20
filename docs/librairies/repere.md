# Repere
:download:`repere.py </../Thonny/Lib/site-packages/repere.py>`
## A propos
Cette [bibliothèque](https://github.com/cspaier/thonny/blob/diderot/Thonny/Lib/site-packages/repere.py) facilite l'affichage d'une fenêtre munie d'un repère interactif (zoom, déplacement). Des fonctions sont disponibles pour tracer des objets géométriques simples.

C'est une Version légèrement modifiée de [cette librairie](https://www.pedagogie.ac-aix-marseille.fr/jcms/c_122350/fr/ressources-graphiques-pour-python) écrite par Olivier Brebant en 2011 et publié par l'académie d'Aix-Marseille en 2012, sous licence MIT depuis novembre 2018.


## A quoi ca sert?
A tracer un graphique **non dynamique** muni (ou non) d'un repère.
On peut par exemple construire facilement un [traceur de courbes](https://gist.github.com/cspaier/3c67ddb66218ee53e7deaef6a61aeb8a).

Par non dynamique, j’entends qu'on ne peut pas facilement utiliser cette librairie pour interagir directement avec les objets. Par exemple cette librairie n'est pas adaptée au codage d'un jeu de type pong ou même d'un objet en mouvement.


## Comment l'utiliser
```python
# On importe la librairie
from repere import *

# On initialise la fenetre
creer_fenetre()

# On créé des objects geométriques
trace_point(5,3)
trace_segment(-10,-4,8,7,couleur='rouge', taille = 2)
trace_rectangle(1,1,8,4,couleur='noir', taille = 4, remplissage='jaune')
trace_point(5,5,couleur='bleu',taille=5)
trace_point(6,7,couleur='bleu',taille=5,forme='croix')
trace_texte(-3,3,"Un texte",couleur = 'bleu')
```

On peut agir sur le repère grâce à la souris:

- La :guilabel:`roulette` de la souris:
  - Si le curseur est proche d’un axe, modifie l’échelle uniquement pour cet axe.
  - Sinon zoome/dézoome par rapport à la position courante du curseur
- Un :guilabel:`Cliquer-glisser`:
  - Si le curseur est proche d’un axe, translate le repère suivant cet axe.
  - Sinon déplace le repère suivant le mouvement libre de la souris.
- Un :guilabel:`double clic` rend le repère orthonormé en se basant sur l’axe des abscisses.


.. note::
    Il faut désactiver `l'affichage de variables </#affichage-des-variables>`_  dans thonny pour pouvoir utiliser cette librairie.

## Couleurs
.. mdinclude:: ../couleurs.md


## Techniquement

Le coté non dynamique mentionné plus haut vient de l'utilisation de Tkinter. C'est [techniquement possible](https://stackoverflow.com/questions/459083/how-do-you-run-your-own-code-alongside-tkinters-event-loop) avec la méthode [after](http://effbot.org/tkinterbook/widget.htm#Tkinter.Widget.after-method) mais pas réaliste dans un cadre pédagogique.

La principale modification par rapport à la version de Olivier Brebant est de créer une variable globale `fenetre`.
Cela simplifie l'utilisation pour les $E = mc^2$ élèves auquel on cache le coté méthodes et attributs de la programmation orientée objet. Concrètement, on passe d'une utilisation:

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

.. note::
    L'utilisation de cette librairie n'est pas limitée à une unique instance de l’objet `fenetre`. Voici un exemple avec  [2fenetresEnMemeTemps.py](https://gist.github.com/al-coloic/c158ed66dd2b627049f5ad2562355fa7).

## Documentation


.. automodule:: repere
    :members:
    :member-order: bysource

.. eof
