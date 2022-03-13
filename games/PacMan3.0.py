from tkinter import *

# Quand on appuie sur une touche, on l'ajoute à la liste
def enfoncee(evt) :
    T = evt.keysym.upper() # En majuscule pour confondre 'a' et 'A'
    if  T not in Touches :
        Touches.append(T)

# Quand on relache la touche, on la retire
def relachee(evt) :
    T = evt.keysym.upper()
    if T in Touches :
        Touches.remove(T)

# Boucle principale :
def animation() :
    score = 0
    global XS, YS, NBcup
    NomFichier = 'PacManp'
    Xavant, Yavant = XS, YS
    if "UP" in Touches :
        if Decors[(YS-27)//40][XS//40] in (' ','H','P','T') :
            YS = YS - 40
            NomFichier = 'PacManp'
            if Decors[(YS)//40][(XS)//40] in (' ','H','X','T') :
                score = score + 1
    if "DOWN" in Touches :
        if Decors[(YS+27)//40][XS//40] in (' ','H','P','T') :
            YS = YS + 40
            NomFichier = 'PacManp'
            if Decors[(YS)//40][(XS)//40] in (' ','H','X','T') :
                score = score + 1
    if "LEFT" in Touches :
        # On regarde ce qu'il y a au pied gauche de la souris : La souris fait
        # 30 pixels de large et 40 pixels de haut, on regarde donc la case qui
        # se situe à (XS - 15 - 8 , YS + 19)
        if Decors[(YS+19)//40][(XS-23)//40] in (' ','H','P','T') :
            XS = XS - 40
            NomFichier = 'PacManp'
            if Decors[(YS)//40][(XS)//40] in (' ','H','X','T') :
                score = score + 1
    if "RIGHT" in Touches :
        # Idem à droite
        if Decors[(YS+19)//40][(XS+23)//40] in (' ','H','P','T') :
            XS = XS + 40
            NomFichier = 'PacManp'
            if Decors[(YS)//40][(XS)//40] in (' ','H','X','T') :
                score = score + 1
    Fond.itemconfigure(pacman, image=eval(NomFichier))
    Fond.coords(pacman, XS, YS)


    if Decors[YS//40][XS//40] == 'P' :
        Decors[YS//40][XS//40] = ' '
        # On efface le cupcake avec un rectangle couleur du fond
        col, lig = (XS // 40) * 40, (YS // 40) * 40
        Fond.create_rectangle(col,lig,col + 39, lig + 39, fill="#000000", outline="#000000")
        #On replace les items souris et chat avant le rectangle effectué
        Fond.tag_raise(pacman)
        NBcup = NBcup + 1
        texte = "Score : "+str(NBcup)+" Points"
        Fond.itemconfig(Txt2,text=texte)

    # on relance la fonction animation après 9ms ce qui permet de continuer les animations
    #même si aucune  touche n'est enfoncée!!
    fenetre.after(130,animation)

# Version 1 : Dessin du décors

def lisDecors(fichier):
    """
    Fonction qui lis le contenu du fichier fichier et la place dans
    la liste 2D Decors
    """
    filin = open(fichier,'r')
    R = [list(line.replace('\n','')) for line in filin]
    filin.close()
    return R

def dessine():
    """
    Fonction qui dessine le plateau de jeu avec les données de la liste Decors
    """
    global XS, YS
    ligne, colonne = 0, 0
    # on parcourt chaque liste de la liste 2D Decors
    #on lit chaque caractère pour savoir ce qu'il faut afficher
    while ligne < 17 :
      if Decors[ligne][colonne] == 'X' :
        Fond.create_image(colonne*40, ligne*40, image=X, anchor=NW)
      if Decors[ligne][colonne] == 'T' :
        Fond.create_image(colonne*40, ligne*40, image=T, anchor=NW)
      if Decors[ligne][colonne]=='P' :
        Fond.create_image(colonne*40, ligne*40, image=P, anchor=NW)
      if Decors[ligne][colonne]=='H' :
        Fond.create_image(colonne*40, ligne*40, image=H, anchor=NW)
      if Decors[ligne][colonne]=='D' :
        Fond.create_image(colonne*40, ligne*40, image=D, anchor=NW)
      if Decors[ligne][colonne] == 'S' :    # Si on a une souris dans le décors
        XS, YS = colonne*40+20, ligne*40+20 # On initialise les coordonnées
        Decors[ligne][colonne] = ' '        # On l'efface du décors
      colonne=colonne+1
      if colonne == 25 :
        colonne = 0
        ligne = ligne + 1


fenetre=Tk()
fenetre.resizable(width=False, height=False)

fenetre.title("PacMan")
fenetre.geometry("1200x680")

# Chargement des fichiers :
T=PhotoImage(file="images/Vert.png")
H=PhotoImage(file="images/Rouge.png")
X=PhotoImage(file="images/Bleu.png")
P=PhotoImage(file="images/Rose.png")
C=PhotoImage(file="images/Coeur.png")
D=PhotoImage(file="images/pacgum.png")

# Dessin de l'interface
Fond=Canvas(fenetre,width=1200,height=680,bg="#000000")
Fond.place(x=0,y=0)
Fond.create_rectangle(1000,0,1200,680,fill="grey",width=5,outline="white")
Fond.create_image(1100,225,image=P)
Fond.create_image(1100,125,image=C)

# Informations sur la souris :
PacManp=PhotoImage(file="images/jaune.png")
XS, YS = 0, 0   # Position

#Affiche le score
Txt=Fond.create_text(1100,20,text="PacMan",font=("comic sans ms","20"),fill="#ffc900")
Txt2=Fond.create_text(1100,275,text="Score : Points",font=("comic sans ms","15"),fill="#5736A6")
Txt3=Fond.create_text(1100,670,text="Created by : Enzo ALOUIN & Jules CHEMINAT",font=("comic sans ms","6"),fill="#ffffff")

# On lis le décors. On garde les informations du décors dans une liste pour
# pouvoir tester si on tombe, si on peut monter, ....
Decors = lisDecors('niveaux/niv1.txt')
dessine()

pacman=Fond.create_image(XS, YS, image=PacManp)
NBcup = 0

# Surveillance des touches
Touches = []
fenetre.bind_all("<KeyPress>",enfoncee)
fenetre.bind_all("<KeyRelease>",relachee)

animation()

fenetre.mainloop()
