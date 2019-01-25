# -*- coding: utf-8 -*-
#

"""
Partie fonctions fonctions_usuelles du module lycee.
"""
"""
Créé à partir d' Edupython: http://edupython.tuxfamily.org/

Licence CECILL http://www.cecill.info/
"""

import math


def puissance(a, n):  # il faut ajouter la fonction carre -> vraiment? a*a est simple
    """
    Renvoie le nombre réel (float) \(a^n\).

    Arguments:
        a (float): un nombre décimal.
        b (float): un nombre décimal représentant l'exposant.

    """
    return a**n

def carre(a): # parce que...
    """
    Renvoie le carre d'un nombre reel (float)

    Arguments:
        a (float): un nombre décimal.

    """
    return a*a


def racine(x):
    """
    Renvoie le nombre réel (float) racine carré de ``x`` \(\sqrt{x}\).

    Arguments:
        a (float): un nombre décimal.
        b (float): un nombre décimal représentant l'exposant.
    """
    return math.sqrt(x)


def factoriel(n):  # Dans quel programme de lycée ?
    """
    Renvoie \(n! = n x (n-1) x ... x 3 x 2 x 1\)

    Arguments:
        n (int): Un nombre entier positif.
    """
    return math.factorial(n)


def partie_entiere(x):  # Utilité ? Concept de la partie entière difficile au lycée pour les nombres négatifs. Faire une fonction pour prendre la partie sans la virgule ?
    """
    Renvoie la partie entiere du nombre ``x``, c'est a dire le plus grand entier inferieur au reel ``x``.

    Arguments:
        x (float): Un nombre décimal.

    """
    return math.floor(x)

def sans_virgule(x):
    """
    Retourne la partie du nombre x sans sa partie décimale. Ex : -2.5 devient -2

    Arguments:
        x (float): Un nombre decimal.

    """
    return int(x)


def exp(x):
    """
    Renvoie l'image du nombre ``x`` par la fonction exponentielle: \(e^x\).

    Arguments:
        x (float): Un nombre decimal.
    """
    return math.exp(x)


def ln(x):
    """
    Renvoie l'image du nombre ``x`` par la fonction logarithme népérien: \(\ln x \).

    Arguments:
        x (float): Un nombre décimal strictement positif.
    """
    return math.log(x)

def log(x):
    """
    Renvoie l'image du nombre ``x`` par la fonction logarithme décimal: \(\log x \).

    Arguments:
        x (float): Un nombre décimal strictement positif.
    """
    return math.log10(x)
