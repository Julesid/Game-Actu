#imporations des bibliothéques
from tkinter import *
from random import randrange

def deplacer(): #définition des variables
    global x
    global y,pX,pY
    global Serpent
    snake.delete('all')
    i=len(Serpent)-1
    j=0
    while i > 0:
        Serpent[i][0]=Serpent[i-1][0]
        Serpent[i][1]=Serpent[i-1][1]
        snake.create_oval(Serpent[i][0], Serpent[i][1], Serpent[i][0] +10, Serpent[i][1]+10,outline='#c30000', fill='#c30000')
        i=i-1

    snake.create_rectangle(pX, pY, pX+5, pY+5, outline='green', fill='green')

#déplacemnts du serpent
    if direction  == 'gauche':
        Serpent[0][0]  = Serpent[0][0] - dx
        if Serpent[0][0] < 0:
            Serpent[0][0] = 493
    elif direction  == 'droite':
        Serpent[0][0]  = Serpent[0][0] + dx
        if Serpent[0][0] > 493:
            Serpent[0][0] = 0
    elif direction  == 'haut':
        Serpent[0][1]  = Serpent[0][1] - dy
        if Serpent[0][1] < 0:
            Serpent[0][1] = 493
    elif direction  == 'bas':
        Serpent[0][1]  = Serpent[0][1] + dy
        if Serpent[0][1] > 493:
            Serpent[0][1] = 0
    snake.create_oval(Serpent[0][0], Serpent[0][1], Serpent[0][0]+10, Serpent[0][1]+10,outline='#c30000', fill='#c30000')
    test()
    test()

    if flag != 0:
        fond.after(60, deplacer)

def jeux():
    global pX,pY
    global flag
    if flag == 0:
        flag = 1
    deplacer()

def left(event):
    global direction
    direction = 'gauche'

def right(event):
    global direction
    direction = 'droite'

def up(event):
    global direction
    direction = 'haut'

def down(event):
    global direction
    direction = 'bas'

def test():
    global pomme
    global x,y,pX,pY
    global Serpent
    if Serpent[1][0]>pX-7 and  Serpent[1][0]<pX+7:
        if Serpent[1][1]>pY-7 and Serpent[1][1]<pY+7:
            #On place une nouvelle pomme de manière aléatoire sur la carte
            pX = randrange(5, 495)
            pY = randrange(5, 495)
            snake.coords(pomme,pX, pY, pX+5, pY+5)
            #On rajoute 1 points au serpent
            Serpent.append([0,0])
x = 245
y = 24
dx, dy = 10, 10
flag = 0
direction = 'haut'
Serpent=[[x,y],[x+2.5,y+2.5],[x+5,y+5],[0,0]]

pX = randrange(5, 495)
pY = randrange(5, 495)

fond = Tk()
snake = Canvas(fond, width=500, height=500, bg='#757575')
snake.pack(side=TOP, padx=5, pady=5)


oval1=snake.create_oval(Serpent[1][0], Serpent[1][1], Serpent[1][0] +10, Serpent[1][1]+10, outline='green', fill='#c30000')

oval = snake.create_oval(Serpent[0][0], Serpent[0][1], Serpent[0][0]+10, Serpent[0][1]+10, outline='green', fill='green')

pomme = snake.create_rectangle(pX, pY, pX+5, pY+5, outline='green', fill='green')

b1 = Button(fond, text='Lancer', command=jeux, bg='white' , fg='black')
b1.pack(side=LEFT, padx=5, pady=5)

b2 = Button(fond, text='Quitter', command=fond.destroy, bg='white' , fg='black')
b2.pack(side=RIGHT, padx=5, pady =5)


fond.bind('<Right>', right)
fond.bind('<Left>', left)
fond.bind('<Up>' , up)
fond.bind('<Down>', down)

fond.mainloop()