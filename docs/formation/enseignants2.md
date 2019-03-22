# Formation Python 2 : échanges sur le plan pédagogique

## 1. Quoi? pour qui?
Ce document est utilisé en formation interne au lycée, pour partager nos expériences avec l'environnement python du lycée. 
Il est téléchargeable en pdf à l'url https://pydiderot.readthedocs.io/_static/formation2.pdf.

Il fait référence à des documents mutualisés en interne par les professeurs du lycée Diderot, Marseille. Ces documents ne sont pas forcément publics.

L'objectif est de :

   - partager des idées d'activités sur l'algorithmique (une synthèse des activités mutualisées par les collègues est proposée)
   - partager les difficultés que rencontrent nos élèves dans l'apprentissage de l'algorithmique
   - partager les difficultés techniques que nous rencontrons ou que rencontrent nos élèves dans l'utilisation de l'environnement pydiderot
   - mettre en place une progression commune sur l'algorithmique


## 2. Synthèse des activités mutualisées
#### 1. Documents généraux
 - liste d'idées de questions d'algo en lien avec les programmes 

fichier "progression algo en parallèle.odt", Loïc

 - quelques trames de séances très basiques sur la prise en main, les opérations de base, une première fonction, le début avec les listes (Python)

fichier "séances_python.odt", Loïc

 - des idées sur l'introduction progressive de la notion de variable, avec quelques idées d'activités 

fichier "progression début algo", Paul

#### 2. Fichiers techniques

 - une fiche reprenant une liste d'instructions disponibles, avec à chaque fois une description et un exemple. Cette fiche donne des instructions disponible dans un petit environnement javascript, du genre de celui [http://byachepaul.web4me.fr/GeometrieJeuxVideo/2nde/build/index.html](visible ici), et repris [http://byachepaul.web4me.fr/blockly/v1/](en blockly ici).
 Il faudrait le reprendre avec nos instructions disponibles dans pydiderot. Il serait sans doute judicieux également de créer un environnement Blockly qui mime pydiderot, de façon à pouvoir basculer facilement de l'un à l'autre, notamment en classe de seconde...
 
 fichier "Liste instructions python.pdf", Paul

#### 2. Activités avec Python

 - deux activités sur la recherche du maximum d'une fonction, testées cette année (boucles while en python et utilisation de la librairie "repère")

fichier "2nde act algo fonction max.odt", Paul

 - un TP de 1S avec boucle for, boucle while et librairie "repère"

fichier "TP_1S.odt", Clément

 - une activité de 1STI2D (prise en main de Python, boucle for, à réécrire avec la nouvelle version de pydiderot)
 
 fichier "1STI2D_La fusée dans l’espace.pdf",Loïc

#### 3. Activités sans Python

 - une activité sur la découverte de la dérivée de la fonction carrée en réalisant l'enveloppe d'une famille de droites (boucle 'for' dans un outil wims)

fichier "1STD2A act tangentes fonction carrée.odt", Paul

 - une activité se 2nde pour utiliser les coordonnées (variable, boucle, code à modifier facilement, mais compliqué à écrire pour les élèves)(Javascript)
 
fichier "2nde act algo enonce (javascript).odt", Paul

## 3. Difficultés
### La notion de variable
introduction délicate : ne pas croire que c'est facile

différentes utilisation : `x=5` est plus simple à comprendre pour les élèves que `x=x+1` ou que `for j in range(5)`

faire une activité débranchée

faire un travail préalable en maths (ou en parallèle)
### La notion de boucle
#### Boucle "while"
nécessite d'expliquer `x=x+1`

nécessite de traduire en langage python "tant que j < 5, il faut répéter ..... fin."

le "il faut répéter" se traduit par une virgule !

le "fin" se traduit par une absence de tabulation !

#### Boucle "for"
nécessite d'expliquer le range()...
#### Difficultés liées au langage
il faut expliquer le fait qu'il y a du code qu'on écrit en général dans un fichier et qu'il y a ensuite l'exécution du code

que l'indentation a du sens

que les commandes sont suivies de parenthèses, sans espace (comme par exemple `print('coucou')`)

les différents types (ou au moins les marqueurs "guillemets" pour le type string)



#### Difficultés liées aux librairies créées spécialement pour pydiderot

il est difficile de devoir sans cesse réécrire au tableau les noms des commandes

de plus, les nommages ne sont pas forcément ultra-judicieux.

Conclusion : faire un doc papier avec les différentes commandes + pour l'année prochaine, renommer les commandes. Le plus cohérent avec python existant : nommer les commandes en anglais + conserver la même structure par exemple au lieu de `creer_fenetre()` et `trace_point()`, mettre : `window()` et `point()`

#### Difficultés techniques

les plantages de la nouvelle version de pydiderot : aucun réel plantage détecté, par contre une difficulté liée sans doute à l'installation sur le réseau du lycée : souvent, thonny se met à "ramer". Dans ce cas, il suffit de le fermer et de le réouvrir. Le travail est automaztiquement enregistré, donc rien n'est perdu.

## 4. Progression

**********la suite est à modifier*****************
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
