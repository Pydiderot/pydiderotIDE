"""
Ce module a ete ecrit par Olivier Brebant en aout 2011.

On peut l'utiliser librement sous licence MIT
"""

from tkinter import *
from math import floor
from couleurs import rgb, rgb2hex
global fenetre

class _Fenetre_graphique(Canvas):
    " Un canvas redimensionnable, avec repère usuel, zoomable... "
    # les coordonnées en pixels sont à l'intérieur du canvas (sans le bord)
    # R1 : repère lié aux pixels, B1 sa base associée
    # R2 : repère lié aux unités, B2 sa base associée

    def __init__(self, boss= None, largeur=400, hauteur=300,
                 xmin=-10, ymin=-10, xmax=10, ymax=10,
                 background='white', axes = True):
        Canvas.__init__(self,boss)
        self.configure(width=largeur, height=hauteur,
                       bg = background, border =5, relief=RIDGE)

        self.axes = axes
        self.xmin, self.ymin, self.xmax, self.ymax = xmin, ymin, xmax, ymax
        self.largeur = largeur #int(self.cget('width'))
        self.hauteur = hauteur #int(self.cget('height'))
        self.o2, self.p, self.inv_p = self._initialize_matrix(xmin,ymin,xmax,ymax,largeur,hauteur)
        self.pasU = self._reglage_pas()
        self.flag = 0           # pas de déplacement d'objets au départ
        border_w = self.winfo_reqwidth()-self.largeur   # largeur intérieure
        border_h = self.winfo_reqheight()-self.hauteur  # hauteur intérieure
        self.border=(border_w/2,border_h/2)             # taille du bord

        self.objets = []    # où l'on stocke les différents objets dessinés pour la réactualisation:
                            # [ tag, nature, xmin, ymin, xmax, ymax, couleur, epaisseur, remplissage ]
        self.redraw()

        self.bind('<Configure>', self._config)
        self.bind('<Button-1>', self.mouseDown)
        boss.bind('<Double-Button-1>', self.dblclic)
        self.bind('<Button1-Motion>', self.mouseMove)
        self.bind('<Button1-ButtonRelease>', self.mouseUp)
        self.bind('<Button-4>', self.wheel)  # roulette pour linux
        self.bind('<Button-5>', self.wheel)  # roulette pour linux
        boss.bind('<MouseWheel>', self.wheel) # pour windows
        self.master.protocol("WM_DELETE_WINDOW",self.fermeture)


    def _initialize_matrix(self,xmin,ymin,xmax,ymax,larg,haut):
        " initialise les matrices O2, P et inv_P "

        o2=[xmin*larg/(xmin-xmax),ymax*haut/(ymax-ymin)]      # coordonnées de O2 dans R1

        p = [[larg/(xmax-xmin),0],[0,haut/(ymin-ymax)]]        # matrice de passage de B1  à B2
        inv_p = [[(xmax-xmin)/larg,0],[0,(ymin-ymax)/haut]]    # matrice de passage de B2 à B1
        return o2,p,inv_p

    def _reglage_pas(self,pix=50,mult=2):
        # 50 pour environ tous les 50 pix, et 5 pour tous les k*5 unités
        cx = mult*floor(pix/mult/self.p[0][0]+0.5)
        cx = max(1,cx)
        cy = mult*floor(pix/mult/abs(self.p[1][1])+0.5)
        cy = max(1,cy)
        return (cx,cy)

    def inside(self, pt, zone):
        " décide si pt (2-tuple) est dans zone (4-tuple) "
        xmin, xmax = min(zone[0],zone[2]), max(zone[0],zone[2])
        ymin, ymax = min(zone[1],zone[3]), max(zone[1],zone[3])
        if pt[0]>xmin and pt[0]<xmax and pt[1]>ymin and pt[1]<ymax :
            return 1
        else :
            return 0

    def mouseDown(self, event):
        "Op. à effectuer quand le bouton gauche de la souris est enfoncé"
        # event.x et event.y contiennent les coordonnées du clic effectué (avec le bord !):
        self.x1, self.y1 = event.x-self.border[0], event.y-self.border[1] # on enlève le bord...

        zone_axeX = (0,self.o2[1]-20,self.largeur,self.o2[1]+20)
        zone_axeY = (self.o2[0]-20,0,self.o2[0]+20,self.hauteur)
        if self.axes:
            if self.inside((self.x1,self.y1),zone_axeX) :
                self.flag = 1       # drapeau de déplacement de l'axe X
            elif self.inside((self.x1,self.y1),zone_axeY):
                self.flag = 2       # drapeau de déplacement de l'ace Y
            else:
                self.flag = 3       # on déplace tout le repère
        else:
            self.flag = 3

    def dblclic(self,event):
        "Rend le repère orthonormé en se basant sur l'axe des X"
        self.p[1][1] = -self.p[0][0]
        self.inv_p[1][1] = 1/self.p[1][1]
        self._rafraichir()
        self.pasU = self._reglage_pas()
        self.redraw()

    def mouseMove(self, event):
        "Op. à effectuer quand la souris se déplace, bouton gauche enfoncé"
        x2,y2 = event.x-self.border[0], event.y-self.border[1]
        dx,dy = x2 - self.x1, y2 - self.y1

        if self.flag==1:
            self.translate(dx,0)

        elif self.flag==2:
            self.translate(0,dy)

        elif self.flag==3:
            self.translate(dx,dy)

        self.x1, self.y1 = x2, y2
        self.redraw()

    def mouseUp(self, event):
        "Op. à effectuer quand le bouton gauche de la souris est relâché"
        self.flag = 0

    def wheel(self,event):
        " Gestion du zoom sur action de la roulette " # attention ne fonctionne que sous Linux
        # event.num == 4 : roulette vers le haut
        # event.num == 5 : roulette vers le bas
        x,y = event.x-self.border[0], event.y-self.border[1] # x et y sont les coord. du clic a l'int. du canvas
        if event.num == 4 or event.delta>0:     # Zoom de +-10%
            zoom = 0.9
        else:
            zoom = 1.1
        zx = zy = zoom
        if (event.state == 20):  # si on appuie sur "Control" avec la roulette
            x , y = self.o2[0],self.o2[1]
        elif self.axes :
            if self.inside((x,y),(self.o2[0]-10,self.o2[1]-10,self.o2[0]+10,self.o2[1]+10)): # roulette proche du centre
                x,y = self.o2[0],self.o2[1]
            elif self.inside((x,y),(0,self.o2[1]-20,self.largeur,self.o2[1]+20)): # roulette sur l'axe des X
                zy = 1 # on bloque sur Y
                y = self.o2[1] # centrage sur l'ordonnée
            elif self.inside((x,y),(self.o2[0]-20,0,self.o2[0]+20,self.hauteur)): # roulette sur l'axe des Y
                zx = 1 # on bloque X
                x = self.o2[0] # centrage sur l'ordonnée

        self.zoom(zx,zy,x,y)   # on ajuste l'homothétie de coef (zx, zy) centré en (x,y)
        self.redraw()

    def translate(self,dx,dy):
        self.o2[0] += dx
        self.o2[1] += dy
        self._rafraichir()

    def zoom(self,zx,zy,x,y):
        self.o2[0]=zx*(self.o2[0]-x)+x
        self.o2[1]=zy*(self.o2[1]-y)+y
        self.p[0][0] = self.p[0][0]*zx
        self.p[1][1] = self.p[1][1]*zy
        self.inv_p[0][0] = 1/self.p[0][0]
        self.inv_p[1][1] = 1/self.p[1][1]
        self._rafraichir()
        self.pasU = self._reglage_pas()

    def pix2coord(self,xp,yp):
        xu = self.inv_p[0][0]*(xp-self.o2[0])
        yu = self.inv_p[1][1]*(yp-self.o2[1])
        return (xu,yu)

    def coord2pix(self,xu,yu):
        xp = self.p[0][0]*xu+self.o2[0]
        yp = self.p[1][1]*yu+self.o2[1]
        return (xp,yp)

    def _conv(self,x,y,delta=(0,0)):  # ajoute le bord et un décalage éventuel (delta) aux coordonnées en pixels
        tmp = self.coord2pix(x,y)
        return (tmp[0]+self.border[0]+delta[0],tmp[1]+self.border[1]+delta[1])

    def _rafraichir(self):
        self.xmax, self .ymax = self.pix2coord(self.largeur,0)
        self.xmin, self. ymin = self.pix2coord(0,self.hauteur)

    def _config(self, event): # event contient la taille du canvas, bord compris
        self.largeur = event.width-self.border[0]*2
        self.hauteur = event.height-self.border[1]*2
        self._rafraichir()
        self.configure(width=self.largeur, height=self.hauteur) # on met à jour les variables de dimension
        self.redraw() #dessine_axes()

    def dessine_axes(self):

        # axe X
        self.delete('axeX')

        self.create_line(self._conv(self.xmin,0,(10,0)),self._conv(self.xmax,0,(-10,0)), tag='axeX',arrow=LAST)
        self.create_text(self._conv(self.xmax,0), tag='axeX', text='x', anchor=NE)

        # Affichage des graduations 'intelligentes'
        # recherche des valeurs de l'axe qui doivent être affichées dans la fenêtre
        i1 = int(-floor(-self.xmin-20*self.inv_p[0][0])/self.pasU[0])
        i2 = int(floor(self.xmax-20*self.inv_p[0][0])/self.pasU[0])+1
        for i in range(i1,i2):
            p = self._conv(i*self.pasU[0],0)
            self.create_line(p[0],p[1]-4,p[0],p[1]+4,tag='axeX')
            if i==0 :
                self.create_text(p[0]-4,p[1]+4, text=str(int(i*self.pasU[0])),
                                 font=("Helvetica","8"), anchor = NE, tag='axeX')
            else:
                 self.create_text(p[0],p[1]+4, text=str(int(i*self.pasU[0])),
                                  font=("Helvetica","8"), anchor = N, tag='axeX')

        # axe Y
        self.delete('axeY')
        self.create_line(self._conv(0,self.ymin,(0,-10)),self._conv(0,self.ymax,(0,10)), tag='axeY',arrow=LAST)
        self.create_text(self._conv(0,self.ymax), tag='axeY', text='y', anchor=NE)

        # Affichage des graduations 'intelligentes'
        # recherche des valeurs de l'axe qui doivent être affichées dans la fenêtre
        i1 = int(floor(self.ymin+20*self.inv_p[1][1])/self.pasU[1])+1
        i2 = int(floor(self.ymax-20*self.inv_p[1][1])/self.pasU[1])
        for i in range(i1,i2):
            p = self._conv(0,i*self.pasU[1])
            self.create_line(p[0]-4,p[1],p[0]+4,p[1],tag='axeY')
            if i!=0 :
                 self.create_text(p[0]-4,p[1], text=str(int(i*self.pasU[1])),
                                  font=("Helvetica","8"), anchor = E, tag='axeY')


    def redraw(self):
        if self.axes :
            self.dessine_axes()
        for i in range(len(self.objets)):
            self.delete(self.objets[i][0])
            if self.objets[i][1]=='segment' :
                self.objets[i][0] = self.create_line(self._conv(self.objets[i][2],self.objets[i][3]),
                             self._conv(self.objets[i][4],self.objets[i][5]),
                             fill=self.objets[i][6], width=self.objets[i][7])
            elif self.objets[i][1]=='rectangle':
                self.objets[i][0] = self.create_rectangle(self._conv(self.objets[i][2],self.objets[i][3]),
                             self._conv(self.objets[i][4],self.objets[i][5]),
                             outline =self.objets[i][6], width=self.objets[i][7], fill=self.objets[i][8])
            elif self.objets[i][1]=='point':
                coef = 2
                pt = self._conv(self.objets[i][2],self.objets[i][3])
                taille = self.objets[i][5]
                if self.objets[i][6]=='rond':
                    self.objets[i][0] = self.create_oval(pt[0]-coef*taille,pt[1]-coef*taille,
                                                         pt[0]+coef*taille,pt[1]+coef*taille,
                                                         outline='', fill = self.objets[i][4])
                elif self.objets[i][6]=='croix':
                    self.delete(self.objets[i][7])
                    self.objets[i][0] = self.create_line(pt[0]-coef*taille,pt[1]-coef*taille,
                                                         pt[0]+coef*taille,pt[1]+coef*taille,
                                                         fill = self.objets[i][4])
                    self.objets[i][7] = self.create_line(pt[0]-coef*taille,pt[1]+coef*taille,
                                                         pt[0]+coef*taille,pt[1]-coef*taille,
                                                         fill = self.objets[i][4])
            elif self.objets[i][1]=='texte':
                self.objets[i][0]= self.create_text(self._conv(self.objets[i][2],self.objets[i][3]),
                                                    text=self.objets[i][4],fill=self.objets[i][5])


    def fermeture(self): # pour fermer proprement l'application avec la croix...
        #self.master.quit()
        self.master.destroy()


    def _trace_point(self,tab):
        pt = self._conv(self.objets[i][2],self.objets[i][3])

        self.objets[i][0] = self.create_oval(pt[0]-coef*taille,pt[1]-coef*taille,
                                                  pt[0]+coef*taille,pt[1]+coef*taille,
                                                  outline='', fill = self.objets[i][4])
    def loop(self):
        self.master.mainloop()

