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

_couleurs = {
    'noir': (0, 0, 0),
    'blanc': (255, 255, 255),
    'gris': (128, 128, 128),
    'rouge': (255, 0, 0),
    'vert': (0, 255, 0),
    'bleu': (0, 0, 255),
    'jaune': (255, 255, 0),
    'cyan':  (0, 255, 255),
    'magenta':(255, 0, 255),
    'orange': (255, 165, 0),
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
    return tuple(int(h[i:i+2], 16) for i in (0, 2 ,4))

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
        if c.startswith("#"):
            # On a un format hexadécimal
            return hex2rgb(c)
        if c.lower() in _couleurs:
            # on a un str
            return _couleurs[c]
    # Au pire, on retourne c et on récupérera une erreur tkinter ou pygame
    return c
