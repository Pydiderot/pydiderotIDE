# Formation Python 2 : échanges sur le plan pédagogique

## 1. Quoi? pour qui?
Ce document est utilisé en formation interne au lycée, pour partager nos expériences avec l'environnement python du lycée. 
Il est téléchargeable en pdf à l'url https://pydiderot.readthedocs.io/_static/formation2.pdf.

Il fait référence à des documents mutualisés en interne par les professeurs du lycée Diderot, Marseille. Ces documents ne sont pas forcément publiés.

L'objectif est de :

   - partager des idées d'activités sur l'algorithmique (une synthèse des activités mutualisées par les collègues est proposée)
   - partager les difficultés que rencontrent nos élèves dans l'apprentissage de l'algorithmique
   - partager les difficultés techniques que nous rencontrons ou que rencontrent nos élèves dans l'utilisation de l'environnement pydiderot
   - discuter d'une progression sur l'algorithmique


## 2. Synthèse des activités mutualisées


## 3. Difficultés
### La notion de variable
introduction délicate : ne pas croire que c'est facile

différentes utilisation : '''x=5''' est plus simple à comprendre pour les élèves que '''x=x+1''' ou que '''for j in range(5)'''

faire une activité débranchée

faire un travail préalable en maths (ou en parallèle)
### La notion de boucle
#### Boucle "while"
nécessite d'expliquer '''x=x+1'''

nécessite de traduire en langage python "tant que j < 5, il faut répéter ..... fin."

le "il faut répéter" se traduit par une virgule !

le "fin" se traduit par une absence de tabulation !

#### Boucle "for"
nécessite d'expliquer le range()...
#### Difficultés liées au langage
#### Difficultés liées aux librairies créées spécialement pour pydiderot
#### Difficultés techniques



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
