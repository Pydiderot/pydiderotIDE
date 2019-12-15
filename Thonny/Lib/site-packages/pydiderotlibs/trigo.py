"""
Partie trigonométrie du module lycee.
Deux familles de fonctions: ``_degré`` et ``_radian``.
"""

import math

"""
Créé à partir d' Edupython: http://edupython.tuxfamily.org/

Licence CECILL http://www.cecill.info/
"""


def cos_radian(angle):
    """
    Renvoie le cosinus de l'angle.

    Arguments:
        angle (float): La mesure d'un angle en radians
    """
    return math.cos(angle)


def sin_radian(angle):
    """
    Renvoie le sinus de l'angle.

    Arguments:
        angle (float): La mesure d'un angle en radians
    """
    return math.sin(angle)


def tan_radian(angle):
    """
    Renvoie la tangente de l'angle.

    Arguments:
        angle (float): La mesure d'un angle en radians
    """
    return math.tan(angle)


def acos_radian(x):
    """
    Renvoie un angle en radians dont le cosinus vaut ``x``.

    Arguments:
        x (float): Un nombre entre -1 et 1
    """
    return math.acos(x)


def asin_radian(x):
    """
    Retourne un angle en radians dont le sinus vaut ``x``.

    Arguments:
        x (float): Un nombre entre -1 et 1
    """
    return math.asin(x)


def atan_radian(x):
    """
    Renvoie un angle en radians dont la tangente vaut ``x``.

    Arguments:
        x (float): Un nombre entre -1 et 1
    """
    return math.atan(x)


def cos_degre(angle):
    """
    Renvoie le cosinus de l'angle (type``float``).

    Arguments:
        angle (float): La mesure d'un angle en degré
    """
    return math.cos(math.radians(angle))


def sin_degre(angle):
    """
    Renvoie le sinus de l'angle (type``float``).

    Arguments:
        angle (float): La mesure d'un angle en degré
    """
    return math.sin(math.radians(angle))


def tan_degre(angle):
    """
    Renvoie la tangente de l'angle (type``float``).

    Arguments:
        angle (float): La mesure d'un angle en degré.
    """
    return math.tan(math.radians(angle))


def acos_degre(x):
    """
    Renvoie un angle en degré (float) dont le cosinus vaut ``x``.

    Arguments:
        x (float): Un nombre réel
    """
    return math.degrees(math.acos(x))


def asin_degre(x):
    """
    Renvoie un angle en degrés (foat) dont le sinus vaut ``x``.

    Arguments:
        x (float): Un nombre réel
    """
    return math.degrees(math.asin(x))


def atan_degre(x):
    """
    Renvoie un angle en degrés (foat) dont le sinus vaut ``x``.

    Arguments:
        x (float): un nombre réel
    """
    return math.degrees(math.atan(x))
