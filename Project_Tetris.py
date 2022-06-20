from tkinter import *
from copy import *
from random import randint
import time
from copy import deepcopy
import winsound
winsound.PlaySound("Tetris.wav", winsound.SND_ASYNC)

class Create_tetraminos:
    def __init__(self,Tetris, fenWin):
        '''
        Initialisation du tetris
        '''
        self.Tetris = Tetris
        self.fenWin = fenWin
        
        # Définition de toutes les pieces du tetris
        self.pieces = [[[[0,0,0,0],
                        [1,1,1,1],
                        [0,0,0,0],
                        [0,0,0,0]
                       ],
                       [[0,0,0,0],
                        [0,2,2,0],
                        [0,0,2,0],
                        [0,0,2,0]
                       ],
                       [[0,0,0,0],
                        [0,3,3,0],
                        [0,3,3,0],
                        [0,0,0,0]
                       ],
                       [[0,0,0,0],
                        [0,4,4,0],
                        [0,0,4,4],
                        [0,0,0,0]
                       ],
                       [[0,0,0,0],
                        [0,5,5,0],
                        [5,5,0,0],
                        [0,0,0,0]
                       ],
                       [[0,0,0,0],
                        [0,0,6,0],
                        [0,6,6,6],
                        [0,0,0,0]
                       ],
                       [[0,0,0,0],
                        [0,7,7,0],
                        [0,7,0,0],
                        [0,7,0,0]
                       ]],
                       [[[0,0,1,0],
                        [0,0,1,0],
                        [0,0,1,0],
                        [0,0,1,0]
                       ],
                       [[0,0,0,0],
                        [0,0,0,2],
                        [0,2,2,2],
                        [0,0,0,0]
                       ],
                       [[0,0,0,0],
                        [0,3,3,0],
                        [0,3,3,0],
                        [0,0,0,0]
                       ],
                       [[0,0,4,0],
                        [0,4,4,0],
                        [0,4,0,0],
                        [0,0,0,0]
                       ],
                       [[0,5,0,0],
                        [0,5,5,0],
                        [0,0,5,0],
                        [0,0,0,0]
                       ],
                       [[0,0,0,0],
                        [0,0,6,0],
                        [0,0,6,6],
                        [0,0,6,0]
                       ],
                       [[0,0,0,0],
                        [7,7,7,0],
                        [0,0,7,0],
                        [0,0,0,0]
                       ]],
                       [[[0,0,0,0],
                        [1,1,1,1],
                        [0,0,0,0],
                        [0,0,0,0]
                       ],
                       [[0,0,0,0],
                        [0,2,0,0],
                        [0,2,0,0],
                        [0,2,2,0]
                       ],
                       [[0,0,0,0],
                        [0,3,3,0],
                        [0,3,3,0],
                        [0,0,0,0]
                       ],
                       [[0,0,0,0],
                        [0,4,4,0],
                        [0,0,4,4],
                        [0,0,0,0]
                       ],
                       [[0,0,0,0],
                        [0,5,5,0],
                        [5,5,0,0],
                        [0,0,0,0]
                       ],
                       [[0,0,0,0],
                        [0,0,0,0],
                        [0,6,6,6],
                        [0,0,6,0]
                       ],
                       [[0,0,0,0],
                        [0,0,7,0],
                        [0,0,7,0],
                        [0,7,7,0]
                       ]],
                       [[[0,0,1,0],
                        [0,0,1,0],
                        [0,0,1,0],
                        [0,0,1,0]
                       ],
                       [[0,0,0,0],
                        [0,2,2,2],
                        [0,2,0,0],
                        [0,0,0,0]
                       ],
                       [[0,0,0,0],
                        [0,3,3,0],
                        [0,3,3,0],
                        [0,0,0,0]
                       ],
                       [[0,0,4,0],
                        [0,4,4,0],
                        [0,4,0,0],
                        [0,0,0,0]
                       ],
                       [[0,5,0,0],
                        [0,5,5,0],
                        [0,0,5,0],
                        [0,0,0,0]
                       ],
                       [[0,0,0,0],
                        [0,0,6,0],
                        [0,6,6,0],
                        [0,0,6,0]
                       ],
                       [[0,0,0,0],
                        [7,0,0,0],
                        [7,7,7,0],
                        [0,0,0,0]
                       ]]]
                
        # Grille principale
        self.grid = [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                        [-1,-1,-1,0,0,0,0,0,0,0,0,0,0,-1,-1,-1],
                    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],]
        
        self.score = 0 # Initialisation du score du joueur
        self.lignes_detruite = 0 # Initialisation du compteur de ligne détruite du joueur
        self.jeuTemps = int(time.time()) # Initialisation du temps de jeu du joueur avec le temps actuelle, le temps est compté en prenant le temps actuelle - le temps enregistré au debut
        self.defaite = False # Définie si le joueur à perdu, par defaut non
        self.saved = False # Définie si la partie a été enrigistré dans le fichier
        self.rotation = 0 # Définie la rotation actuelle de la piece (0,1,2,3 ou 4), 4 étant équivalent à 0
        self.random = randint(0,6) # Initialisation de la première piece
        self.colors = ["blue", "yellow", "pink", "green", "cyan", "red", "orange"] # Initialisation des couleurs possible pour les pieces
        self.Hcolors = list() # Initialisation de l'historique de couleur, utilisé pour assigner une couleur à une piece grace à son ID
        self.Hcolors.append(self.colors[self.random]) # Attribution d'une couleur à la première piece
        self.pieceId = 1 # Attribution d'un ID pour la première piece
        self.tetra = deepcopy(self.pieces[self.rotation][self.random])
        self.tetra_x = 6 # Atribution de la position X de la piece
        self.tetra_y = 3 # Atribution de la position Y de la piece
        while True :
            self.newRandom = randint(0,6) # génération de la piece suivante
            if self.newRandom != self.random: # verification pour que la prochaine piece soit différente de la piece actuelle
                self.futurpiece = self.newRandom # la prochaine piece est créer
                break
        self.pieceApercu = deepcopy(self.pieces[self.rotation][self.futurpiece])
        for j in range(0,4):
            for i in range(0,4):
                if self.tetra[j][i] == self.random+1: # la piece est déssiné sur la grille
                    self.tetra[j][i] = self.pieceId
        self.c_lapercu = Apercu(self, self.Tetris, self.fenWin)
        
    
    def cadriage(self):
        '''
        Il n'est pas possible de créer un thème sombre avec Tkinter, donc on met tous en noir et on dessine des lignes blanches
        '''
        for i in range(0, 440, 40):
            couleur = 'white'
            self.Tetris.create_rectangle(i, 0, i+2, 800,fill=couleur)
        for i in range(0, 800, 40):
            couleur = 'white'
            self.Tetris.create_rectangle(0, i, 400, i+2,fill=couleur)

    def draw_game(self):
        '''
        Fonction pour afficher la grille à l'écran
        '''
        self.Tetris.delete("all")
        for i in range(3,13):
            for j in range(2,22):
                if self.grid[j][i] != 0 and self.defaite:
                    couleur = 'red'
                    self.Tetris.create_rectangle((i-3)*40,(j-2)*40,((i-3)+1)*40,((j-2)+1)*40,fill=couleur)
                elif self.grid[j][i] > 0 and self.grid[j][i] < self.pieceId:
                    couleur = self.Hcolors[self.grid[j][i]-1]
                    self.Tetris.create_rectangle((i-3)*40,(j-2)*40,((i-3)+1)*40,((j-2)+1)*40,fill=couleur)
                elif self.grid[j][i] == self.pieceId:
                    couleur = self.colors[self.random]
                    self.Tetris.create_rectangle((i-3)*40,(j-2)*40,((i-3)+1)*40,((j-2)+1)*40,fill=couleur)
                elif self.grid[j][i] == 0:
                    couleur = 'black'
                    self.Tetris.create_rectangle((i-3)*40,(j-2)*40,((i-3)+1)*40,((j-2)+1)*40,fill=couleur)

    def collagePiece(self):
        '''
        Fonction pour déssiner une nouvelle piece sur la grille
        '''
        for j in range(0,4):
            for i in range(0,4):
                if self.grid[j+self.tetra_y][i+self.tetra_x] == 0:
                    if self.tetra[j][i] == self.pieceId:
                        self.grid[j+self.tetra_y][i+self.tetra_x] = self.pieceId

    def nettoyeur3000(self):
        for j in range(0,4):
            for i in range(0,4):
                if self.grid[j+self.tetra_y][i+self.tetra_x] == self.pieceId:
                    self.grid[j+self.tetra_y][i+self.tetra_x] = 0
    
    def SaTouchePas(self):
        '''
        Fonction pour vérifier si la piece touche d'autre piece
        '''
        satouchepas = True
        for j in range(0,4):
            for i in range(0,4):
                if self.tetra[j][i] == self.pieceId:
                    if self.grid[j+self.tetra_y][i+self.tetra_x] != self.pieceId and self.grid[j+self.tetra_y][i+self.tetra_x] != 0:
                        satouchepas = False
        return satouchepas

    def jeu(self):
        self.collagePiece()
        self.draw_game()
        self.cadriage()


    def rtt(self):
        '''
        Fonction pour tourner la piece actuelle
        '''
        self.nettoyeur3000()
        self.rotation += 1
        if self.rotation == 4:
            self.rotation = 0
        self.tetra = deepcopy(self.pieces[self.rotation][self.random])
        for j in range(0,4):
            for i in range(0,4):
                if self.tetra[j][i] == self.random+1:
                    self.tetra[j][i] = self.pieceId
        self.nettoyeur3000()
        self.jeu()
        
    def handleLeftKey(self):
        '''
        Fonction pour envoyer à gauche la piece actuelle de 1 case
        '''
        self.nettoyeur3000()
        self.tetra_x -= 1
        if self.SaTouchePas():
            self.nettoyeur3000()
            self.jeu()
        else:
            self.tetra_x += 1
            self.jeu()
        
    def handleRightKey(self):
        '''
        Fonction pour envoyer à droite la piece actuelle de 1 case
        '''
        self.nettoyeur3000()
        self.tetra_x += 1
        if self.SaTouchePas():
            self.nettoyeur3000()
            self.jeu()
        else:
            self.tetra_x -= 1
            self.jeu()
    
    def autodown(self):
        '''
        Fonction pour descendre la piece actuelle de 1 case
        '''
        self.nettoyeur3000()
        self.tetra_y += 1
        if self.SaTouchePas():
            self.nettoyeur3000()
            self.jeu()
        else:
            self.tetra_y -= 1
            self.jeu()
            self.check()
            self.Testdefaite()
            self.rePiece()
    
    def check(self):
        '''
        Vérifie si il est possible de détruire les ligne complété, si oui les ligne sont retiré
        '''
        supernombre=0
        for j in range(21, 3, -1):
            c_oui = True
            for i in range(3,13):
                if self.grid[j+supernombre][i] == 0:
                    c_oui = False
            if c_oui:
                self.score += 100
                self.lignes_detruite += 1
                for jk in range(j+supernombre, 2, -1):
                    for i in range(3,13):
                                self.grid[jk][i] = self.grid[jk-1][i]
                supernombre+=1
        if supernombre > 1:
            self.score += supernombre*100
        print("ton score est de:", self.score)
    
    def Testdefaite(self):
        '''
        Verifie si le joueur a perdu
        '''
        j = 4
        for i in range(3,13):
                if self.grid[j][i] != 0:
                    self.defaite = True
              
    def rePiece(self):
        '''
        Génère une nouvelle piece
        '''
        self.rotation = 0
        self.random = self.futurpiece
        while True :
            self.newRandom = randint(0,6)
            if self.newRandom != self.futurpiece:
                self.futurpiece = self.newRandom
                break
        self.colors = ["blue", "yellow", "pink", "green", "cyan", "red", "orange"]
        self.pieceId += 1
        self.tetra = deepcopy(self.pieces[self.rotation][self.random])
        self.tetra_x = 6
        self.tetra_y = 3
        self.Hcolors.append(self.colors[self.random])
        self.pieceApercu = deepcopy(self.pieces[self.rotation][self.futurpiece])
        for j in range(0,4):
            for i in range(0,4):
                if self.tetra[j][i] == self.random+1:
                    self.tetra[j][i] = self.pieceId
        self.c_lapercu.re()

