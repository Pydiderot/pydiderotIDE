# -*- coding: utf-8 -*-
#

"""
Fichier permettant de tester de façon systématique le bon fonctionnement des librairies
"""

from time import sleep
from tkinter import *
from .entree import *
from .lycee import *
import types
import pydiderotlibs.repere as repere
import pydiderotlibs.graphique as graphique

from .couleurs import _couleurs, rgb, rgb2hex


def test_lycee():
    """
    Teste les fonctions de lycee
    """
    print('\n Les fonctions de lycee')
    # arithmetique
    print('pgcd(12,4) =', pgcd(12, 4))
    print('pgcd(-4,12) = ', pgcd(-4, 12))

    print('reste(15,4) = ', reste(15, 4))

    print('quotient(15,4) = ', quotient(15, 4))

    # fonctions usuelles

    print('4**1/2 = ', puissance(4, 1 / 2))
    print('2**-2 = ', puissance(2, -2))

    print('carre =  ', carre(-2))

    print('racine de 4 = ', racine(4))

    print('4! = ', factoriel(4))

    print('Partie entière de -2,5 = ', partie_entiere(-2.5))
    print('Sans virgule = ', sans_virgule(-2.5))

    print('exp(1) = ', exp(1))
    print('ln(e) = ', ln(exp(1)))
    print('log(10) = ', log(10))


def test_chaines():
    print('\n Les fonctions sur les chaines')
    print('la fonction taille doit afficher 2 : ', taille('ab'))
    print('la fonction taille doit afficher 3 : ', taille([0, 1, 2]))

    chaine2fich('Yo !', 'blabla')
    print('Allez voir dans votre répertoire courant doit avoir un fichier blabla qui contient Yo !')
    input("Appuyez sur entrée pour continuer...")
    contenu = fich2chaine()
    print('Sélectionner le fichier blabla')
    print('La machine doit vous dire bonjour...')
    print('Machine : ', contenu)


def test_listes():
    print('\n Les fonctions sur les listes à partir de fichier')

    print('On doit avoir une liste de 0 à 9 : ',
          CSV2liste('A', 'TableurPourTest.csv'))
    print('On doit avoir une liste de 10 en 10 : ',
          CSV2liste(1, 'TableurPourTest.csv'))

    liste2CSV([1, 'a', 3, 'bonjour', 10, 'aurevoir'],
              fichier='TableurPourTest2.csv')
    print('Votre répertoire courant doit contenir un fichier TableurPourTest2.csv')

    x = [[1, 2, 'a'], [3, 4, 'b'], [5, 6, 'c'], [7, 8, 'd']]
    print(x)
    print("On transpose la liste ci-dessus : ", transposer(x))

    print("On affiche un polynome à partir d'une liste ",
          affiche_poly([1, 1, 1]))


