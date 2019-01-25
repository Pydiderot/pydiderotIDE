# -*- coding: utf-8 -*-

import tkinter as tk

def demander_texte(titre="Entrez un texte", message=None):
    """
    Ouvre une fenêtre avec le titre "titre" et attend une chaine de caractères.

    Arguments:
        titre (str, optionel): Le titre de la fenetre (``"Entrez un texte"`` par défaut).
        message (str, optionel): Si présente, on ajoute un champ de texte contenant ``message``.

    Returns:
        La chaine de caractère (type ``str``) entrée par l'utilisateur.
    """
    def _sauver_valeur(event=None):#la fonction sauve la valeur dans value et ferme la fenetre
        value.set(entree.get())
        fenetre.destroy()

    fenetre = tk.Tk()
    fenetre.title(titre)

    # Si message est entré, on ajoute un champ message.
    # permet par exemple l'affichage d'érreurs.
    if message is not None:
        label = tk.Label(fenetre, text = message)
        label.pack()

    value = tk.StringVar()

    entree = tk.Entry(fenetre, textvariable=value, width=50)
    entree.pack()
    # la touche retour appelle _sauver_valeur
    entree.bind('<Key-Return>', _sauver_valeur)
    # Donne le focus à la fenetre et au widget entree
    # Peut-etre focus_set serait plus poli?
    # http://tkinter.fdex.eu/doc/uwm.html#focus_set
    # http://tkinter.fdex.eu/doc/uwm.html#focus_force
    entree.focus_force()

    bouton=tk.Button(fenetre,text='Valider',command=_sauver_valeur)
    bouton.pack()

    fenetre.mainloop()
    return value.get()

def demander_reel(titre="Entrez un nombre réel"):
    """Ouvre une fenetre et attend un nombre réel.

    Si ce n'est pas un nombre réel, on repose la question en ajoutant un message d'erreur.

    Arguments:
        titre (str, optionel): Titre de la fenetre (``"Entrez un nombre réel"`` par défaut).

    Returns:
        Le nombre réel entré par l'utilisateur (type ``float``).
    """
    message = None
    while True:
        texte = demander_texte(titre, message)
        try:
            reel = float(texte)
        except ValueError:
            message = "La donnée est incorrecte. Ce n'est pas un nombre"
            continue
        else:
            break
    return reel

def demander_entier(titre="Entrez un nombre entier"):
    """Ouvre une fenetre et attend un nombre entier.

    Si ce n'est pas un nombre entier, on repose la question en ajoutant un message d'erreur.

    Arguments:
        titre (str, optionel): Titre de la fenêtre (``"Entrez un nombre entier"`` par défaut).

    Returns:
        Le nombre entier entré par l'utilisateur (type ``float``).
    """
    message = None
    while True:
        texte = demander_texte(titre, message)
        try:
            entier = int(texte)
        except ValueError:
            message = "La donnée est incorrecte. Ce n'est pas un nombre ENTIER"
            continue
        else:
            break
    return entier
