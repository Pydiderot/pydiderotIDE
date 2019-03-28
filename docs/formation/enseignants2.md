# Formation Python 2 : échanges sur le plan pédagogique

## 1. Quoi ? pour qui ?
Ce document est utilisé en formation interne au lycée, pour partager nos expériences avec l'environnement python du lycée. 
Il est téléchargeable en pdf à l'url https://pydiderot.readthedocs.io/_static/formation2.pdf.

Il fait référence à des documents mutualisés en interne par les professeurs du lycée Diderot, Marseille. Ces documents ne sont pas forcément publics.

L'objectif est de :

   - partager des idées d'activités sur l'algorithmique (une synthèse des activités mutualisées par les collègues est proposée)
   - partager les difficultés que rencontrent nos élèves dans l'apprentissage de l'algorithmique
   - partager les difficultés techniques que nous rencontrons ou que rencontrent nos élèves dans l'utilisation de l'environnement pydiderot
   - mettre en place une progression commune sur l'algorithmique


## 2. Synthèse des activités mutualisées

Les documents qui se trouvent dans : `Atrium > Mes sites > Professeurs de maths > Documents > Python > Mutualisation` se répartissent ainsi : il y a des documents généraux, des fiches techniques, des activités à faire avec les élèves (certaines avec Python, d'autres sans Python). 

#### 1. Documents généraux
 - une liste d'idées d'algorithmes qui peuvent être en lien avec les programmes 

  *fichier "progression algo en parallèle.odt", Loïc*

 
 - quelques trames de séances très basiques sur la prise en main, les opérations de base, une première fonction, le début avec les listes (Python)

  *fichier "séances_python.odt", Loïc*

 
 - des remarques sur l'introduction progressive de la notion de variable, avec quelques idées d'activités 

  *fichier "progression début algo", Paul*

 
#### 2. Fiches techniques

 - une fiche à donner aux élèves, reprenant la liste des commandes disponibles, avec à chaque fois une description et un exemple. Cette fiche correspond à un petit environnement javascript, du genre de celui [visible ici](http://byachepaul.web4me.fr/GeometrieJeuxVideo/2nde/build/index.html), et repris [en blockly ici](http://byachepaul.web4me.fr/blockly/v1/).
 Il faudrait la refaire pour pydiderot. Il serait sans doute judicieux également de créer un environnement Blockly qui mime pydiderot, de façon à pouvoir basculer facilement de l'un à l'autre, notamment en classe de seconde...
 
  *fichier "Liste instructions python.pdf", Paul*

#### 3. Activités avec Python

 - deux activités sur la recherche du maximum d'une fonction (boucles while en python et utilisation de la librairie "repère")
 
  *fichier "2nde act algo fonction max.odt", Paul*

  
 - un TP de 1S avec boucle for, boucle while et librairie "repère"

  *fichier "TP_1S.odt", Clément*

 
 - une activité de 1STI2D (prise en main de Python, boucle for, à réécrire avec la nouvelle version de pydiderot)
 
  *fichier "1STI2D_La fusée dans l’espace.pdf",Loïc*
 
  
 - une activité sur les suites en 1S qui donne lieu a un travail sur les boucles
 
  *fichier "Activités suites et boucles.pdf", Loïc*

 
#### 4. Activités sans Python

 - une activité sans ordinateur, pour mettre en évidence la notion de boucle et celle de variable

  *fichier "act debranchee boucle et variable (1).odt", Paul*

 
 - une activité sur la découverte de la dérivée de la fonction carrée en réalisant l'enveloppe d'une famille de droites (boucle 'for' *préparée* dans un outil Wims)

  *fichier "1STD2A act tangentes fonction carrée.odt", Paul*

 
 - une activité de 2nde pour utiliser les coordonnées (variable, boucle, code à modifier facilement, mais compliqué à écrire pour les élèves)(Javascript)
 
  *fichier "2nde act algo enonce (javascript).odt", Paul*

 
 - une activité de seconde sur les vecteurs (coordonnées de vecteurs pour faire rebondir une balle en mouvement sur les parois d'un rectangle)(blockly)
 
  *fichier "act 2nde vecteurs blockly.odt", Paul*

 
 - un exercice d'entraînement où il faut créer du code blockly
 
  *fichier "2nde axo algo blocklypouraujourdhui.odt", Paul*

 
 - une activité plus difficile où il faut utiliser les intervalles et la logique pour programmer une fonction qui détecte si deux rectangles s'intersectent ou non (pseudo-code / javascript)

  *fichier "2nde act algo jeu video intervalles.odt", Paul*

 
 - Quelques idées pour la TSTD2A (javascript / pseudo-code)
 
  [voir ici](http://byachepaul.web4me.fr/GeometrieJeuxVideo/Tale/build/index.html)
 
 - Quelques idées pour la seconde (javascript)
 
  [voir ici](http://byachepaul.web4me.fr/GeometrieJeuxVideo/2nde/build/index.html)

## 3. Difficultés


### La notion de variable


La notion de variable pose des problèmes aux élèves. Son introduction doit être considérée comme délicate : attention à ne pas croire que c'est facile pour eux, sinon on risque des désillusions.

Ceci dit, différentes utilisations existent : `x=5` est plus simple à comprendre pour les élèves que `x=x+1` ou que `for j in range(5)`...

Pour y aller en douceur, on peut par exemple faire une première activité "débranchée" (mais cela peut sembler inutile lorsqu'ils ont déjà travaillé ce genre de choses au collège...).

Un exemple d'activité débranchée où le codage de `j=j+1` s'impose :

.. figure:: https://raw.githubusercontent.com/cspaier/pydiderot/dev/docs/formation/variable_necessaire.PNG
    :align: center
    :width: 200px


On peut aussi faire un travail préalable en maths (avant ou en parallèle du travail en algo) : faire une ou deux études de fonctions où les variables sont modélisées par des curseurs GeoGebra par exemple...


### La notion de boucle


Remarques générales : la notion de boucle pose moins de problème aux élèves que la notion de variable. On peut très bien faire des boucles sans variable, par exemple en blockly ou en "débranché". L'instruction est alors du type "répéter 5 fois...". Les élèves comprennent très bien l'intérêt de demander à l'ordinateur de répéter plusieurs fois les mêmes instructions.

Un exemple d'image qu'on peut générer avec une fonction "entier_aleatoire()" et des boucles de type "répéter 1000 fois". Aucune variable n'est nécessaire.

.. figure:: https://raw.githubusercontent.com/cspaier/pydiderot/dev/docs/formation/avec_fonction_mais_sans_variable.PNG
    :align: center
    :width: 200px

Cependant, en Python, difficile de faire une boucle sans variable. On a essentiellement le choix entre "for j in range(5)" et "while j<5 : ... j=j+1". Dans les deux cas, le travail sur la variable "compteur" j s'impose.

Une autre remarque : ce travail a un coût pour les élèves. Si on présente par exemple les quelques lignes de syntaxe permettant de faire une boucle "while", ces lignes ne paraissent pas naturelles. De plus, leur mémorisation par les élèves ne va pas du tout de soi. Enfin, ils ne comprennent pas forcément très vite à quel point ces quelques lignes permettent de résoudre un GRAND nombre de problèmes. Tous les ingrédients sont donc réunis pour que les élèves décrochent.

Propositions de remèdes : aller progressivement, faire faire prendre conscience de l'utilité de la structure de boucle while...

Voici un exemple d'activité débranchée pour mettre en évidence l'intérêt de faire une boucle.
Cependant, on n'a pas besoin spécialement d'une boucle "while" !

.. figure:: https://raw.githubusercontent.com/cspaier/pydiderot/dev/docs/formation/boucle_necessaire.PNG
    :align: center
    :width: 200px

Une idée : programmer une fonction "repeter(n,f)" qui répète n fois la fonction f (cela nécessite de commencer très tôt la notion de fonction en algorithmique mais ce n'est sans doute pas grave).

On utilise plusieurs fois cette fonction.

Ensuite, on s'arrange pour proposer des problèmes dans lesquels on ne sait pas à l'avance le nombre de fois où il faut répéter et/ou des problèmes où la vraiable "compteur" est utile. Cela permet alors de proposer la boucle while.

Un peu de comparaison entre les deux types de boucles :

#### Boucle "while"

Exemple simple :
```python
x=0
while x<3:
   print(x)
   x=x+1
print('fini !')
```
L'utilisation de cette boucle nécessite d'expliquer `x=x+1`

Elle nécessite de traduire en langage python "tant que j < 5, il faut répéter ..... fin."

Le "il faut répéter" se traduit par "deux points" !

Le "fin" se traduit par une absence de tabulation ! (Donc il faut expliquer ce qu'est une tabulation...)

#### Boucle "for"

Exemple simple :
```python
for x in range(3):
   print(x)
print('fini !')
```
Cette boucle nécessite d'expliquer le range()...

La difficulté peut-être contournée dans un premier temps par l'intruction suivante :
```python

for x in 1,2,3,4,5,6,7,8:
   U=U+2

```
en calculant seulement le U au rang 8.



#### Boucles et suites

Observations après l'activité boucle et suite (cf. plus haut). Il y a beaucoup de variables à considérer pour une suite Un. Les valeurs et rang initiaux, les valeurs et rang finaux désirés et un compteur de boucle : tous les rangs intermédiaires qu'il faut calculer.

Le 'n' dans Un en math joue à la fois le rôle de rang final et de compteur de la boucle...

#### Difficultés liées au langage

Python est un langage assez naturel et souple à utiliser, mais il y a quand même pleins de choses plus ou moins implicites chez les programmeurs et qui doivent être expliquées et travaillées avec les élèves. Petite liste :

Il faut expliquer le fait qu'il y a du code qu'on écrit en général dans un fichier et qu'il y a ensuite l'exécution du code.

Que l'indentation a du sens et qu'il ne faut pas indenter n'importe comment.

Que les commandes sont suivies de parenthèses, sans espace (comme par exemple `print('coucou')`)

Expliquer aussi les différents types (ou au moins les marqueurs "guillemets" pour le type `string`)

Que la fonction `input()` renvoie un string lorsqu'on lui passe un nombre et qu'il faut le convertir avec `int()`. 

Exemple :
```python

n=input("donner un nombre : ")
n=int(n)

```

#### Difficultés liées aux librairies créées spécialement pour pydiderot

Pydiderot contient le langage Python, l'IDE Thonny, quelques librairies couramment utilisées en Python et quelques librairies spécialement créées pour faciliter le codage à des élèves de lycée. ces dernières librairies ont été créées par d'autres et un peu modifiées pour le lycée Diderot, ou parfois créées spécialement pour le lycée Diderot.

Elles induisent fatalement quelques problèmes (mais en même temps elle permettent bien sûr de coder facilement des trucs intéressants et normalement inaccessibles pour des débutants !). Petite revue :

Il est difficile de devoir sans cesse réécrire au tableau les noms des commandes.
De plus, les nommages ne sont pas forcément ultra-judicieux.

Conclusion : d'où la proposition ci-dessus de créer un document pdf avec les différentes commandes + pour l'année prochaine, renommer les commandes. Le plus cohérent avec python existant : nommer les commandes en anglais + conserver la même structure par exemple au lieu de `creer_fenetre()` et `trace_point()`, mettre : `window()` et `point()`.

Autre proposition : on peut multiplier les fonctions (faire des alias) : faire une fonction `fenetre()` ET une fonction `window()` qui font la même chose.

#### Difficultés techniques

Les plantages de la nouvelle version de pydiderot : aucun réel plantage n'a été détecté, par contre une difficulté liée sans doute à l'installation sur le réseau du lycée revient fréquemment. Thonny se met à "ramer". Dans ce cas, il suffit de le fermer et de le réouvrir. Le travail est automatiquement enregistré, donc rien n'est perdu. Ca fait juste un peu "bricolage"...

## 4. Progression


 ### Seconde : 

 - fonction (expliquer les différences avec les fonctions en maths)
 - boucle (sans variable --> "répéter n fois")
 - variable (en liaison avec les fonctions d'une variable en maths)
 - boucle avec variable, mais simple (que des while avec la variable compteur qui est utilisée de façon hyper standardisée ?)
 - condition "if..." (pas de difficulté our les élèves ?)


 ### Première :


 - notion de liste
 - boucle "for"
 - boucles avec variables plus compliquées (typiquement : boucles pour résoudre les problèmes sur les suites, dans lesquels il y a aussi bien un travail possible sur l'indice de la suite que sur la valeur du terme de la suite)
 - boucle avec un "append" (instruction qui ajoute un élément à une liste)

 ### Terminale :


- rien de plus, retravail de ces notions
 

## 5. Les consignes dans nos activités

Quand on lit tout ce qui a été mutualisé, on peut regrouper les activités en fonction (par exemple) du type de consigne.

Une consigne très bête, mais parfois très utile : *recopiez ces lignes de code et faites les s'exécuter sur votre machine !*

.. figure:: https://raw.githubusercontent.com/cspaier/pydiderot/dev/docs/formation/consigne_recopier_solution.PNG
    :align: center
    :width: 400px

Une consigne un peu différente : *recopiez puis analysez*
    
.. figure:: https://raw.githubusercontent.com/cspaier/pydiderot/dev/docs/formation/consigne_recopier_puis_analyser.PNG
    :align: center
    :width: 400px

Une autre consigne, qui marche super bien mais qui n'apprend sans doute pas réellement aux élèves à coder : *modifiez ces lignes de code pour qu'on obtienne tel ou tel résultat* (Les élèves aiment bien et ils arrivent assez vite au résultat demandé en tâtonnant. Cependant : ils s'inventent des tas de "théorèmes élèves" sur le code qu'ils manipulent (c'est à dire qu'ils le comprennent souvent assez mal). Par ailleurs, si on leur demande par la suite de coder un petit programme à partir de zéro, c'est assez catastrophique si ça n'a pas été travaillé également de façon approfondie.

.. figure:: https://raw.githubusercontent.com/cspaier/pydiderot/dev/docs/formation/consigne_modif_code.PNG
    :align: center
    :width: 300px

Un exemple de consigne totalement non technique (là, au contraire, il s'agit vraiment de codage !) : 


.. figure:: https://raw.githubusercontent.com/cspaier/pydiderot/dev/docs/formation/consignes_non_techniques2.PNG
    :align: center
    :width: 500px

Un exemple de type "mini projet" où la consigne est très libre.
Cependant, le guidage provient du fait que les élèves vont essentiellement copier les exemples qui ont été travaillés précédemment.

.. figure:: https://raw.githubusercontent.com/cspaier/pydiderot/dev/docs/formation/consigne_liberte_guidee.PNG
    :align: center
    :width: 500px

## 6. Le dialogue entre les maths et l'algorithmique dans nos activités

Quand on lit tout ce qui a été mutualisé, on peut aussi regrouper les activités en fonction de l'objectif qui est présenté aux élèves.

Ici, un problème d'algorithmique devient le prétexte pour une étude mathématique qui utilise la notion d'intervalle de façon un peu inhabituelle :

.. figure:: https://raw.githubusercontent.com/cspaier/pydiderot/dev/docs/formation/algo_pretexte_pour_etude_math.PNG
    :align: center
    :width: 600px

Ici, on veut tester (en 1STD2A, sans avoir les moyens de le justifier mathématiquement) que la dérivée de la fonction carré est x->2x. Pour cela, on trace à l'aide d'une boucle for pleins de tangentes en calculant leurs coefficients directeurs grâce à cette fonction. Le résultat est une famille de droites faisant apparaître clairement la parabole de la fonction carré. C'est à la fois beau et convaincant.

.. figure:: https://raw.githubusercontent.com/cspaier/pydiderot/dev/docs/formation/prof_programme_util_justif_exp_math.PNG
    :align: center
    :width: 250px

.