def test_stats_proba():

    print('\n Les fonctions sur les stats et proba')

    print("Le nombre de choix de 2 parmi 5 : ", binomial(5, 2))

    print(
        "Un nombre au hasard avec la loi binomiale de 2 parmi 5: ",
        tirage_binomial(
            5,
            2))

    print("Un nombre entier au hasard entre -10 et 10 : ", alea_entier(-10, 10))

    print("Un nombre au hasard entre -5 et 5 avec la loi uniforme : ",
          tirage_uniforme(-5, 5))

    print(range(0, 11))
    print("Un nombre au hasard dans la liste précédente : ", choix(contenu))

    print("Renvoie au hasard un décimal de l'intervalle [0 , 1[ : ", alea())

    print(
        "Un nombre au hasard avec la loi exponentielle de paramètre 1 : ",
        tirage_expo(1))

    print(
        "Un nombre au hasard avec la loi normale de paramètre 0 et 1 : ",
        tirage_normale(
            0,
            1))

    ListeTest = [3, 2, 3, 4, 5, 6, 1, 2, 3, 4, 1, 2, 3]
    EffecTest = [
        1 / 55,
        2 / 55,
        3 / 55,
        4 / 55,
        5 / 55,
        6 / 55,
        7 / 55,
        8 / 55,
        9 / 55,
        1 / 55,
        2 / 55,
        3 / 55,
        4 / 55]
    print("Criteres : ", ListeTest, " avec les effectifs : ", EffecTest)
    c = compte(ListeTest, EffecTest)
    print("Compte la liste ci-dessus : ", compte(ListeTest, EffecTest))
    print("On range : ", trier(c[0], c[1]), "\n")

    ListeTest2 = ['bla', 2, 3, 4, 5, [5, 6], 'bla', 2, 3, 4, 'bla', 2, 3]
    EffecTest2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4]
    print("Criteres : ", ListeTest2, " avec les effectifs : ", EffecTest2)
    print("Compte la liste ci-dessus : ", compte(ListeTest2, EffecTest2))

    print(range(0, 11))
    print("Trouve le centre de la liste précédente : ", centres(range(0, 11)))

    L = [float(i) for i in range(100)]
    print("\n ------------------------------------\n", L)
    print("Moyenne de la liste ci-dessus : ", moyenne(L))
    print("Variance de la liste ci-dessus : ", variance(L))
    print("Ecart-type de la liste ci-dessus : ", ecartype(L))


def test_entree_tk():
    print('\n Les fonctions de entre_tk')
    nom = demander_texte('Bonjour', "Quel est ton nom?")

    age = demander_reel("Quel age as tu?")
    annee = str(int(2019 - age))

    print(nom + " est né(e) en " + annee)


def test_repere():
    # On initialise la fenetre
    repere.creer_fenetre()

    # On créé des objects geométriques
    repere.trace_point(5, 3)
    repere.trace_segment(-10, -4, 8, 7, couleur='rouge', taille=2)
    repere.trace_rectangle(
        1,
        1,
        8,
        4,
        couleur='noir',
        taille=4,
        remplissage='jaune')
    repere.trace_point(5, 5, couleur='bleu', taille=5)
    repere.trace_point(6, 7, couleur='bleu', taille=5, forme='croix')
    repere.trace_texte(-3, 3, "Un texte", couleur='bleu')


def test_graphique():
    # On créé la fenêtre graphique
    graphique.creer_fenetre()
    x = 100
    y = 100
    # Boucle principale
    while True:
        evenements = graphique.demande_evenements()

        if 'souris' in evenements:
            [x, y] = evenements['souris']

        if 'clic' in evenements:
            # ici evenements['clic'] est une liste [x, y]
            print('clic aux coordonées ' + str(evenements['clic']))

        # Trace un cercle au coordonnées (x,y)
        graphique.trace_cercle(x, y)
        # Attend un dixième de secondes
        sleep(0.1)
        # Efface le cercle
        graphique.trace_cercle(x, y, couleur='blanc')


def test_couleurs():
    """
    Affiche les couleurs disponibles.

    http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
    """
    MAX_ROWS = 12
    FONT_SIZE = 30  # (pixels)
    root = tk.Tk()
    root.title("Named colour chart")
    row = 0
    col = 0
    for c, t in _couleurs.items():
        texte = c + " " + str(t)
        if c in ['noir', 'bleu']:
            couleur = rgb2hex(rgb('blanc'))
        else:
            couleur = rgb2hex(rgb('noir'))
        e = Label(
            root,
            text=texte,
            background=rgb2hex(t),
            foreground=couleur,
            font=(None, -FONT_SIZE)
        )
        e.grid(row=row, column=col, sticky=E + W)
        row += 1
        if (row > MAX_ROWS):
            row = 0
            col += 1

    root.mainloop()


print("\n" * 10)
message = "Vous pouvez tester les différents modules avec les fonctions suivantes:\n"
fonctions = [f + "()" for f in dir() if f.startswith("test")]
message += "\n".join(fonctions)
print(message)
