# -*- coding: utf-8 -*-
"""
Partie statistiques et probobilité du module lycee.
"""
"""
Créé à partir d' Edupython: http://edupython.tuxfamily.org/

Licence CECILL http://www.cecill.info/
"""


# Loi Binomial




import math
import builtins
import random
from .arithmetique import quotient
from .listes import transposer
def binomial(n, p):
    """
    Renvoie un entier (int) représentant le coefficient binomial ``p`` parmi ``n``.

    C'est à dire le nombre de chemins de l’arbre réalisant ``p`` succès pour ``n`` répétitions.

    Arguments:
        n (int): Un nombre entier
        p (int): Un nombre entier
    """
    if p <= n:
        return quotient(
            math.factorial(n),
            math.factorial(n - p) * math.factorial(p)
        )
    else:
        return 0


def tirage_binomial(n, p):
    """
    Renvoie un nombre entier (int) choisi de manière aléatoire selon une loi binomiale B(n,p) : ``p`` parmi ``ǹ``.

    Arguments:
        n (int): Premier paramètre de la loi binomiale à simuler.
        p (int): Second paramètre de la loi binomiale à simuler.
    """
    s = 0
    for i in range(n):
        if alea() < p:
            s = s + 1
    return s

# Loi uniforme


def alea_entier(min, max):
    """
    Renvoie un entier (int) choisi de manière (pseudo)aléatoire et équiprobable
    dans l'intervalle [``min`` ; ``max``].

    Arguments:
        min (int): Un nombre entier
        max (int): Un nombre entier
    """
    return random.randint(min, max)


def tirage_uniforme(min, max):
    """
    Renvoie un nombre décimal (float) choisi de manière (pseudo)aléatoire et uniforme
    de l'intervalle \[``min`` ; ``max``\[.

    Arguments:
        min (float): Un nombre réel.
        max (float): Un nombre réel.

    """
    return random.uniform(min, max)


def choix(liste):
    """
    Renvoie un élément de la liste ``liste`` choisi (pseudo)aléatoirement et de manière équipropable

    Arguments:
        liste (int): La liste dans laquelle on choisit un élément.
    """
    return random.choice(liste)


def alea():
    """
    Renvoie au hasard un décimal de l'intervalle [0 ; 1[
    """
    return random.random()

# Loi exponentielle


def tirage_expo(x):
    """
    Renvoie un nombre décimal (float) choisi de manière aléatoire selon
    une loi exponentielle de paramètre ``x``.

    Arguments:
        x (float) : est un réel strictement positif.
    """
    return random.expovariate(x)

# Loi normale


def tirage_normale(mu, sigma):
    """
    Renvoie un nombre décimal (float) choisi de manière aléatoire
    selon une loi nomale d'espérance ``mu`` et d'écart type ``sigma``.

    Arguments:
        mu (float): Un nombre décimal. L'éspérance de la loi normale
        sigma (float): Un nombre décimal. L'écart type de la loi normale
    """
    return random.gauss(mu, sigma)


def tirage_gauss(mu, sigma):
    """
    Renvoie un nombre décimal (float) choisi de manière aléatoire
    selon une loi nomale d'espérance ``mu`` et d'écart type ``sigma``.

    Arguments:
        mu (float): Un nombre décimal. L'éspérance de la loi normale
        sigma (float): Un nombre décimal. L'écart type de la loi normale
    """
    return random.gauss(mu, sigma)


def compte(liste_critere, liste_effectif=[]):
    """
    Retourne la liste non triée, sans les doublons, les effectifs, les fréquences correspondantes et l'effectifs totales.
    La fonctionne NE TRIE PAS par ordre des critères : les critères n'ont pas nécessairement un ordre.
    Pour trier le résultat, utililser la fonctions trier()

    Arguments:
        liste_critere (list): une liste de critère d'une population
        liste_effectif (list, optionnel) : liste des frequences ou des effectifs des critères
    """
    n = len(liste_critere)
    eff_tot = 0
    leff = []
    if liste_effectif == []:  # On crée la liste des effectifs si elle n'existe pas, 1 par critère
        leff = [1] * n
    elif liste_effectif != [] and len(liste_effectif) != n:
        print("Erreur : les 2 listes n'ont pas le même nombre déléments !")
    else:
        leff = liste_effectif

    critere_groupe = []
    eff_groupe = []
    for i in range(n):  # où l'on compte
        if liste_critere[i] not in critere_groupe:
            # Si le critere n'est pas dans la liste on le rajoute
            critere_groupe.append(liste_critere[i])
            # Et on ajoute l'effectif/frequence correspondante
            eff_groupe.append(leff[i])
            eff_tot += leff[i]
        else:
            # Si le critere est déjà présent on ajoute l'effectif/frequence à
            # celle déjà existante
            eff_groupe[critere_groupe.index(liste_critere[i])] += leff[i]
            eff_tot += leff[i]

    return [critere_groupe, eff_groupe, [
        float(i) / eff_tot for i in eff_groupe], eff_tot]


# Les classes
def centres(L):  # Pourquoi?
    """
    Renvoie une liste de longueur n-1 contenant les valeurs (L[i]+L[i+1])/2.

    Arguments:
        L (list): Une liste de taille n
    """
    R = []
    for i in range(len(L) - 1):
        R.append((L[i] + L[i + 1]) / 2)
    return R


def moyenne(xi, ni=[]):
    """
    Renvoie la moyenne de la liste ``xi``.

    Arguments:
        xi (list): liste de valeurs
        ni (liste, optionnel): série des effectifs ou des fréquences associés
    """
    L = compte(xi, ni)
    # Manipulation technique pour ne prendre que critere et freq de la serie
    # statistiques
    L1 = transposer(L[::2])
    # Et prendre la transposee
    m = 0
    for i, j in L1:
        m += i * j
    return m


def variance(xi, ni=[]):
    """
    Retourne la variance de la liste.

    Arguments:
        xi (list): Liste de valeurs
        ni (list, optionnel): Liste des effectifs associés
    """
    L = compte(xi, ni)
    m = moyenne(xi, ni)
    # Manipulation technique pour ne prendre que critere et freq de la serie
    # statistiques
    L1 = transposer(L[::2])
    # Et prendre la transposee
    v = 0
    for i, j in L1:
        v += (i - m)**2 * j
    return v


def ecartype(xi, ni=[]):
    """
    Retourne l'écart-type de la liste.

    Arguments:
        xi (list): Liste de valeurs
        ni (list, optionnel): Liste des effectifs associés
    """
    return math.sqrt(variance(xi, ni))
