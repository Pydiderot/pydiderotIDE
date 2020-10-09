"""
Partie chaines de caractères du module lycee.
Créé à partir d' Edupython: http://edupython.tuxfamily.org/

Licence CECILL http://www.cecill.info/
"""
import tkinter as Tk
import tkinter.filedialog as tkf
import builtins


def taille(objet):
    """
    Retourne la longueur de cette chaine ou de cettte liste.

    Arguments:
        objet (str ou list): Une chaine de caractères ou une liste.
    """
    return builtins.len(objet)


def fich2chaine(fichier='optionnel'):
    """
    Retourne chaine formée du contenu du fichier ``fichier``.

    Si ``fichier`` n'est pas précisé, ouvre une boite de dialogue pour le sélectionner.

    Arguments:
        fichier (file, optionnel): Nom complet (avec le chemin) d'un fichier contenant du texte brut.

    """
    if fichier == 'optionnel':
        fen = Tk.Tk()
        tex1 = Tk.Label(fen, text='Vous n''avez pas précisé de fichier')
        tex1.pack()
        fich = tkf.askopenfile(
            parent=fen,
            mode='rb',
            title="Choisissez un fichier")
        try:
            fen.destroy()
        except BaseException:
            pass
        if fich is not None:
            fichier = fich.name
    if fichier != 'optionnel':
        filin = open(fichier, 'r')
        chaine = "\n".join([line.strip() for line in filin])
        filin.close()
        return chaine
    else:
        return ""


def chaine2fich(ch, fichier='optionnel'):
    """
    Enregistre sous le nom ``fichier`` la chaine ``ch``.

    Si fichier n'est pas précisé, ouvre une boite de dialogue pour le sélectionner.

    Arguments:
        ch (str): Une chaine de caractères
        fichier (file, optionnel): Le nom complet (avec le chemnin) d'un fichier contenant du texte brut.
    """
    if fichier == 'optionnel':
        fen = Tk.Tk()
        tex1 = Tk.Label(fen, text='Vous n''avez pas précisé de fichier')
        tex1.pack()
        fich = tkf.asksaveasfile(
            parent=fen,
            mode='w',
            title="Choisissez un fichier")
        try:
            fen.destroy()
        except BaseException:
            pass
        if fich is not None:
            fichier = fich.name
    if fichier != 'optionnel':
        filout = open(fichier, 'w')
        filout.write(ch)
        filout.close()
        return True
    else:
        return False