################################## Fin de la classe _Fenetre_graphique ##############



def trace_point(x,y, couleur='noir', taille=1, forme='rond'):
    """Ajoute un point dans la fenetre graphique aux coordonees ``(x, y)``.

    Arguments:
        x (float): abscisse du point
        y (float): ordonnée du point
        couleur (`couleur <#couleurs>`_, optionel): couleur du point (``noir`` par défaut)
        taille (int, optionel): taille du point (``1`` par défaut)
        forme (str, optionel): forme du point: rond/croix (``'rond'`` par défaut)
    """

    couleur = rgb2hex(rgb(couleur))
    global fenetre
    coef=2
    pt = fenetre._conv(x,y)
    tab = [0]*8
    if forme == 'rond':
        tab[0] = fenetre.create_oval(pt[0]-coef*taille,pt[1]-coef*taille,
                                  pt[0]+coef*taille,pt[1]+coef*taille,
                                  outline='', fill = couleur)
    elif forme == 'croix':
        tab[0] = fenetre.create_line(pt[0]-coef*taille,pt[1]-coef*taille,
                                  pt[0]+coef*taille,pt[1]+coef*taille,
                                  fill = couleur)
        tab[7] = fenetre.create_line(pt[0]-coef*taille,pt[1]+coef*taille,
                                  pt[0]+coef*taille,pt[1]-coef*taille,
                                  fill = couleur)

    tab[1] = 'point'
    tab[2] = x
    tab[3] = y
    tab[4] = couleur
    tab[5] = taille
    tab[6] = forme
    fenetre.objets.append(tab)