class Apercu:

    def __init__(self, tetraminos, Tetris, fenWin):
        '''
        Initialise l'apperçu
        '''
        self.fenWin = fenWin
        self.Apercu = Canvas(self.fenWin,width = 160, height = 160)
        self.Apercu.pack(side="right")
        self.Tetris = Tetris
        self.tetraminos = tetraminos
        self.grille = deepcopy(self.tetraminos.pieceApercu)
        self.apDraw()

    def re(self):
        '''
        Methode à appeler pour mettre à jour la prochaine pièce
        '''
        self.grille = deepcopy(self.tetraminos.pieceApercu)
        self.apDraw()
    
    def apDraw(self):
        '''
        Dessine la prochaine piece à l'écran
        '''
        self.Apercu.delete("all")

        for i in range(0,4):
            for j in range(0,4):
                if self.grille[j][i] != 0:
                    couleur = self.tetraminos.colors[self.tetraminos.futurpiece]
                    self.Apercu.create_rectangle((i)*40,(j)*40,((i)+1)*40,((j)+1)*40,fill=couleur)
                elif self.grille[j][i] == 0:
                    couleur = 'black'
                    self.Apercu.create_rectangle((i)*40,(j)*40,((i)+1)*40,((j)+1)*40,fill=couleur)
        
        for i in range(0, 200, 40):
            couleur = 'white'
            self.Apercu.create_rectangle(i, 0, i+2, 160,fill=couleur)
        for i in range(0, 200, 40):
            couleur = 'white'
            self.Apercu.create_rectangle(0, i, 160, i+2,fill=couleur)




