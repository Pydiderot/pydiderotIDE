"""
Partie listes du module lycee.
"""
"""
Créé à partir d' Edupython: http://edupython.tuxfamily.org/

Licence CECILL http://www.cecill.info/
"""

from math import floor, log
from .chaines import fich2chaine, chaine2fich

def CSV2liste(num, fichier='optionnel'):
    """
    Retourne une liste correspondant à la colonne ou la ligne nom du fichier ``fichier``.

    Si fichier n'est pas précisé, ouvre une boite de dialogue pour le choisir
    Le fichier ne doit contenir que des nombres et le séparateur doit être ``;``

    Arguments:
        num (str ou int): Un numéro de ligne ou un nom de colonne (``A`` à ``Z`` ).
        fichier (file,optionnel): Le nom complet (avec le chemin) d'un fichier contenant des nombres.
    """
    ch = fich2chaine(fichier)
    if isinstance(num, int):
        L = ch.split("\n")
        if len(L) >= num:
            R = []
            for n in L[num - 1].split(";"):
                try:
                    R.append(eval(n))
                except BaseException:
                    raise Exception("Problème lors de l'importation")
            return R
    if isinstance(num, str):
        num = num.upper()
        c = ord(num) - ord('A')
        R = []
        for m1 in ch.split("\n"):
            m2 = m1.split(";")
            if len(m2) > c and m2[c] != '':
                try:
                    R.append(eval(m2[c].replace(' ', '').replace(',', '.')))
                except BaseException:
                    raise Exception("Problème lors de l'importation")
        return R


def liste2CSV(L, fichier='optionnel'):
    """
    Enregistre sous le nom ``fichier`` la liste ``L``.

    Si fichier n'est pas précisé, ouvre une boite de dialogue pour le choisir

    Arguments:
        L (list): Une liste
        fichier (file, optionnel): Le nom complet (avec le chemin) d'un fichier contenant du texte brut.
    """
    for i in range(len(L)):
        L[i] = str(L[i])
    chaine2fich("\n".join(L), fichier)


liste2CSV([1, 'a', 3, 'bonjour', 10, 'aurevoir'],
          fichier='TableurPourTest2.csv')


def trier(liste1, liste2=[]):
    """
    Retourne `liste1` triée.
    Si `liste2` est renseignée, elle est réorganisée de la même manière que `liste1`.
    Ex 1 : trier([5,3,4])=[3,4,5]

    Ex 2 : `liste1=[3,2,1]` et `liste2=[10,20,30]`.
    trier(liste1,liste2)=([1,2,3],[30,20,10])

    Arguments:
        liste1 (list) : Une liste avec UNIQUEMENT des nombres OU UNIQUMENT des chaines de caractères
        liste2 (list,optionnel) : Une liste quelconque mais de même taille que `liste1`
    """

    if liste2 == []:
        return sorted(liste1)
    if len(liste1) != len(liste2):
        print("Erreur : les 2 listes n'ont pas la même taille !")
    else:
        # Il faut trier la liste selon l'ordre de liste_groupe
        # On crée une matrice n x 2
        L = []
        for i in range(len(liste1)):
            L.append([liste1[i], liste2[i]])
        L.sort()
        return [i for i, j in L], [j for i, j in L]


def transposer(L):
    """
    L est une liste de liste, comme une matrice NxM. On prend la transposée.
    Ex : L=[[a,b,c],[1,2,3]]. Retourne la liste [[a,1],[b,2],[c,3]]

    Arguments:
        L (list) : une liste de listes
    """
    n = len(L[0])
    for i in range(len(L)):
        if n != len(L[i]):
            print("Les listes n'ont pas la même taille !")

    return list(map(list, zip(*L)))


def serie(deb, fin, pas=1):
    """
    Renvoie une liste de nombre (float) de `deb` à `fin` (inclu) avec un `pas`

    Arguments
        deb (float ou int) : début de la série
        fin (float ou int) : fin de la série
        pas (float ou int, optionnel) : pas de la série
    """
    l = [deb, fin, pas]
    degmax = 10**(-min([floor(log(abs(float(i)))) for i in l]))
    ToutEntier = [int(i * degmax) for i in l]
    return [float(i) / degmax for i in range(ToutEntier[0],
                                             ToutEntier[1] + ToutEntier[2], ToutEntier[2])]


def affiche_poly(L):  # Pourquoi???
    """
    Affiche la liste L sous forme d'un polynôme (L[n] étant le coefficient de degré n).

    Arguments:
        L (list): Une liste
    """
    poly = ""
    for i in range(len(L)):
        c = L[i]
        if c != 0 and poly != "":
            poly = poly + '+'
        if c != 0:
            if i > 0:
                if c == -1:
                    poly = poly + '-'
                if abs(c) != 1:
                    poly = poly + str(c)
            else:
                poly = poly + str(c)
            if i > 0:
                poly = poly + 'X'
                if i > 1:
                    poly = poly + '^' + str(i)
    if poly == "":
        poly = 0
    return poly
