#########################################
#   Adrien Montariol    Alexandre Wery  #
#               2018-2019               #
#                   6Info               #
#       Travail de fin d'études         #
#########################################



from tkinter import *
from tkinter import messagebox
from random import *
import webbrowser
import os
import PokemonBr
import update
from  pygame.locals import *
import pygame
import sqlite3
import hashlib
from tkinter import ttk
from tkinter.messagebox import showinfo



class Launcher:
    def __init__(self,fen,login,mdp):
        """
        methode constructrice de la classe
        ne renvoie rien, prend login et mdp en parrametres
        """
        #initialisation des différents attributs fixes à la classe
        self.fen=fen
        self.login=login
        self.mdp=mdp
        self.width=1000
        self.height=750
        self.C2 = Canvas(self.fen, bg="#4b433b", height=750, width=250,bd=0, highlightthickness=0, relief='ridge')
        self.C1 = Canvas(self.fen, height=750, width=750,bd=0, highlightthickness=0, relief='ridge')
        self.img=Launcher.imagechooser()
        self.img2 = PhotoImage(file='BattleScene/logo_final_25.png')
        self.panel = Label(self.fen, image = self.img2)
        self.fen.geometry('1000x750')
        self.fen.resizable(False, False)
        self.fen.configure(bg="black")

    def verifierlogin(self):
        """
        methode permettant de verifier le login et le mot de passe de l'utilisateur
        ne renvoie rien, prend self en parametre
        """
        self.login=self.login.get()#recuperation de login
        self.mdp=self.mdp.get()#recuperation de mdp
        Drapeau=0
        conn = sqlite3.connect('db.db')#connection a la db
        c = conn.cursor()#variable permettant l'interaction avec la db
        mdps=[]#creation de la table mot de passe
        logins=[]#creation de la table logins
        for row in c.execute("SELECT * FROM joueur"):#boucle for permettant de selectionner les element de joueur et de les stocker dans leurs listes respectives
            mdps.append(row[5])
            logins.append(row[4])
        stop=False
        for i in range (0,len(logins)):#boucle for permettant de parcourir login et mdp et de verifier si les valeurs encodées par l'utilisateur sont présentes dedans.
            if self.login==str(logins[i]) and str(mdps[i])==hashlib.md5(self.mdp.encode()).hexdigest() and stop ==False:
                Drapeau = 1
                stop=True
            elif self.login==str(logins[i]) and str(mdps[i])!=hashlib.md5(self.mdp.encode()).hexdigest()and stop ==False:
                Drapeau=2
            elif self.login!=str(logins[i])and stop ==False:
                Drapeau = 3
        if Drapeau ==1:
            print('Bon mdp et login')
        elif Drapeau==2:
            print('mdp incorrect')
        elif Drapeau ==3:
            print("pas d'user trouvé")
        else :
            print('non')
        
        for widget in self.fen.winfo_children():#destruction de tout les widgets de la page
                widget.destroy()


        if Drapeau==1:#test de redirection vers la page de lancement du jeu
            oui(self.fen,self.login)
        else:
            fen=Launcher(self.fen,"","")
            fen.creer_launcher()

    #les 3 methodes ci dessous sont identiques
    def popup_showinfo(self):
        """
        methode permettant d'afficher un popup
        ne revoie rien et prend self en parametre
        """
        showinfo("About", "This is a game by Alexandre Wery and Adrien Montariol that was created for their computer science class. This game is based on the ever so popular pokemon license.")
    def popup_showinfo2(self):#methode permettant d' afficher un popup
        showinfo("Objective", "The Objective of this project is of course to develop our skills in programming and time managing but also to, through this project, get our diploma at the end of the year.")
    def popup_showinfo3(self):
        showinfo("Programs", "We have used multiple programms and languages such as Tkinter, Pygame and the default python library. For our website, we've used php, html and css. To link everything together, we used SQLite and MySQL.We've used multiple programms such as Idle for python, Visual Studio for web languages and Wamp for database programming.")


    def creer_menus(self):
        """
        methode permettant de vréer les menus déroulants dans le jeu
        ne renvoie rien et prend self en parametre
        """
        top = Menu(self.fen)
        self.fen.config(menu=top)
        jeu = Menu(top, tearoff=False)
        
        top.add_cascade(label='Menu', menu=jeu)#creation du menu déroulant
        jeu.add_command(label='Site', command=lambda:webbrowser.open_new('http://localhost/SITE%20TFE%20Final/Vue/home.php'))#onglet du menu
        submenu=Menu(jeu, tearoff=False)#sous menu de menu  
        submenu2=Menu(jeu, tearoff=False)#sous menu2 de menu
        jeu.add_cascade(label='Access specific pages', menu=submenu)
        submenu.add_command(label='Wiki', command=lambda:webbrowser.open_new('http://localhost/SITE%20TFE%20Final/Vue/wiki.php'))#onglet de pages 
        
        jeu.add_cascade(label='About', menu=submenu2)#sous menu contenant les popup
        submenu2.add_command(label='Information', command=lambda:self.popup_showinfo())
        submenu2.add_command(label='Objective', command=lambda:self.popup_showinfo2())#differents bouttons permettant d'activer les popups
        submenu2.add_command(label='Programs', command=lambda:self.popup_showinfo3())


        top.add_command(label='Quit', command=self.fen.destroy)#ajout du bouton quitter

    def imagechooser ():
        """
        methode permettant de renvoyer une image aleatoire
        ne prend rien en parametre et renvoie une image
        """
        nb = randint(1,3)#choix aleatoire
        imgfond1 = PhotoImage(file='./BattleScene/launcherimg1.png')#lien vers différentes images
        imgfond2 = PhotoImage(file='./BattleScene/launcherimg2.png')
        imgfond3 = PhotoImage(file='./BattleScene/launcherimg3.png')
        if nb==1:#selon le choix aleatoire, renvoie une valeur
            return imgfond1
        elif nb==2:
            return imgfond2
        elif nb==3:
            return imgfond3

    
    def creer_start(self,login):
        """
        methode permettant de créer le menu launcher apres la connexion
        prend self et login en parametre et ne renvoie rien
        """
        self.C2.place(x=750,y=0)#placemement de canvas
        self.creer_menus()#appel de la fonction pour les menus déroulants
        
        self.panel.image=self.img2#placemement de canvas
        self.panel.place(x=845,y=25)


        
        self.C1.create_image(0, 0, image=self.img, anchor=NW)#placemement de canvas
        self.C1.image=self.img
        self.C1.place(x=0,y=0)

        Label(self.fen, text="Bienvenue,",bg="#4b433b",font="Broadway").place(x=self.width-247, y=250)#placemement de Labels
        Label(self.fen, text=login,bg="#4b433b",font="Broadway").place(x=self.width-247, y=300)#placemement de Labels
        Label(self.fen, text="le jeu est pret à ",bg="#4b433b",font="Broadway").place(x=self.width-247, y=350)#placemement de Labels
        Label(self.fen, text="être lancé",bg="#4b433b",font="Broadway").place(x=self.width-247, y=400)#placemement de Labels

        Button(self.fen, width=15, text="Play Tutorial",bg="#4b433b",font="Broadway", relief=GROOVE, command=lambda:launchgame(self.fen,login,True)).place(x=self.width-247, y=630)#placemement de Bouttons
        Button(self.fen, width=15, text="Play",bg="#4b433b",font="Broadway", relief=GROOVE, command=lambda:launchgame(self.fen,login,False)).place(x=self.width-247, y=680)#placemement de Bouttons
        
    def creer_launcher(self):
        """
        methode permettant de créer le menu launcher 
        prend self et login en parametre et ne renvoie rien
        """
        self.creer_menus()#appel de la fonction pour les menus déroulants

        self.C2.place(x=750,y=0)#placemement de canvas

        self.panel.image=self.img2
        self.panel.place(x=845,y=25)


        
        self.C1.create_image(0, 0, image=self.img, anchor=NW)#placemement de canvas
        self.C1.image=self.img
        self.C1.place(x=0,y=0)

        self.login =StringVar(self.fen)#creation des variables pour stocker les valeurs de login et de mdp
        self.login.set("")
        self.mdp = StringVar(self.fen)
        self.mdp.set("")

        self.l1txt = Label( self.fen,text = "Login:",width=15,bg="#4b433b",font="Broadway" ).place(x=self.width-240, y=125)#placemement de Labels
        self.l1entree = Entry( self.fen,width=16,textvariable = self.login,bg="#4b433b",font="Broadway", relief=GROOVE ).place(x=self.width-240, y=175)#placemement de Labels

        Label( self.fen,text = "Mot de Passe:",width=15,bg="#4b433b",font="Broadway" ).place(x=self.width-240, y=225)#placemement de Labels
        Entry( self.fen,width=16,textvariable = self.mdp, show="*",bg="#4b433b",font="Broadway", relief=GROOVE ).place(x=self.width-240, y=275)#placemement de Labels

        Button(self.fen, text="Login", width=7,bg="#4b433b",font="Broadway", command=lambda: self.verifierlogin(), relief=GROOVE).place(x=self.width-180, y=325)#placemement de Bouttons
        


        self.fen.mainloop
        
    
def launchgame(fen,login,state):
    """
    methode permettant de lancer le jeu
    prend fen en parametre en ne renvoie rien
    """
    fen.destroy()#destruction de la fenetre
    PokemonBr.jouer(login,state)#appel du jeu principal
    
def oui(win,login):
    """
    methode permettant de lancer le second menu du launcher
    prend fen en parametre en ne renvoie rien
    """
    fen=fen=Launcher(win,"","")#instanciation de fenetre
    fen.creer_start(login)#appel de la methode permettant de creer le 2e menu

def launch(login):
    update.update()
    win=Tk()#creation de la fenetre
    fen=Launcher(win,"","")#instanciation de fenetre
    fen.creer_start(login)#appel de la methode permettant de creer le 1e menu
    win.mainloop()
    
def launchlauncher():
    update.update()
    win=Tk()#creation de la fenetre
    fen=Launcher(win,"","")#instanciation de fenetre
    fen.creer_launcher()#appel de la methode permettant de creer le 1e menu
    win.mainloop()
