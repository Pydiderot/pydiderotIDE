# -*- coding: utf-8 -*-
#
# Version 1.1
"""
Module avec les fonctions de la classe de Seconde 2018 pour le lycée diderot (marseille).
On prend comme fichier de départ le module de l'irem d'Amiens
http://download.tuxfamily.org/amienspython/lycee.py
Licence http://www.cecill.info/
"""


import math

from .arithmetique import *
from .trigo import *
from .stats_proba import *
from .fonctions_usuelles import *
from .vecteurs import *
from .chaines import *
from .listes import *

print("""
Merci d'utiliser la librairie lycee du module pydiderot.\n
N'hésitez pas à consulter la documentation en ligne:\n
https://pydiderotlibs.rtfd.io/librairies/lycee.html
""")

pi = math.pi


def repeter(f, n):
    """ 
    Appelle `n` fois la fonction ``f``.

    Alias disponible: ``repeat()``
    """
    for i in range(n):
        f()

def repeat(f, n):
    repeter(f, n)
    