def trace_texte(x, y, texte, couleur='noir'):
    """Trace un texte dans la fenêtre graphique au coordonées ``x, y``.

    Arguments:
        x (float): abscisse du point
        y (float): ordonnée du point
        texte (str): Texte à placer dans la fenêtre graphique
        couleur (`couleur <#couleurs>`_, optionel): Couleur du texte (``noir`` par défaut)

    """
    couleur = rgb2hex(rgb(couleur))

    global fenetre
    tab = [0]*6
    tab[0] = fenetre.create_text(x,y,text=texte,fill = couleur)
    tab[1] = 'texte'
    tab[2] = x
    tab[3] = y
    tab[4] = texte
    tab[5] = couleur
    fenetre.objets.append(tab)

def trace_segment(x1, y1, x2, y2, couleur='noir', taille=2):
    """Trace un segment entre les points de coordonées ``(x1, y1)`` et ``(x2, y2)``.

    Arguments:
        x1,y1,x2,y2 (float): Coordonées des extrémités du segment.
        couleur (`couleur <#couleurs>`_, optionel): Couleur du segment (``noir`` par défaut).
        taille (int, optionl): Epaisseur du segment (``2`` par défaut).
        """
    couleur = rgb2hex(rgb(couleur))

    global fenetre

    tab = [0]*8
    tab[0] = fenetre.create_line(fenetre._conv(x1,y1),fenetre._conv(x2,y2),width=taille, fill = couleur)
    tab[1] = 'segment'
    tab[2] = x1
    tab[3] = y1
    tab[4] = x2
    tab[5] = y2
    tab[6] = couleur
    tab[7] = taille
    fenetre.objets.append(tab)

