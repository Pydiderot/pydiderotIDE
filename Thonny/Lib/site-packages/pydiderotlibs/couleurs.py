# -*- coding: utf-8 -*-
"""
Gestion des couleurs en Francais.

Permet la conversion francais -> rgb <-> hexadécimal.
Utilisé par les librairies repere et graphique

Notre fonction principale rgb(c) retourne un tuple RGB.
En gros on accepte un str du type "rouge", un str en hexadécimal ou un tuple RGB et on sort un RGB.

L'utilisateur peut ensuite choisir de le convertir en hexadécimal avec rgb2hex si besoin.

Licence MIT.
"""
#pour randcolor :
from random import randint

_couleurs = {
    'noir': (0, 0, 0),
    'blanc': (255, 255, 255),
    'gris': (128, 128, 128),
    'rouge': (255, 0, 0),
    'vert': (0, 255, 0),
    'bleu': (0, 0, 255),
    'jaune': (255, 255, 0),
    'rose': (253, 108, 158),
    'violet': (102, 0, 153),
    'cyan': (0, 255, 255),
    'magenta': (255, 0, 255),
    'orange': (255, 165, 0),
}

_colors = {
    'black': 'noir',
    'white': 'blanc',
    'grey': 'gris',
    'red': 'rouge',
    'green': 'vert',
    'blue': 'bleu',
    'yellow': 'jaune',
    'pink': 'rose',
    'purple': 'violet'
}

def rgb2hex(rgb):
    """
    Convertit un tuple RGB en hexadécimal
    """
    return '#%02x%02x%02x' % rgb


def hex2rgb(hex):
    """
    Convertit une coulur hexadécimale en tuple RGB
    """
    h = hex.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rgb(c):
    """
    On formate une couleur en RGB.

    Arguments:
        c (str ou tuple): Couleur sous la form "rouge", hexa ou rgb

    Returns:
        Tuple RGB.
    """

    if isinstance(c, tuple):
        return c
    elif isinstance(c, str):
        # on a un str
        if c.startswith("#"):
            # On a un format hexadécimal
            return hex2rgb(c)
        if c.lower() in _couleurs:
            # on a une couleur
            return _couleurs[c]
        if c.lower() in _colors:
            # on a une couleur en anglais
            return _couleurs[_colors[c]]
    # Au pire, on retourne c et on récupérera une erreur tkinter ou pygame
    return c

def randcolor():
    """
    Choix aléatoire d'une couleur en RGB.
    Returns:
        Tuple RGB.
        
    Alias: ``alea_couleur()``, ``random_color()``

    """
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    
    return (r,g,b)

def alea_couleur():
    randcolor()
    
def random_color():
    randcolor()
