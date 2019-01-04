# Formation technique.

*Ce document est utilisé pour former les collègues du lycée à l'utilisation de l'environnement Thonny / Python / modules "maison"*

## 1. Où se trouve le raccourci vers thonny

Démarrer > Programmes > \_Maths > Raccourcis maths > Thonny python

## 2. Prise en main :
Quand on lance Thonny, il y a deux zones :
![](https://thonny.org/img/get_started.png)
 - la zone du haut où on travaille dans un fichier, qui peut être exécuté quand on le demande, et qui peut être enregistré (sur cette image, le fichier s'appelle "Hell.py")
 - la zone du bas qui est un **shell** : comme un écran de calculatrice, mais qui exécute des commandes Python (on ne peut pas l'enregistrer)(c'est dans cette zone qu'apparaissent les résultats des commandes exécutées depuis un fichier de la zone du haut)

### Quelques instructions à essayer dans le shell :
```python
3+4
print("hello world")
"hello"+"world"
```
### Quelques exemples à enregistrer dans un fichier :
```python
3+4
print("hello world")
"hello"+"world"
```
Pour exécuter le fichier, il faut cliquer sur le bouton **run** (un triangle blanc dans un disque vert) ou appuyer sur **F5**.
Il faut donner un nom au fichier. Le fichier sera sauvegardé par défaut dans : `USER/python`

## 3. Quelques trucs sur python :
### 3.a. Variable
Une des difficulté principale pour les élèves au début (en seconde) est l'utilisation de variables.

Quelques lignes à tester :
```python
x = 4
y = x + 1
print(y)
```
### 3.b. Typage et ce que provoque l’absence de typage
Les variables peuvent être de différent type : par exemple "entier" `int` ou "chaîne de caractères (texte)" `str` ou encore "nombre à virgule flottante" `float`.

Souvent, on peut suggérer facilement à Python le type utilisé. Par exemple, `a=2` est de type `ìnt`, `a=2.0` est de type `float`, `a='2'` ou `a="2"` est de type `str`.

Si Python ne sait pas trop quel est le type d'une variable, il essaye de faire un choix (par exemple il considère que la variable est de type "texte" `str`) ou alors il renvoie un message d'erreur.

Les messages d'erreur apparaissent en rouge dans le shell. Même s'ils sont indigestes, il faut expliquer aux élèves que dans un message d'erreur il y a deux informations très utiles :
 - une explication sur l'erreur (par exemple le mot-clé "typeError" signale qu'il s'agit d'une erreur de typage)
 - la ligne du fichier où l'erreur a été rencontrée (en bleu et cliquable pour aller directement au bon endroit du fichier)

Essayez de faire exécuter ces instructions :
```python
3*'13'
'3'*'13'
'3'+'13'
3+'13'
3*13
3*13.0
```
### 3.c. Deux trucs :

 - pour aller vite dans le shell, on peut rappeler les instructions précédemment tapées en appuyant sur la flèche du haut
 - pour mettre un commentaire, il suffit de le précéder d'un #

### 3.d. Deux fonctions d'entrée / sortie :
 - `input()` permet de faire demander par Python à l'utilisateur de d'entrer quelque chose au clavier.
 - `print()` permet de demander à Python l'affichage de quelque chose.

Essayez de faire exécuter ces instructions :
```python
input("tapez quelque chose")
a=input("tapez quelque chose")
a
print(a)
type(a)
```
### 3.e. Retour sur les problèmes de typage : formule magique : ...=float(input(« ... »))

Si vous avez essayé les lignes de code précédentes avec diverses entrées tapées au clvier, vous avez peut-être remarqué que quel que soit ce qu'on tape, Python considère que ce qui vient du `ìnput()` est du type `str`.

Du coup, cela va sans cesse provoquer des erreurs dans les programmes des élèves. Un des moyens d'éviter cela est de leur donner la ligne de `input` sous la forme suivante :

```python
a=float(input("tapez quelque chose"))
```
`a` sera alors automatiquement du type "nombre à virgule flottante", ce qui est en général ce qu'on veut.

## 4. Librairies :
### 4.a. Généralités :
Python ne charge pas toutes les commandes disponibles lorsqu'on le lance. Si on a besoin d'une commande non chargée, il faut demander le chargement de la librairie.
```python
print(sqrt(2))
```
solution :
```python
from math import sqrt
print(sqrt(2))
```
une autre solution (si on doit utiliser plusieurs fonctions du même module) :
```python
import math
print(math.sqrt(2))
print(math.pi)
```
une autre solution (si on veut renommer le module) :
```python
import math as m
print(m.sqrt(2))
print(m.pi)
```
### 4.b. Quelques exemples avec les librairies « maison »

La librairie `entree_tk` permet de répondre au problème de typage évoqué précédemment :

```python
from entree_tk import *
demander_texte()
a=demander_reel()
print(type(a))
print(a)
```
La librairie `graphique` permet d'afficher facilement une fenêtre graphique où on fera par exemple afficher la courbe d'une fonction.

```python
from graphique import *
creer_fenetre()
trace_segment(1,2,3,5)
trace_point(3,3)
```
Un autre exempke, plus élaboré :
```python
from math import *
from graphique import *
creer_fenetre()
for i in range(100): #i va de 0 à 100
    x=i/10-5 #x va de -5 à 5
    trace_point(x,cos(x))
```

5) python avec les élèves : prise en main
- où les élèves doivent-ils enregistrer leur travail ?
- ctrl +/ crl molette pour zoomer
- le fait que la config est enregistrée automatiquement quand on quitte thonny
- view > variables pour voir le contenu des variables
- tools > options < show lines numbers
- debug et les différents types de « pas à pas »
- exemple de programme :

xA=input("Abscisse de A ? ")
yA=input("Ordonnée de A ? ")
xB=input("Abscisse de B ? ")
yB=input("Ordonnée de B ? ")
xM=(float(xA)+float(xB))/2
yM=(float(yA)+float(yB))/2
print("Coordonnées du milieu : ("+str(xM)+" ; "+str(yM)+")")

→ exo : le refaire et l’améliorer en ajoutant de quoi afficher la distance AB
→ on peut demander exactement la même chose à une classe à condition d’écrire au tableau la « formule magique »

6) gestion salle info

ce qui ne marche pas : parler à un groupe d'élèves devant leur écran
ce qui peut marcher :
- faire se lever tout le groupe, venir devant le tableau et parler avec le vidéo-projecteur
- verrouiller tous les écrans (ça peut se faire avec le logiciel...)(il y a souvent un ou deux écrans qui ne se verrouillent pas !), donner les consignes, puis déverrouiller
- envoyer son écran dans les écrans de tous les élèves (avec la commande "démo" du logiciel ...), parler en montrant à l'écran en même temps, puis arrêter la démo (les élèves sont encore bluffés par cette manip pour le moment :-)
 - annoncer au groupe "je vais vous envoyer l'écran de -nom d'élève-" (avec la commande clic droit > "laisser faire une démo" du logiciel ...), laisser l'élève faire sa démo (en l'incitant à parler de façon compréhensible), puis arrêter la démo (je ne sais pas comment faire alors je vérrouille / déverrouille !)

6) un peu plus loin :
- comment envoyer du code aux élèves ? / comment récupérer du code qu’ils ont fait ?
- comment peut-on (les élèves ou nous) télécharger thonny pour chez nous ?
- comment peut-on demander à ajouter une fonction dans les librairies ?

7) un ou deux autres exemples d’activités à faire avec les élèves.
traceur de courbes?
discriminant ?

8) un peu plus de python : listes, boucles
Les listes sont-elles nécessaires?