class Tetris:

    clock = time.time()

    def run(self):
        '''
        Fonction principale, definition de la fenêtre + boucle principale
        '''
        fenWin = Tk()
        fenWin.title('Tetris')
        fenWin.geometry('600x800')

        self.fenWin = fenWin

        self.Tetris = Canvas(fenWin,width = 400, height = 800)
        self.Tetris.pack(side="left")

        self.tetraminos = Create_tetraminos(self.Tetris, self.fenWin)
        self.tetraminos.jeu()
        #self.c_lapercu = Apercu(self.tetraminos, self.Tetris, self.fenWin)

        fenWin.bind('<Key>', self.handleKeyboardEvent)

        while True:
            if time.time()>(self.clock+1*(0.98**(self.tetraminos.pieceId-1))) and not self.tetraminos.defaite:
                self.clock = time.time()
                self.tetraminos.autodown()
            if self.tetraminos.defaite:
                self.tetraminos.draw_game()
                winsound.PlaySound(None, winsound.SND_ASYNC)
                if not self.tetraminos.saved:
                    self.tetraminos.saved = True
                    with open("Tetris_historique_parties.txt", "a", encoding="utf_8") as file:
                        file.write(f"\n\n\npartie joué le {time.localtime().tm_mday}/{time.localtime().tm_mon}/{time.localtime().tm_year} à {time.localtime().tm_hour}h{time.localtime().tm_min}")
                        file.write(f"\nscore : {self.tetraminos.score}\nlignes détruites : {self.tetraminos.lignes_detruite}\npieces jouées : {self.tetraminos.pieceId-1}\ntemps de jeu : {time.localtime(int(time.time())-self.tetraminos.jeuTemps).tm_min}min{time.localtime(int(time.time())-self.tetraminos.jeuTemps).tm_sec}s")
            fenWin.update_idletasks()
            fenWin.update()
        
    def handleKeyboardEvent(self, event):
        '''
        Cette fonction permet de prendre en charge les appuy sur les touches du clavier
        '''
        if (event.keysym == "Left") and not self.tetraminos.defaite:
            self.tetraminos.handleLeftKey()
            
        if (event.keysym == "Right") and not self.tetraminos.defaite:
            self.tetraminos.handleRightKey()
        
        if (event.keysym == "Up") and not self.tetraminos.defaite:
            self.tetraminos.rtt()
        
        if (event.keysym == "Down") and not self.tetraminos.defaite:
            self.tetraminos.autodown()

tetris = Tetris()
tetris.run()
