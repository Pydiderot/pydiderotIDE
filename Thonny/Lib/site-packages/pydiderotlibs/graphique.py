# -*- coding: utf-8 -*-
#

# import des librairies
from time import sleep  # pour rendre transparent côté élève l'utilisation de "sleep"
from random import randint #pour la fonction vecteur2 et pour cercle_aleatoire
from .detection_collision import *

import sys
import math
import pygame
from .couleurs import rgb

# Un petit message invitant a lire la doc
print("""
Merci d'utiliser la librairie graphique du module pydiderot.\n
N'hésitez pas à consulter la documentation en ligne:\n
https://pydiderotlibs.rtfd.io/librairies/graphique.html
""")

# On définit les variables globales.
# Si quelqu'un veut s'amuser à sous-classer pygame.Surface pour faire plus propre il est bienvenue
_axeMath = False
_fenetre = None
_autorefresh = True


def creer_fenetre(largeur=200, hauteur=300, orientation_axe_ordonnees=False, titre="Fenetre graphique", autorefresh=True):
    fenetre(largeur, hauteur, orientation_axe_ordonnees, titre)


def window(largeur=600, hauteur=500, orientation_axe_ordonnees=False, titre="Fenetre graphique", autorefresh=True):
    fenetre(largeur, hauteur, orientation_axe_ordonnees, titre)


def fenetre(
    largeur=600,
    hauteur=500,
    orientation_axe_ordonnees=False,
    titre="Fenetre graphique",
    autorefresh=True
    ):
    """
    Crée et affiche une fenêtre graphique.

    Alias: ``window()``, ``creer_fenetre()``

    Arguments:
        largeur (int, optionnel): Largeur de la fenetre en pixels (``600`` par défaut)
        hauteur (int, optionnel): Hauteur de la fenetre en pixels (``500`` par défaut)
        orientation_axe_ordonnees: Si on met cet argument à True, l'axe des ordonnées sera orienté de bas en haut comme en maths. Sinon il est orienté dans l'autre sens comme habituellement en informatique (``False`` par défaut)
        titre (str, optionnel): Titre de la fenetre (``Fenetre graphique`` par défaut)
        autorefresh(bool, optionnel): Active le rafraichissement automatique de la fenetre graphique (`False` par défaut)
    """

    pygame.init()
    global _fenetre
    global _axeMath
    global _autorefresh
    _axeMath = orientation_axe_ordonnees
    _autorefresh = autorefresh
    _fenetre = pygame.display.set_mode((largeur, hauteur))
    pygame.display.set_caption(titre)
    # active la répétition des touches
    pygame.key.set_repeat(1)
    _fenetre.fill(rgb('blanc'))
    pygame.display.update()

def _ordo(y):
    global _axeMath
    ymax = pygame.display.Info().current_h
    if _axeMath:
        return ymax-y
    return y

def rafraichir():
    """
    Rafraîchie la fenêtre graphique.
    C'est uniquement utile si vous désactivez l'option :ref:`autorefresh <autorefresh>`.
    """
    pygame.display.update()

def ecoute_evenements():
    return demande_evenements()


def events():
    return demande_evenements()


