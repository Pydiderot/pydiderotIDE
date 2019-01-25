# Formation technique
## 1.Quoi? pour qui?
Ce document est utilisé pour former les collègues du lycée à l'utilisation de l'environnement python du lycée. Il est téléchargeable en pdf à l'url https://pydiderot.readthedocs.io/_static/formation.pdf.
Il est à destination des professeurs n'ayant pas ou peu de connaissances sur le langage python.

L'objectif est d'introduire, à l'aide d'exemples et d'exercices:

   - le langage de programmation
   - l'environnement de développement thonny utilisé au lycée
   - les librairies propres au lycée Diderot
   - quelques constats pratiques d'ordre pédagogique.



## 2. Prise en main
.. figure:: https://thonny.org/img/get_started.png
    :align: right
    :width: 200px

A partir du bureau des ordinateurs du lycée: `Logiciels > MATH > _Maths > _RACCOURCIS MATH_ > Thonny python`

Quand on lance Thonny, il y a deux zones :

- la zone du haut où on travaille dans un fichier, qui peut être exécuté quand on le demande, et qui peut être enregistré (sur cette image, le fichier s'appelle "Hello.py")
- la zone du bas qui est un **shell** : comme un écran de calculatrice, mais qui exécute des commandes Python (on ne peut pas l'enregistrer)(c'est dans cette zone qu'apparaissent les résultats des commandes exécutées depuis un fichier de la zone du haut)

### Quelques instructions à essayer dans le shell :
```python
3 + 4
print("hello world")
"hello" + "world"
```
### Quelques exemples à enregistrer dans un fichier :
```python
3 + 4
print("hello world")
"hello" + "world"
```
Pour exécuter le fichier, il faut cliquer sur le bouton |run|  ou appuyer sur :guilabel:`F5`.
Il faut donner un nom au fichier. Le fichier sera sauvegardé par défaut dans : `USER/python`

.. |run| image:: /source/_static/bouton_run.png

## 3. Quelques trucs sur python

.. figure:: https://www.python.org/static/img/python-logo-large.png
    :align: right
    :width: 100px

Python est un langage de programmation libre qui fonctionne sur toutes plate-formes (Windows, Mac, Linux, Android,…). Il à été créé au début des années 90 et baptisé en l’honneur de la série Monty Python's Flying Circus.

Épuré et lisible, Python est utilisé par de nombreuses entreprises et organisations (Google, NASA, …), dans la recherche scientifique et est enseigné au lycée, en prépa, et à l’université.

Les projets de [nouveaux programmes](http://cache.media.education.gouv.fr/file/CSP/19/8/2de_Mathematiques_Enseignement_commun_1021198.pdf) précisent le choix de python comme langage de programmation utilisé à partir de la seconde.


### 3.a. Variable
Une des difficulté principale pour les élèves au début (en seconde) est l'utilisation de variables.

.. note:: Voir `5.b <#b-variables>`_ ci dessous pour des remarques concernant des outils pédagogiques à la notion de variable.

Quelques lignes à tester :
```python
x = 4
y = x + 1
print(y)
```

### 3.b. Typage et ce que provoque l’absence de typage
Les variables peuvent être de différents types : par exemple "entier" `int` ou "chaîne de caractères (texte)" `str` ou encore "nombre à virgule flottante" `float`.

Souvent, on peut suggérer facilement à Python le type utilisé. Par exemple, `a=2` est de type `ìnt`, `a=2.0` est de type `float`, `a='2'` ou `a="2"` est de type `str`.

Si Python ne sait pas trop quel est le type d'une variable, il essaye de faire un choix (par exemple il considère que la variable est de type "texte" `str`) ou alors il renvoie un message d'erreur.

Les messages d'erreur apparaissent en rouge dans le shell. Même s'ils sont indigestes, il faut expliquer aux élèves que dans un message d'erreur il y a deux informations très utiles :


- une explication sur l'erreur (par exemple le mot-clé "typeError" signale qu'il s'agit d'une erreur de typage)
- la ligne du fichier où l'erreur a été rencontrée (en bleu et cliquable pour aller directement au bon endroit du fichier)

Essayez de faire exécuter ces instructions :
```python
3 * '13'
'3' * '13'
'3' + '13'
3 + '13'
3 * 13
3 * 13.0
```

.. note::
 - pour aller vite dans le shell, on peut rappeler les instructions précédemment tapées en appuyant sur la flèche du haut
 - pour mettre un commentaire, il suffit de le précéder d'un #


### 3.c. Deux fonctions d'entrée / sortie :

.. figure:: /source/_static/entrees_sorties.png
    :align: center

- `input()` permet de faire demander par Python à l'utilisateur de d'entrer quelque chose au clavier.
- `print()` permet de demander à Python l'affichage de quelque chose.

Essayez de faire exécuter ces instructions :
```python
input("tapez quelque chose")
a = input("tapez quelque chose")
a
print(a)
type(a)
```
### 3.e. Retour sur les problèmes de typage : formule magique

Si vous avez essayé les lignes de code précédentes avec diverses entrées tapées au clavier, vous avez peut-être remarqué que quel que soit ce qu'on tape, Python considère que ce qui vient du `ìnput()` est du type `str`.

Du coup, cela va sans cesse provoquer des erreurs dans les programmes des élèves. Un des moyens d'éviter cela est de leur donner la ligne de `input` sous la forme suivante :

```python
a = float(input("tapez quelque chose"))
```
`a` sera alors automatiquement du type "nombre à virgule flottante", ce qui est en général ce qu'on veut.

Exercice: Demander deux nombres à l'utilisateur et afficher leur produit.

### 3.d Indentation

Pour signaler le début et la fin de blocs de code, on utilise l'indentation. Une indentation correspond à 4 espaces.

```python

print("Bonjour!")

for x in range(10):
    # début du sous-block for
    print(x)

# Nous sommes sortis du sous-bloc "for"
print("C'est fini.")
```

```python

print("Bonjour!")

for x in range(10):
    # début du sous-block "for"
    print(x)
    # Nous sommes toujours dans le bloc "for"
    print("C'est pas fini.")

# Nous sommes sortis du sous-bloc "for"
print("C'est fini.")
```
.. note::
  L'utilisation du mode "pas à pas" de thonny peut aider à illustrer cette notion (voir `5.c <#c-debug-et-les-differents-types-de-pas-a-pas>`_ ).

## 4. Librairies :
### 4.a. Généralités :
Python ne charge pas toutes les commandes disponibles lorsqu'on le lance. Si on a besoin d'une commande non chargée, il faut demander le chargement de la librairie.
```python
print(sqrt(2))
```
solutions :
1. On importe la fonction `sqrt` de la librairie [math](https://docs.python.org/fr/3/library/math.html). On peut ensuite l'utiliser directement.
```python
from math import sqrt
print(sqrt(2))
```

2. Une autre solution qui importe tout le contenu de la librairie [math](https://docs.python.org/fr/3/library/math.html) :
```python
from math import *
print(sqrt(2))
print(pi)
```

### 4.b. Quelques exemples avec les librairies « maison »

La librairie [entree](/librairies/entree) permet de répondre au problème de typage évoqué précédemment :

```python
from entree import *
demander_texte()
a=demander_reel()
print(type(a))
print(a)
```
La librairie [repere](/librairies/repere) permet d'afficher facilement une fenêtre graphique munie d'un repère où on fera par exemple afficher la courbe d'une fonction.

```python
from repere import *
creer_fenetre()
trace_segment(1,2,3,5)
trace_point(3,3)
```

Un autre exemple, plus élaboré :

```python
from math import *
from repere import *
creer_fenetre()
for i in range(100): #i va de 0 à 100
    x = i / 10 - 5 #x va de -5 à 5
    trace_point(x,cos(x))
```
La même chose avec un "while" au lieu du "for" (quel est le plus simple avec les élèves ?) :

```python
from math import *
from repere import *
creer_fenetre()
x = -5
while x < 5:  # x va de -5 à 5
    trace_point(x, cos(x))
    x = x + 0.1
```
## 5. Python avec les élèves

### 5.a Prise en main
Voici quelques remarques que nous espérons utiles:

 - Les élèves enregistrent leur travail dans le dossier `USER/python/`.
 - Lors de la vidéoprojection de thonny, les caractères sont trop petits. On peut utiliser :guilabel:`ctrl` + :guilabel:`+` ou :guilabel:`ctrl` +  :guilabel:`molette` pour zoomer.
 - La config est enregistrée automatiquement quand on quitte thonny.
 - Pour afficher les numéros des lignes: :guilabel:`Tools` → :guilabel:`Otions` → :guilabel:`Editor` → :guilabel:`Show lines numbers`

### 5.b Variables

Comme annoncé plus haut, la notion de variable informatique n'est pas du tout évidente à appréhender pour les élèves.

Il peut être bon d'expliquer que concrètement, à chaque nouvelle variable `x`, la machine va créer un espace (une boite) dans la mémoire vive étiquetée par le nom de la variable (`x`). Nous pouvons ensuite lire le contenu de la boite avec `print(x)` et changer ce qu'elle contient avec `x = 3`.

.. figure:: https://thonny.org/img/variables.png
    :align: right
    :width: 200px

Thonny propose un affichage dynamique du contenu des variables accessible dans le menu :guilabel:`View` → :guilabel:`Variables` qui peut être particulièrement utile dans un cadre pédagogique.

Son utilisation n'est **pas compatible avec l'import de librairies**. En effet, l'onglet affichera le contenu de toutes les fonctions et variables importées ce qui peut ralentir considérablement l'utilisation.


### 5.c Debug et les différents types de « pas à pas »

Thonny propose un mode débug accessible avec le bouton |bouton_debug| ou les touches :guilabel:`crtl` + :guilabel:`F5`  qui permet l'éxécution du script en mode « pas à pas ». Cela activera le menu debug :|menu_debug|

- |bouton_step_over| ou :guilabel:`F6`: Passe au bloc suivant sans rentrer en détail dans le bloc.
- |bouton_step_into| ou :guilabel:`F7`: Rentre dans le bloc sélectionné pour en voir les détails.
- |bouton_step_out| : Sort du bloc sélectionné en remontant vers le bloc parent.
- |bouton_resume| ou :guilabel:`F8`: Quitte le mode débug et reprend l’exécution du script.

.. |bouton_debug| image:: /source/_static/bouton_debug.png
.. |menu_debug| image:: /source/_static/menu_debug.png
.. |bouton_step_over| image:: /source/_static/bouton_step_over.png
.. |bouton_step_into| image:: /source/_static/bouton_step_into.png
.. |bouton_resume| image:: /source/_static/bouton_resume.png
.. |bouton_step_out| image:: /source/_static/bouton_step_out.png

Voici par exemple un programme affichant la table de multiplication par 7 dont la vidéoprojection en mode débug peut avantageusement illustrer le fonctionnement d'une boucle et des variables:
```python
for x in range(10):
    y = 7 * x
    print(y)

print("Et voila!")
```
### 5.d. Gestion salle info

Ce qui ne marche pas : parler à un groupe d'élèves devant leur écran.

Ce qui peut marcher :

- faire se lever tout le groupe, venir devant le tableau et parler avec le vidéo-projecteur

- verrouiller tous les écrans (ça peut se faire avec le logiciel iTALC (il y a souvent un ou deux écrans qui ne se verrouillent pas !), donner les consignes, puis déverrouiller

![](https://raw.githubusercontent.com/cspaier/pydiderot/dev/docs/formation/Capture_iTALC.PNG)

- envoyer son écran dans les écrans de tous les élèves (avec la commande "démo" du logiciel iTALC), parler en montrant à l'écran en même temps, puis arrêter la démo (les élèves sont encore bluffés par cette manip pour le moment :-)

- annoncer au groupe "je vais vous envoyer l'écran de -nom d'élève-" (avec la commande clic droit > "laisser faire une démo" du logiciel iTALC), laisser l'élève faire sa démo (en l'incitant à parler de façon compréhensible), puis arrêter la démo (je ne sais pas comment faire alors je verrouille / déverrouille !)


## 6. un peu plus loin :
### 6.a Questions fréquentes
- comment peut-on (les élèves ou nous) télécharger thonny pour chez nous ?

Il suffit de se rendre sur https://pydiderot.readthedocs.io

- comment peut-on demander à ajouter une fonction dans les librairies ?

Ouvrir une issue sur https://github.com/cspaier/pydiderot

### 6.b. Exemples d'activités

#### Le milieu

```python
xA = float(input("Abscisse de A ? "))
yA = float(input("Ordonnée de A ? "))
xB = float(input("Abscisse de B ? "))
yB = float(input("Ordonnée de B ? "))
xM = (xA + xB) / 2
yM = (yA + yB) / 2

print("Coordonnées du milieu : (" + str(xM) + " ; " + str(yM) + ")")
```

__exo__ : le refaire et l’améliorer en ajoutant de quoi afficher la distance AB

__Remarque__ on peut demander exactement la même chose à une classe à condition d’écrire au tableau la « formule magique » ou d'utiliser la libraire [entree](/librairies/entree).

#### Ca bouge!

Voici un exemple utilisant la librairie [graphique](/librairies/graphique/) où une balle traverse l'écran en diagonale.

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

# On créé la fenêtre graphique de taille 200 x 300
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
a. Modifier le code pour que la balle traverse l'autre diagonale.
b. Faire en sorte que la balle rebondisse sur les bords de l'écran.
c. Faire en sorte que l'utilisateur déplace la balle avec la sourie ou l'écran. On pourra faire un `print(evenements())` pour explorer la gestion des événements.
