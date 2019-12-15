# -*- coding: utf-8 -*-
#
"""
Partie vecteurs du module lycee.
"""

from math import sqrt

"""
Créé à partir d' Edupython: http://edupython.tuxfamily.org/

Licence CECILL http://www.cecill.info/
"""

def vecteur(x, y, z=None):
    """
    Renvoie un vecteur de coordonées ``(x,y)`` ou ``(x,y,z)``.

    Arguments:
        x (float): Abscisse du vecteur
        y (float): Ordonnée du vecteur
        z (float, optionnel): Cote du vecteur.

    """
    if z is None:
        return [x, y]
    return [x, y, z]


def norme(v):
    """
    Renvoie la norme du vecteur ``v``.

    Arguments:
        v (array): Un vecteur du plan ou de l'espace
    """

    n = 0
    for i in v:
        n = n + i * i
    return sqrt(n)


def abscisse(v):
    """
    Renvoie l'abscisse du vecteur ``v``.
        Arguments:
            v (array): Un vecteur du plan ou de l'espace
    """
    return v[0]


def ordonnee(v):
    """
    Renvoie l'ordonnée du vecteur ``v``.

    Arguments:
        v (array): Un vecteur du plan ou de l'espace
    """
    return v[1]


def cote(v):
    """
    Renvoie la cote du vecteur ``v``.

    Arguments:
        v (array): Un vecteur de l'espace
    """
    return v[2]