def demande_evenements():
    """
    Récupère les évenements pygame gère la fermeture de la fenetre et retourne les évenements formatés.

    Renvoie un dictionnaire d'évenements formaté comme suit:
    ``{'touche1': None, 'touche2':None, 'souris': [x,y], 'click': [x,y]}``

    Les valeurs ``None`` pour les touches peuvent surprendre mais il est nécéssaire d'utiliser un dictionnaire pour avoir les coordonnées
    éventuelles de la souris lors d'un click par exemple. Pour les touches clavier, l'importance est la présence de la cléf et la valeur associée est donc ``None``.

    - Les caractères alphanumériques sont encodés en ascii (``'a'``, ``'n'``, ``';'``) et, si présent, leur valeur est ``None``.
    - les touches spéciales ont les clefs ``'espace'``, ``'haut'``, ``'bas'``, ``'droite'``, ``'gauche'`` et, si présent, leur valeur est ``None``.
    - Un clic avec le bouton gauche de la souris ajoute une clef ``'clic'``. Sa valeur est une liste ``[x, y]`` des coordonnées de la souris.
    - Un déplacement de la souris ajoute une clef ``'souris'``. Sa valeur est une liste ``[x, y]`` des coordonnées de la souris.

    Alias: ``events()``, ``ecoute_evenements()``

    """

    # Initialisation du dictionnaire de sortie
    evenements = {}
    touches_speciales = {
        'up': 'haut',
        'down': 'bas',
        'left': 'gauche',
        'right': 'droite',
        'space': 'espace'
    }

    for event in pygame.event.get():
        # Gestion de la fermeture de la fenetre
        if event.type == pygame.QUIT:
            sys.exit()
        # Gestion des evenements souris
        elif event.type == pygame.MOUSEMOTION:
            evenements['souris'] = list(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            evenements['clic'] = list(event.pos)
    # Gestion des touches. pygame.KeyDown ne va pas gérer plusieurs touches enfoncées
    # https://www.pygame.org/docs/ref/key.html#pygame.key.get_pressed
    for index, enfoncee in enumerate(pygame.key.get_pressed()):
        if enfoncee:
            # On traduit les touches speciales
            if pygame.key.name(index) in touches_speciales:
                touche = touches_speciales[pygame.key.name(index)]
            else:
                touche = pygame.key.name(index)
            evenements[touche] = None

    return evenements


def efface(couleur='blanc'):
    """
    Efface l'écran.

    Arguments:
        couleur (:ref:`couleur <couleur>`, optionnel): Couleur de remplissage de l'écran (``'blanc'`` par défaut).
    """
    _fenetre.fill(rgb(couleur))
    if _autorefresh:
        pygame.display.update()


def erase(couleur='blanc'):
    efface(couleur)


def trace_cercle(x, y, couleur='bleu', rayon=50, epaisseur=0):
    cercle(x, y, couleur, rayon, epaisseur)


def circle(x, y, couleur='bleu', rayon=50, epaisseur=0):
    cercle(x, y, couleur, rayon, epaisseur)


def cercle(x, y, couleur='bleu', rayon=25, epaisseur=0):
    """
    Trace un cercle dans la fenetre graphique.

    Alias: ``circle()``, ``trace_cercle()``

    Arguments:
        x (int): Abscisse du centre du cercle
        y (int): Ordonnée du centre du cercle
        rayon (int, optionnel): Rayon du cercle (25 par défaut)
        epaisseur (int, optionnel): Epaisseur du cercle (``0`` par défaut). Si ``0``, le cercle sera rempli et apparaitra comme un disque.
        couleur (:ref:`couleur <couleur>`, optionnel): Couleur du cercle (bleu par défaut)
    """
    couleur = rgb(couleur)
    pygame.draw.circle(_fenetre, couleur, (x, _ordo(y)), rayon, epaisseur)
    if _autorefresh:
        pygame.display.update()


def trace_cercle_aleatoire(couleur='bleu', rayon=5, epaisseur=0):
    cercle_aleatoire(couleur, rayon, epaisseur)


def random_circle(couleur='bleu', rayon=5, epaisseur=0):
    cercle_aleatoire(couleur, rayon, epaisseur)
    
def randcircle(couleur='bleu', rayon=5, epaisseur=0):
    cercle_aleatoire(couleur, rayon, epaisseur)

def cercle_aleatoire(couleur='bleu', rayon=5, epaisseur=0):
    """
    Trace un (petit) cercle dans la fenetre graphique, à un endroit choisit au hasard.
    (Utile pour fairre de la neige par exemple.)

    Alias: ``random_circle()``, ``randcircle()``, ``trace_cercle_aleatoire()``

    Arguments:
        rayon (int, optionnel): Rayon du cercle (5 par défaut)
        epaisseur (int, optionnel): Epaisseur du cercle (``0`` par défaut). Si ``0``, le cercle sera rempli et apparaitra comme un disque.
        couleur (:ref:`couleur <couleur>`, optionnel): Couleur du cercle (bleu par défaut)
    """
    couleur = rgb(couleur)
    ymax = pygame.display.Info().current_h
    xmax = pygame.display.Info().current_w
    centre = (randint(-rayon, xmax + rayon),randint(-rayon, ymax + rayon))
    pygame.draw.circle(_fenetre, couleur, centre, rayon, epaisseur)
    if _autorefresh:
        pygame.display.update()


def trace_point(x, y, couleur='bleu'):
    point(x, y, couleur)


def point(x, y, couleur='bleu'):
    """
    Trace un point dans la fenetre graphique.

    Alias: ``trace_point()``

    Arguments:
        x (int): Abscisse du point
        y (int): Ordonnée du point
        couleur (:ref:`couleur <couleur>`, optionnel): Couleur du point (bleu par défaut)
    """
    couleur = rgb(couleur)
    pygame.draw.circle(_fenetre, couleur, (x, _ordo(y)), 1, 0)
    if _autorefresh:
        pygame.display.update()


def trace_rectangle(x, y, largeur=100, hauteur=50, couleur='bleu', epaisseur=0):
    rectangle(x, y, largeur, hauteur, couleur, epaisseur)


def rectangle(x, y, largeur=100, hauteur=50, couleur='bleu', epaisseur=0):
    """
    Trace un rectangle horizontal dans la fenetre graphique .

    Le sommet haut-gauche à pour coordonnées ``(x,y)``, la ``largeur`` est la taille en abscisse
    et la ``hauteur`` la taille en ordonnée.

    Alias: ``trace_rectangle()``

    Arguments:
        x (int): abscisse du sommet haut gauche du rectangle
        y (int): ordonnée du sommet haut gauche du rectangle
        largeur (int): taille du rectangle sur l'axe des abscisses
        hauteur (int): taille du rectangle sur l'axe des ordonnées
        couleur (:ref:`couleur <couleur>`, optionnel): Couleur du rectangle (``bleu`` par défaut)
        epaisseur (int, optionnel): Epaisseur des cotés du rectangle (``0`` par défaut). Si ``0``, le rectangle est rempli.

    """
    couleur = rgb(couleur)
    pygame.draw.rect(_fenetre, couleur, (x, _ordo(y), largeur, hauteur), epaisseur)
    if _autorefresh:
        pygame.display.update()


def trace_triangle(x1, y1, x2, y2, x3, y3, couleur='bleu', epaisseur=0):
    triangle(x1, y1, x2, y2, x3, y3, couleur, epaisseur)


def triangle(x1, y1, x2, y2, x3, y3, couleur='bleu', epaisseur=0):
    """
    Trace un triangle dans la fenetre graphique .

    Alias: ``trace_triangle()``

    Arguments:
        x1 (int): abscisse du premier sommet du triangle
        y1 (int): ordonnée du premier sommet du triangle
        x2 (int): abscisse du deuxième sommet du triangle
        y2 (int): ordonnée du deuxième sommet du triangle
        x3 (int): abscisse du troisième sommet du triangle
        y3 (int): ordonnée du troisième sommet du triangle
        couleur (:ref:`couleur <couleur>`, optionnel): Couleur du triangle (``bleu`` par défaut)
        epaisseur (int, optionnel): Epaisseur des cotés du triangle (``0`` par défaut). Si ``0``, le triangle est rempli.

    """
    couleur = rgb(couleur)
    pygame.draw.polygon(_fenetre, couleur, [(x1, _ordo(y1)), (x2, _ordo(y2)), (x3, _ordo(y3))], epaisseur)
    if _autorefresh:
        pygame.display.update()


def trace_segment(x1, y1, x2, y2, couleur='bleu', epaisseur=2):
    segment(x1, y1, x2, y2, couleur, epaisseur)


def segment(x1, y1, x2, y2, couleur='bleu', epaisseur=2):
    """
    Trace un segment entre les points de coordonées ``(x1, y1)`` et ``(x2, y2)``.

    Alias: ``trace_segment()``

    Arguments:
        x1 (int): abscisse de la première extremité du segment
        y1 (int): ordonnée de la première extremité du segment
        x2 (int): abscisse de la deuxieme extrémité du segment
        y2 (int): ordonnée de la deuxieme extrémité du segment
        couleur (:ref:`couleur <couleur>`, optionnel): Couleur du segment (``bleu`` par défaut)
        epaisseur (int, optionnel): Epaisseur du segment (``2`` par défaut)
    """
    couleur = rgb(couleur)
    pygame.draw.lines(_fenetre, couleur, False, [(x1, _ordo(y1)), (x2, _ordo(y2))], epaisseur)
    if _autorefresh:
        pygame.display.update()


def trace_vecteur(x, y, v, couleur='rouge', epaisseur=2):
    vecteur(x, y, v, couleur, epaisseur)


def vector(x, y, v, couleur='rouge', epaisseur=2):
    vecteur(x, y, v, couleur, epaisseur)


def vecteur(x, y, v, couleur='rouge', epaisseur=2):
    """
    Trace la représentation du vecteur ``v`` à partir du point d'origine ``(x, y)``.

    Alias: ``vector()``, ``trace_vecteur()``

    Arguments:
        x (int): abscisse du point d'origine de la représentation du vecteur
        y (int): ordonnée du point d'origine de la représentation du vecteur
        v (list): Coordonnées de la deuxieme extrémité du segment
        couleur (:ref:`couleur <couleur>`, optionnel): Couleur du segment (``rouge`` par défaut)
        epaisseur (int, optionnel): Epaisseur du segment (``2`` par défaut)
    """

    couleur = rgb(couleur)

    trace_segment(x, y, x + v[0], y + v[1], couleur, epaisseur)
    w1 = [0, 0]
    w2 = [0, 0]
    w1[0] = -.3 * math.cos(15 * math.pi / 180) * v[0] + .3 * math.sin(15 * math.pi / 180) * (-v[1])
    w1[1] = -.3 * math.cos(15 * math.pi / 180) * v[1] + .3 * math.sin(15 * math.pi / 180) * v[0]
    w2[0] = -.3 * math.cos(15 * math.pi / 180) * v[0] - .3 * math.sin(15 * math.pi / 180) * (-v[1])
    w2[1] = -.3 * math.cos(15 * math.pi / 180) * v[1] - .3 * math.sin(15 * math.pi / 180) * v[0]
    pygame.draw.polygon(
        _fenetre,
        couleur,
        [
            (x + v[0], _ordo(y + v[1])),
            (x + v[0] + w1[0], _ordo(y + v[1] + w1[1])),
            (x + v[0] + w2[0], _ordo(y + v[1] + w2[1])),
            (x + v[0], _ordo(y + v[1]))
        ],
        0
    )
    if _autorefresh:
        pygame.display.update()

def vecteur2(xv, yv, couleur='rouge', epaisseur=2):
    """
    Trace la représentation du vecteur de coordonnées ``(xv, yv)`` à partir d'une origine choisie au hasard.

    Alias: ``vector2()``, ``trace_vecteur2()``

    Arguments:
        xv (int): abscisse du vecteur
        yv (int): ordonnée du vecteur
        couleur (:ref:`couleur <couleur>`, optionnel): Couleur du segment (``rouge`` par défaut)
        epaisseur (int, optionnel): Epaisseur du segment (``2`` par défaut)
    """

    ymax = pygame.display.Info().current_h
    xmax = pygame.display.Info().current_w
    x = randint(xv, xmax - xv)
    y = randint(yv, ymax - yv)
    v = [xv, yv]
    vector(x, y, v, couleur, epaisseur)


def trace_vecteur2(xv, yv, couleur='rouge', epaisseur=2):
    vecteur2(xv, yv, couleur, epaisseur)


def vector2(xv, yv, couleur='rouge', epaisseur=2):
    vecteur2(xv, yv, couleur, epaisseur)


def trace_image(x, y, nom, largeur=100, hauteur=100):
    image(x, y, nom, largeur, hauteur)


def image(x, y, nom, largeur=100, hauteur=100):
    """
    Trace une image dans la fenetre graphique.

    Alias:``trace_image()``

    Arguments:
        x (int): Abscisse du centre de l'image
        y (int): Ordonnée du centre de l'image
        nom (str) : nom du fichier image (qui doit être dans le répertoire du script)
        largeur (int, optionnel): Largeur de l'image (100 par défaut)
        hauteur (int, optionnel): Hauteur de l'image (100 par défaut)
    """
    pygame_image = pygame.transform.scale(pygame.image.load(
        nom).convert_alpha(), (largeur, hauteur))
    _fenetre.blit(pygame_image, (int(x - largeur / 2), _ordo(int(y - hauteur / 2))))
    if _autorefresh:
        pygame.display.update()


def trace_explosion(x, y, couleur='orange', r=50, c=0.5, n=10):
    explosion(x, y, couleur, r, c, n)


def explosion(x, y, couleur='orange', r=25, c=0.5, n=10):
    '''
    Trace un polygône régulier étoilé à ``2n`` côté,
    de rayon extérieur ``r``,
    et tel que le rayon intérieur est égal à ``c*r``
    (pour ``c=0``, le polygône est réduit à ``n`` rayons du cencle de rayon ``r``
    pour ``c=1``, c'est un polygône régulier à ``2n`` côtés)

    Alias: ``trace_explosion()``

    Arguments:
        x (int): Abscisse du centre de l'explosion
        y (int): Ordonnée du centre de l'explosion
        couleur (:ref:`couleur <couleur>`, optionnel): Couleur (``orange`` par défaut)
        r (int): Rayon extérieur
        c (float):Coefficient pour obtenir le rayon intérieur égal à ``c*r``
        n (int): Nombre de sommets
    '''
    couleur = rgb(couleur)
    pointlist = []
    theta = 2 * math.pi / n
    for k in range(n):
        pointlist.append((
            x + r * math.cos(k * theta),
            _ordo(y + r * math.sin(k * theta))
        ))
        pointlist.append((
            x + c * r * math.cos((k + 1 / 2) * theta),
            _ordo(y + c * r * math.sin((k + 1 / 2) * theta))
        ))
    pointlist.append((x + r, _ordo(y)))
    pygame.draw.polygon(_fenetre, couleur, pointlist)
    if _autorefresh:
        pygame.display.update()


def trace_axes(color='noir'):
    axes(color)


def axes(color='noir'):
    '''
    Dessine les axes de coordonnées pour une meilleure compréhension par les élèves.

    Alias: ``trace_axes()``
    '''
    couleur = rgb(color)
    ymax = pygame.display.Info().current_h
    xmax = pygame.display.Info().current_w
    epaisseur = 2
    correction = 0
    if _axeMath:
        ## cette correction vient du fait que les textes continuent d'être définis par rapport à leur coin haut-gauche même si l'axe est à l'envers
        correction = 12
    pygame.draw.lines(_fenetre, couleur, False, [(5, _ordo(0)), (5, _ordo(ymax))], epaisseur)
    pygame.draw.lines(
        _fenetre, couleur, False, [
            (0, _ordo(ymax - 5)), (5, _ordo(ymax))], epaisseur)
    pygame.draw.lines(
        _fenetre, couleur, False, [
            (10, _ordo(ymax - 5)), (5, _ordo(ymax))], epaisseur)
    pygame.draw.lines(_fenetre, couleur, False, [(0, _ordo(5)), (xmax, _ordo(5))], epaisseur)
    pygame.draw.lines(
        _fenetre, couleur, False, [
            (xmax - 5, _ordo(0)), (xmax, _ordo(5))], epaisseur)
    pygame.draw.lines(
        _fenetre, couleur, False, [
            (xmax - 5, _ordo(10)), (xmax, _ordo(5))], epaisseur)
    font = pygame.font.Font(None, 24, bold=False, italic=False)
    text = font.render(str(ymax), 1, couleur)
    _fenetre.blit(text, (15, _ordo(ymax - 35 + correction)))
    text = font.render("y", 1, couleur)
    _fenetre.blit(text, (15, _ordo(ymax - 17 + correction)))
    text = font.render(str(xmax), 1, couleur)
    _fenetre.blit(text, (xmax - 35, _ordo(10 + correction)))
    text = font.render("x", 1, couleur)
    _fenetre.blit(text, (xmax - 15, _ordo(25 + correction)))
    text = font.render("0", 1, couleur)
    _fenetre.blit(text, (10, _ordo(10 + correction)))
    if _autorefresh:
        pygame.display.update()

# Gestion du texte.
# voir https://nerdparadise.com/programming/pygame/part5

# On stocke les polices dans une globale pour ne pas avoir à la regénérer à chaque affichage.
_cached_fonts = {}
# On stocke les textes sous forme d'images pour ne pas avoir à la regénérer à chaque affichage.
# Un meme texte a de grande chance d'être affiché plusieurs fois.
_cached_text = {}

def _make_font(fonts, size):
    """
    Initialise une police de caractères à partir d'une liste.
    On retourne la première police de la liste installée sur la machine.
    Si aucune police n'est installée, on retourne la police systeme par défaut.

    Arguments:
        fonts(list): Liste de polices de caractères
        size(int): Taille de la police de caractère

    Returns:
        la première police de la liste installée sur la machine de taille ``size``.
    """
    available = pygame.font.get_fonts()
    # get_fonts() returns a list of lowercase spaceless font names
    choices = map(lambda x:x.lower().replace(' ', ''), fonts)
    for choice in choices:
        if choice in available:
            return pygame.font.SysFont(choice, size)
    return pygame.font.Font(None, size)


def _get_font(font_preferences, size):
    """
    Retourne une police de caractère dans la liste ``font_preferences`` de taille ``size``
    Si la police a déja été utilisée on utilise la cache ``_cached_fonts``.
    """
    global _cached_fonts
    key = str(font_preferences) + '|' + str(size)
    font = _cached_fonts.get(key, None)
    if font is None:
        font = _make_font(font_preferences, size)
        _cached_fonts[key] = font
    return font

def _create_text(text, fonts, size, color):
    global _cached_text
    key = '|'.join(map(str, (fonts, size, color, text)))
    text_image = _cached_text.get(key, None)
    if text_image is None:
        font = _get_font(fonts, size)
        text_image = font.render(text, True, color)
        _cached_text[key] = text_image
    return text_image


def texte(message, x, y, police='', taille=12, couleur="noir"):
    """
    Affiche un texte dans la fenetre graphique.

    Arguments:
        message(str): le texte à afficher
        x(int): abscisse du début du texte
        y(int): ordonnée du haut du début du texte
        police(str, optionnel): la police de caractère à utiliser. Si non renseigné ou si la police n'est pas installée, on utilise la police de caractère défaut du system
        taille(int, optionnel): taille du texte
        couleur(:ref:`couleur <couleur>`, optionnel): couleur du texte
    """
    texte_image = _create_text(message, [police], taille, rgb(couleur))
    pygame.display.get_surface().blit(texte_image, (x, y))
    if _autorefresh:
        pygame.display.update()

def polices_disponibles():
    """
    Retourne les polices caractères disponibles
    """
    return pygame.font.get_fonts()

def test_police(police):
    """
    Test si une police de caractère est installée.

    Arguments:
        police(str): police de caractère à tester

    Returns:
        True si la police est installée, False sinon
    """
    return police.lower().replace(' ', '') in polices_disponibles()