def trace_rectangle(x1, y1, x2, y2, couleur='noir', taille=2, remplissage='jaune'):
    """Trace un rectangle dont les sommets opposés sont les points de coordonées ``(x1, y1)`` et ``(x2, y2)``.

    Arguments:
        x1,y1,x2,y2 (float): Coordonées des sommets du rectangle.
        couleur (`couleur <#couleurs>`_, optionel): Couleur des cotés du rectangle (``noir`` par défaut).
        taille (int, optionel): épaisseur des cotés du rectangle. ( ``2`` par défaut).
        remplissage (str, optionel): Couleur de l'intérieur du rectangle (``yellow`` par default)
    """

    couleur = rgb2hex(rgb(couleur))
    remplissage = rgb2hex(rgb(remplissage))


    global fenetre

    tab = [0]*9
    tab[0] = fenetre.create_rectangle(fenetre._conv(x1,y1),fenetre._conv(x2,y2),
                                   outline = couleur, width = taille, fill= remplissage)
    tab[1] = 'rectangle'
    tab[2] = x1
    tab[3] = y1
    tab[4] = x2
    tab[5] = y2
    tab[6] = couleur
    tab[7] = taille
    tab[8] = remplissage
    fenetre.objets.append(tab)


def affiche_fenetre():
    """Affiche la fenêtre graphique."""
    global fenetre
    fenetre.loop

### Fonction principale pour demarrer ####
def creer_fenetre(titre = "Repère mathematique", xmin=-10, xmax=10, ymin=-10, ymax=10, fond = 'blanc', axes = True):
    """Initialise l'object fenetre graphique sans l'afficher.

    Arguments:
        titre (str): Titre de la fenêtre. La valeur par défaut est ``Repère mathematique``.
        xmin,xmax,ymin,ymax (float) : Dimensions du repère. Les valeurs par défaut sont -10, 10, -10, 10
        fond (`couleur <#couleurs>`_, optionel): Couleur de fond de la fenêtre (``blanc`` par défaut).
        axes (bool, optionel): Affiche les axes du repère si ``True`` (``True`` par défaut).
    """

    fond = rgb2hex(rgb(fond))

    root = Tk()       # on crée la fenêtre
    root.title(titre) # on lui donne un titre
    graph = _Fenetre_graphique(root,xmin = xmin, xmax=xmax, ymin = ymin, ymax=ymax,
                              background = fond, axes = axes)
    graph.pack(side=LEFT,fill=BOTH, expand= YES)
    global fenetre
    fenetre = graph
    return graph
