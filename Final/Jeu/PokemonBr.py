import pygame
import time
import random
import sqlite3
from math import *
import update2
import launcherPOO
import tuto
import lvl
import tileset
class play:
    def __init__(self,tut=False):
        self.tuto=tut
        global joueur
        global login
        self.height=736
        self.width=512
        
        self.win = pygame.display.set_mode((self.width,self.height))#Permet de stocker la fenetre


        #int(( ( ( (2*lvl/5) +2) *20*baseattack/basedefence) /50)+2)
        
        #Interaction avec la base de donnée
        conn = sqlite3.connect('db.db')
        c = conn.cursor()

        
        #attribue son sac au joueur
        sac=1
        for row in c.execute("SELECT * FROM sac"):
            sac+=1
        self.nsac=sac
        sac=str(sac)
        c.execute("INSERT INTO sac VALUES ("+sac+")")
        c.execute("INSERT INTO objets VALUES (NULL,'Pokeball',0,"+sac+")")
        c.execute("INSERT INTO objets VALUES (NULL,'Superball',0,"+sac+")")
        c.execute("INSERT INTO objets VALUES (NULL,'Hyperball',0,"+sac+")")
        c.execute("INSERT INTO objets VALUES (NULL,'Masterball',0,"+sac+")")
        c.execute("INSERT INTO objets VALUES (NULL,'Potion',0,"+sac+")")
        c.execute("INSERT INTO objets VALUES (NULL,'SuperPotion',0,"+sac+")")
        c.execute("INSERT INTO objets VALUES (NULL,'HyperPotion',0,"+sac+")")
        c.execute("INSERT INTO objets VALUES (NULL,'PotionMax',0,"+sac+")")
        c.execute("INSERT INTO objets VALUES (NULL,'Rappel',0,"+sac+")")
        c.execute("INSERT INTO objets VALUES (NULL,'RappelMax',0,"+sac+")")
        conn.commit()
        conn.close()
                    
                
            
        
        self.x = -300#position x du joueur sur la map en pixels
        self.y = 0#position y du joueur sur la map en pixels
        self.vel = 3#vitesse de déplacement
        
        self.tileset = pygame.image.load("tileset.png").convert_alpha()#image contenant toutes les parties de la map

        if tut:
            self.level=tuto.niv
        else:
            self.level=lvl.niv#contient la disposition de la map
        
        self.xs=len(self.level[0])*32#largeur de la map en tuiles
        self.ys=len(self.level)*32#hauteur de la map en tuiles
        
        self.xtj=abs(self.x)/32+self.width/64#position x du joueur sur la map en tuiles
        self.ytj=abs(self.y)/32+self.height/64#position y du joueur sur la map en tuiles
        self.lt=[0,0]
        self.collision=tileset.tilescollision#contient un liste qui détermine si une tuile est traversable ou non

        self.trainers = pygame.image.load("characters.png").convert_alpha()#charge l'image contenant les personnages du jeu
        self.trainers = pygame.transform.scale(self.trainers, (self.trainers.get_width()*2, self.trainers.get_height()*2))
        

        self.textbox=pygame.image.load("./BattleScene/textbox.png")
        self.textbox=pygame.transform.scale(self.textbox,(self.textbox.get_width()*2,self.textbox.get_height()*2))
        self.message=False#Vrai si il y à un message à afficher
        
        self.eact={'[2, 2]':'print("ceci est un sapaing")','[4, 20]':'self.pickpokeball(ftt)'}#dictionnaire contenant les interaction avec la tuile choisie
        self.way=""#initialisation de la direction du personnage du joueur à nulle

        #génère les PNJ (personnages non joueurs)
        self.pnjs=[]
        for i in range(0,len(self.level)):
            for j in range(0,len(self.level[i])):
                for k in range(0,len(self.level[i][j])):
                    if len(self.level[i][j][k])==3:
                        self.pnjs.append(createpnj(i,self.win,[j*32,i*32],self.level[i][j][k][2][0],self.level[i][j][k][2][1],self.level[i][j][k][2][2],self.vel,self.level[i][j][k][2][3]))
                        
    def choosestarter(self):
        starters=[pygame.transform.scale(pygame.image.load("./BattleScene/front/001.gif"),(int(512/3),int(512/3))),pygame.transform.scale(pygame.image.load("./BattleScene/front/004.gif"),(int(512/3),int(512/3))),pygame.transform.scale(pygame.image.load("./BattleScene/front/007.gif"),(int(512/3),int(512/3)))]
        pokeball=pygame.transform.scale(pygame.image.load("pokeball.png"),(int(512/3),int(512/3)))
        chosen=25#le pokémon choisi par défaut est pikachu
        otime=time.time()#relève le temps au lancement du programe
        tm=15#temps restant à l'utilisateur pour choisir son pokémon
        tl=tm
        while tl>0:#donne 15 secondes au joueur pour choisir son pokémon de départ
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    global run
                    run=False
            self.win.fill((255,255,255))
            tl=tm+otime-time.time()
            self.win.blit(pygame.font.SysFont("monospace", 50).render(str(int(tl)), 1, (0,0,0)), (240, 00))
            pygame.draw.rect(self.win,(0,0,0),((40,60, 432, 50)))
            pygame.draw.rect(self.win,(255,255,255),((50,70, 412, 30)))
            pygame.draw.rect(self.win,(255,0,0),((50,70, (412/tm)*tl, 30)))
            self.win.blit(pygame.font.SysFont("monospace", 20).render("Choisissez votre pokémon de départ:", 1, (0,0,0)), (0,150))
            if (736/2-512/6<pygame.mouse.get_pos()[1]<736/2+512/6 and pygame.mouse.get_pos()[0]<512/3) or chosen==1:
                self.win.blit(starters[0], (0, int(736/2-512/6)))
            else:
                self.win.blit(pokeball, (0, int(736/2-512/6)))
            
            if (int(736/2-512/6)<pygame.mouse.get_pos()[1]<int(736/2+512/6) and 512/3<pygame.mouse.get_pos()[0]<512*2/3) or chosen==4:
                self.win.blit(starters[1], (512/3, int(736/2-512/6)))
            else:
                self.win.blit(pokeball, (512/3, int(736/2-512/6)))
            
            if (int(736/2-512/6)<pygame.mouse.get_pos()[1]<int(736/2+512/6) and 512*2/3<pygame.mouse.get_pos()[0]) or chosen==7:
                self.win.blit(starters[2], (512*2/3, int(736/2-512/6)))
            else:
                self.win.blit(pokeball, (512*2/3, int(736/2-512/6)))

            if pygame.mouse.get_pressed()[0]==1:
                if 736/2-512/6<pygame.mouse.get_pos()[1]<736/2+512/6:
                    if pygame.mouse.get_pos()[0]<512/3:
                        chosen=1#pokémon sélectionné
                    elif pygame.mouse.get_pos()[0]<512*2/3:
                        chosen=4
                    else:
                        chosen=7
            if pygame.mouse.get_pressed()[2]==1:
                chosen=0
            pygame.display.update()
            pygame.time.delay(10)
        conn = sqlite3.connect('db.db')
        c = conn.cursor()
        #attribue un numéro d'équipe au joueur
        team=1
        for row in c.execute("SELECT * FROM equipe"):
            team+=1
        self.numteam=team
        team=str(team)
        c.execute("INSERT INTO equipe(idEquipe) VALUES ("+team+")")#Créer l'équipe du joueur

        #attribue son pokémon de départ au joueur
        for row in c.execute("SELECT * FROM basepokemon WHERE id = "+str(chosen)):#Récupère les données du pokemon generique corrspondant à notre starter
            base=row
        npokemon=1
        self.basehp = int(str(base[3]))
        self.basevitesse = int(str(base[4]))
        self.baseattack = int(str(base[5]))
        self.basedefence = int(str(base[6]))
        self.basehp = int((((int(self.basehp)*2) + (int((int(sqrt(int(str(base[7])))*100))/4))*int(5))/100)+5+10)
        self.basevitesse=int((((int(self.basevitesse)*2) +(int((int(sqrt(int(str(base[7])))*100))/4))*int(5))/100)+5)
        self.baseattack=int((((int(self.baseattack)*2) + (int((int(sqrt(int(str(base[7])))*100))/4))*int(5))/100)+5)
        self.basedefence=int((((int(self.basedefence)*2) + (int((int(sqrt(int(str(base[7])))*100))/4))*int(5))/100)+5)
        if joueur.tuto :
            self.basehp=200
            self.basevitesse = self.basevitesse*4
        for row in c.execute("SELECT * FROM pokemon"):
            npokemon+=1
        npokemon=str(npokemon)
        c.execute("INSERT INTO pokemon VALUES ("+npokemon+","+str(base[0])+",'"+base[1]+"','"+base[2]+"',5,"+str(self.basehp)+","+str(self.basehp)+","+str(self.basevitesse)+","+str(self.baseattack)+","+str(self.basedefence)+","+str(base[7])+","+team+")")#Attribue les données génériques a notre pokemon de départ
        #attribue sa première attaque au pokémon de départ du joueur
        nattack=1
        for row in c.execute("SELECT * FROM attaquespokemon"):
            nattack+=1
        c.execute("INSERT INTO attaquespokemon VALUES ("+str(nattack)+",59,"+npokemon+")")
        conn.commit()
        conn.close()

    
    def move(self):
        global joueur
        global login
        keys = pygame.key.get_pressed()
        #En fonction de flèche enfoncée, si la vois est libre dans la direction de la flèche, déplace le personnage du joueur dans direction
        #playertilepos contient la tuile du personnage à afficher
        if keys[pygame.K_LEFT]:
            self.way="L"
            if self.x<0 and self.hocollision(self.way):
                self.x += self.vel
                if int((time.time()*4)%2)==0:
                    playertilepos=[0,1344]
                else:
                    playertilepos=[0,1472]
            else:
                playertilepos=[0,1408]
            self.message=False
        elif keys[pygame.K_RIGHT] :
            self.way="R"
            if self.x>self.width-self.xs+50 and self.hocollision(self.way):
                self.x -= self.vel
                if int((time.time()*4)%2)==0:
                    playertilepos=[64,1344]
                else:
                    playertilepos=[64,1408]
            else:
                playertilepos=[64,1280]
            self.message=False
        elif keys[pygame.K_UP]:
            self.way="U"
            if self.y<0 and self.hocollision(self.way):
                self.y += self.vel
                if int((time.time()*4)%2)==0:
                    playertilepos=[128,1280]
                else:
                    playertilepos=[64,1472]
            else:
                playertilepos=[0,1280]
            self.message=False
        elif keys[pygame.K_DOWN]:
            self.way="D"
            if self.y>self.height-self.ys+21 and self.hocollision(self.way):
                self.y -= self.vel
                if int((time.time()*4)%2)==0:
                    playertilepos=[128,1408]
                else:
                    playertilepos=[128,1472]
            else:
                playertilepos=[128,1344]
            self.message=False
        else:
            if self.way=="L":
                playertilepos=[0,1408]
            elif self.way=="R":
                playertilepos=[64,1280]
            elif self.way=="U":
                playertilepos=[0,1280]
            else:
                playertilepos=[128,1344]

        #efface la fenetre
        self.win.fill((255,255,255))

        #détermine la tuile sur laquelle le joueur se trouve
        self.xtj=abs(self.x)/32+self.width/64
        self.ytj=abs(self.y)/32+self.height/64

        #si la touche E est pressée
        if keys[pygame.K_e]:
            if self.ce:#si l'utilisateur peut appuyer sur e
                self.ce=False
                xf=self.x#xf coordonnée x de la tuile en face du joueur en pixels
                yf=self.y#yf coordonnée y de la tuile en face du joueur en pixels
                if self.way=="L":
                    xf+=20
                    yf-=16
                elif self.way=="R":
                    xf-=20
                    yf-=16
                elif self.way=="U":
                    yf+=10
                else:
                    yf-=32
                self.yft=int(-yf/32+self.height/64)#xf coordonnée x de la tuile en face du joueur
                self.xft=int(-xf/32+self.width/64)#yf coordonnée y de la tuile en face du joueur
                for i in range(0,len(self.pnjs)):#Interaction avec un PNJ
                    if int(self.xft)==self.pnjs[i].pos[0]/32 and int(self.yft)==self.pnjs[i].pos[1]/32:
                        if self.pnjs[i].active:
                            if self.pnjs[i].trainer:
                                self.pnjs[i].duel()
                            else:
                                objet=random.choice(['Pokeball','Superball','Hyperball','Masterball','Potion','SuperPotion','HyperPotion','PotionMax','Rappel','RappelMax'])#objet à donner
                                quant=random.randint(1,3)#quantité d'objets à donner
                                self.message=["Personnage: Prend ces "+str(quant)+" "+str(objet),"Tu en aurra plus besoin que moi!"]

                                conn = sqlite3.connect('db.db')
                                c = conn.cursor()
                                #ajouter les objets dans la base de donnée
                                for row in c.execute("SELECT quantité FROM objets WHERE refsac="+str(joueur.nsac)+" AND Nom='"+objet+"'"):
                                    row=row[0]+quant
                                    c.execute("DELETE FROM objets WHERE refsac="+str(joueur.nsac)+" AND Nom='"+objet+"'")
                                    c.execute("INSERT INTO objets VALUES (NULL,'"+objet+"',"+str(row)+","+str(joueur.nsac)+")")
                                conn.commit()
                                conn.close()
                                self.pnjs[i].active=False
                        else:
                            self.message="Je n'ai rien pour toi!"
                ftt=self.level[self.yft][self.xft]
                for i in range (len(ftt)):
                    if str(ftt[i]) in self.eact:
                        act=self.eact[str(ftt[i])]
                        exec(act)
        else:
            self.ce=True
        
        

        for j in range(int(self.ytj)-12,int(self.ytj)+13):#dessine les tiles sur tout l'écran
            for i in range(int(self.xtj)-9,int(self.xtj)+10):
                for k in range(0,len(self.level[j][i])):
                    self.win.blit(self.tileset, (i*32+self.x, j*32+self.y),(self.level[j][i][k][0]*32,self.level[j][i][k][1]*32,32,32))

        for k in range(0,len(self.level[int(self.ytj+0.5)][int(self.xtj)])):#regarde ce qu'il y a sur la tiles sous le joueur
            if self.level[int(self.ytj+0.5)][int(self.xtj)][k] in ([3,20],[3,21]):
                if self.lt!=[int(self.ytj+0.5),int(self.xtj)]:
                    self.lt=[int(self.ytj+0.5),int(self.xtj)]
                    if random.randint(0,10)==0:
                        fight=initfight(self.win,False)
                        fight.fight()
                    
                    
        
        for j in [int(self.ytj)-1,int(self.ytj),int(self.ytj)+1]:#efface les tiles superposables autour du joueur
            for i in [int(self.xtj)-1,int(self.xtj),int(self.xtj)+1]:
                for k in range(0,len(self.level[j][i])):
                    if self.collision[self.level[j][i][k][1]][self.level[j][i][k][0]][1]!=1 and (self.collision[self.level[j][i][k][1]][self.level[j][i][k][0]][1]!=2 or (j!=int(self.ytj+0.5) and j!=int(self.ytj+0.8))):
                        self.win.blit(self.tileset, (i*32+self.x, j*32+self.y),(self.level[j][i][k][0]*32,self.level[j][i][k][1]*32,32,32))

        
        for i in range(0,len(self.pnjs)):#affiche et fait bouger les pnjs qui se situent au dessus le joueur
            if int(self.xtj)-19<self.pnjs[i].pos[0]/32<int(self.xtj)+20 and int(self.ytj)-22<self.pnjs[i].pos[1]/32<int(self.ytj)+23:
                trainertilepos=self.pnjs[i].move([self.x,self.y])
                if self.pnjs[i].pos[1]-32+self.y<=self.height/2-32:
                    self.win.blit(self.trainers, (self.pnjs[i].pos[0]-16+self.x,self.pnjs[i].pos[1]-32+self.y),(trainertilepos[0],trainertilepos[1],64,64))
                    
        
        self.win.blit(self.trainers, (self.width/2-32,self.height/2-32),(playertilepos[0],playertilepos[1],64,64))#affiche le personnage du joueur

        
        for i in range(0,len(self.pnjs)):#affiche et fait bouger les pnjs qui se situent sous le joueur
            if int(self.xtj)-19<self.pnjs[i].pos[0]/32<int(self.xtj)+20 and int(self.ytj)-22<self.pnjs[i].pos[1]/32<int(self.ytj)+23:
                trainertilepos=self.pnjs[i].move([self.x,self.y])
                if self.pnjs[i].pos[1]-32+self.y>self.height/2-32:
                    self.win.blit(self.trainers, (self.pnjs[i].pos[0]-16+self.x,self.pnjs[i].pos[1]-32+self.y),(trainertilepos[0],trainertilepos[1],64,64))
        
        for j in [int(self.ytj)-1,int(self.ytj),int(self.ytj)+1]:#dessine les tiles superposables autour du joueur
            for i in [int(self.xtj)-1,int(self.xtj),int(self.xtj)+1]:
                for k in range(0,len(self.level[j][i])):
                    if self.collision[self.level[j][i][k][1]][self.level[j][i][k][0]][1]==1 or (self.collision[self.level[j][i][k][1]][self.level[j][i][k][0]][1]==2 and (j==int(self.ytj+0.5) or j==int(self.ytj+0.8))):
                        self.win.blit(self.tileset, (i*32+self.x, j*32+self.y),(self.level[j][i][k][0]*32,self.level[j][i][k][1]*32,32,32))

        #Vérifie si un PNJ est encore apte au combat sinon déclare les joueur vainqueur
        last=True
        for i in self.pnjs:
            if i.trainer:
                if i.active:
                    last=False
        if last:
            global run
            run=False
            won=True
            while won:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run=False
                        won=False
                self.win.fill((255,255,255))
                self.win.blit(pygame.font.SysFont("monospace", 100).render("Gagné", 1, (0,0,0)), (100, 100))
                pygame.display.update()
                
                
                
                
                
                
                
                pygame.time.delay(2000)
                run = False
                pygame.quit()
                if not joueur.tuto:
                    update2.update(login,'win')
                else :
                    update2.update(login,'win')







        if self.tuto and not self.message:
            if abs(self.y)<20:
                self.message=['Utilise les flèches directionelles','pour te déplacer.']
            elif abs(self.x)<503 and abs(self.y)<145:
                self.message=['Utilise la touche E pour intéragir avec','les objets et les personnages.']
            elif abs(self.x)<720:
                self.message=["Méfie toi des hautes herbes, de nombreux pokémons","sauvages s'y cachent."]
            else:
                self.message=["Tu es maintenant en présence d'un dresseur, si il","te voit, il va te lancer un défi."]



                 #affiche un message si il y à lieu
        if self.message!=False:
            self.win.blit(self.textbox, (0, 0))
            if type(self.message)==list:
                self.win.blit(pygame.font.SysFont("monospace", 15).render(self.message[0], 1, (0,0,0)), (20,20))
                self.win.blit(pygame.font.SysFont("monospace", 15).render(self.message[1], 1, (0,0,0)), (20,40))
            else:
                self.win.blit(pygame.font.SysFont("monospace", 15).render(self.message, 1, (0,0,0)), (20,20))
            pygame.display.update()
            if pygame.mouse.get_pressed()[0]==1:
                if self.cc:
                    self.cc=False
                    self.message=False
            else:
                self.cc=True
                
        

    def hocollision(self,direction):#regarde si la direction vers laquelle le joueur veux se diriger est libre
        global joueur
        global login
        if direction=="L":
            dx=[-0.4]
            dy=[0.4,0.8]
        elif direction=="R":
            dx=[0.4]
            dy=[0.4,0.8]
        elif direction=="D":
            dx=[-0.2,0.2]
            dy=[1]
        else:
            dx=[-0.2,0.2]
            dy=[0.2]
        sblocd=""
        for j in range(0,len(dy)):
            for i in range(0,len(dx)):
                xtja=int(self.xtj+dx[i])
                ytja=int(self.ytj+dy[j])
                let=False
                blocd=[]
                for k in range(0,len(self.level[ytja][xtja])):#tiles potential hitbox
                    blocd.append(self.level[ytja][xtja][k])

                for k in range(0,len(self.pnjs)):#pnj hitbox
                    if int(self.xtj)-19<self.pnjs[k].pos[0]/32<int(self.xtj)+20 and int(self.ytj)-22<self.pnjs[k].pos[1]/32<int(self.ytj)+23:
                        if self.pnjs[k].pos[0]<(self.xtj+dx[i])*32<self.pnjs[k].pos[0]+32 and self.pnjs[k].pos[1]<(self.ytj+dy[j])*32<self.pnjs[k].pos[1]+32:
                            if direction=="L":
                                sblocd+="R"
                            elif direction=="R":
                                sblocd+="L"
                            elif direction=="D":
                                sblocd+="U"
                            else:
                                sblocd+="D"

                for k in range(0,len(blocd)):#rassemble les directions bloquées
                    sblocd+=self.collision[blocd[k][1]][blocd[k][0]][0]

        
        if (direction=="L" and "R" not in sblocd) or (direction=="R" and "L" not in sblocd) or (direction=="U" and "D" not in sblocd) or (direction=="D" and "U" not in sblocd):
            return True

    def pickpokeball(self,ft):#récupere la pokeball au sol et attribue les items
        global joueur
        global login
        del self.level[self.yft][self.xft][len(self.level[self.yft][self.xft])-1]
        objet=random.choice(['Pokeball','Superball','Hyperball','Masterball','Potion','SuperPotion','HyperPotion','PotionMax','Rappel','RappelMax'])
        quant=random.randint(1,3)
        self.message="Vous avez trouvé "+str(quant)+" "+str(objet)
        
        conn = sqlite3.connect('db.db')
        c = conn.cursor()
        
        for row in c.execute("SELECT quantité FROM objets WHERE refsac="+str(joueur.nsac)+" AND Nom='"+objet+"'"):
            row=row[0]+quant
            c.execute("DELETE FROM objets WHERE refsac="+str(joueur.nsac)+" AND Nom='"+objet+"'")
            c.execute("INSERT INTO objets VALUES (NULL,'"+objet+"',"+str(row)+","+str(joueur.nsac)+")")
            
        conn.commit()
        conn.close()

class createpnj:
    def __init__(self,num,fenetre,pos,trainer,ran,direction,vitesse,clas):
        global joueur
        global login
        self.number=num#numéro de l'équipe du PNJ dans la DB
        self.teamnumber=0
        self.fen=fenetre
        self.pos=pos#coordonnées du PNJ
        self.trainer=trainer#détermine si je PNJ est un deresseur
        self.range=(ran)*32#détermine la taille du tour que le PNJ décrit
        self.direction=direction#détermine la direction dans laquelle le pnj est tourné
        self.ranstate=0
        self.vit=vitesse/5#vitesse de déplacement
        self.tclass=clas#type du PNJ
        self.xtp=abs(self.pos[0])/32#coordonnée x du PNJ
        self.ytp=abs(self.pos[1])/32#coordonnée y du PNJ
        self.active=True#si le PNJ peut ineragir
    def move(self,coop):
        global joueur
        global login
        """
        méthode permettant au PNJ de se déplacer
        prend comme argument coop de type list d'entiers contenant les coordonnées du joueur
        """
        self.xtp=abs(self.pos[0])/32#coordonnée x de la tuile du PNJ
        self.ytp=abs(self.pos[1])/32#coordonnée y de la tuile du PNJ
        tilepos=[self.tclass[0]*3*64+128,self.tclass[1]*64*4+64]
        if self.ranstate<self.range and self.active:
            if self.collisionp(self.direction[0],coop):
                if self.direction[0]=="L":
                    self.pos[0]-=self.vit
                    self.ranstate+=self.vit
                    if int((time.time()*4)%2)==0:
                        tilepos=[self.tclass[0]*3*64,self.tclass[1]*64*4+64]
                    else:
                        tilepos=[self.tclass[0]*3*64,self.tclass[1]*64*4+3*64]
                elif self.direction[0]=="R":
                    self.pos[0]+=self.vit
                    self.ranstate+=self.vit
                    if int((time.time()*4)%2)==0:
                        tilepos=[self.tclass[0]*3*64+64,self.tclass[1]*64*4]
                    else:
                        tilepos=[self.tclass[0]*3*64+64,self.tclass[1]*64*4+2*64]
                elif self.direction[0]=="U":
                    self.pos[1]-=self.vit
                    self.ranstate+=self.vit
                    if int((time.time()*4)%2)==0:
                        tilepos=[self.tclass[0]*3*64+2*64,self.tclass[1]*64*4]
                    else:
                        tilepos=[self.tclass[0]*3*64+64,self.tclass[1]*64*4+3*64]
                elif self.direction[0]=="D":
                    self.pos[1]+=self.vit
                    self.ranstate+=self.vit
                    if int((time.time()*4)%2)==0:
                        tilepos=[self.tclass[0]*3*64+2*64,self.tclass[1]*64*4+2*64]
                    else:
                        tilepos=[self.tclass[0]*3*64+2*64,self.tclass[1]*64*4+3*64]
            else:
                if self.direction[0]=="L":
                    tilepos=[self.tclass[0]*3*64,self.tclass[1]*64*4+128]
                elif self.direction[0]=="R":
                    tilepos=[self.tclass[0]*3*64+64,self.tclass[1]*64*4]
                elif self.direction[0]=="U":
                    tilepos=[self.tclass[0]*3*64,self.tclass[1]*64*4]
        else:
            if self.direction[1]==True:
                if self.direction[0]=="L":
                    self.direction[0]="U"
                elif self.direction[0]=="R":
                    self.direction[0]="D"
                elif self.direction[0]=="U":
                    self.direction[0]="R"
                elif self.direction[0]=="D":
                    self.direction[0]="L"
            else:
                if self.direction[0]=="L":
                    self.direction[0]="D"
                elif self.direction[0]=="R":
                    self.direction[0]="U"
                elif self.direction[0]=="U":
                    self.direction[0]="L"
                elif self.direction[0]=="D":
                    self.direction[0]="R"
            self.ranstate=0
        return(tilepos)

    def collisionp(self,direction,xyp):
        global joueur
        global login
        """
        méthode permettant au PNJ vérifier si le joueur est devant
        prend comme argument xyp de type list d'entiers contenant les coordonnées du joueur et direction de type chaine de charactère contenant la direction du PNJ
        """
        dx=0#décalage x de la tuiles en face du PNJ
        dy=0#décalage y de la tuiles en face du PNJ
        vx=[0,0]#décalages x des la tuiles en face du PNJ
        vy=[0,0]#décalages y des la tuiles en face du PNJ
        if direction=="L":
            dx=0.5
            vx[0]=64
        elif direction=="R":
            dx=-0.5
            vx[1]=64
        elif direction=="D":
            dy=-1
            vy[1]=64
        else:
            dy=1
            vy[0]=64
        if -xyp[0]+self.fen.get_width()/2+16*dx-48-vx[1]<self.pos[0]<-xyp[0]+self.fen.get_width()/2+16*dx+16+vx[0] and -xyp[1]+self.fen.get_height()/2+16*dy-16-vy[1]<self.pos[1]<-xyp[1]+self.fen.get_height()/2+16*dy+16+vy[0]:
            if self.trainer:
                self.duel()
        else:
            return True

    def duel(self):
        global login
        """
        méthode permettant au PNJ d'engager le combat contre le joueur
        """
        fight=initfight(self.fen,self)
        fight.fight()

    def createteam(self,typ,lvl):
        global joueur
        global login
        """
        méthode permettant de créer un équipe au PNJ
        pernant comme argument typ de type chaine de charactère contenant le style de dresseur et lvl de type entier pour le lvl du pokémon de l'équipe du PNJ
        """
        
        conn = sqlite3.connect('db.db')
        c = conn.cursor()

        team=1
        for row in c.execute("SELECT * FROM equipe"):
            team+=1
        self.teamnumber=team
        team=str(team)
        c.execute("INSERT INTO equipe(idEquipe) VALUES ("+team+")")#Créer l'équipe du pnj
        for row in c.execute("SELECT * FROM basepokemon WHERE id = "+str(random.randint(1,151))):#Récupère les données du pokemon
            base=row
        npokemon=1
        for row in c.execute("SELECT * FROM pokemon"):
            npokemon+=1
        npokemon=str(npokemon)
        basehp = int(str(base[3]))
        basevitesse = int(str(base[4]))
        baseattack = int(str(base[5]))
        basedefence = int(str(base[6]))
        basehp = int((((int(basehp)*2) + (int((int(sqrt(int(str(base[7])))*100))/4))*int(5))/100)+5+10)
        basevitesse=int((((int(basevitesse)*2) +(int((int(sqrt(int(str(base[7])))*100))/4))*int(5))/100)+5)
        baseattack=int((((int(baseattack)*2) + (int((int(sqrt(int(str(base[7])))*100))/4))*int(5))/100)+5)
        basedefence=int((((int(basedefence)*2) + (int((int(sqrt(int(str(base[7])))*100))/4))*int(5))/100)+5)
        c.execute("INSERT INTO pokemon VALUES ("+npokemon+","+str(base[0])+",'"+base[1]+"','"+base[2]+"',"+str(lvl)+","+str(basehp)+","+str(basehp)+","+str(basevitesse)+","+str(baseattack)+","+str(basedefence)+","+str(base[7])+","+team+")")#+","+str(base[7])######Attribue les données génériques a notre starter 
        nattack=1
        for row in c.execute("SELECT * FROM attaquespokemon"):
            nattack+=1
        c.execute("INSERT INTO attaquespokemon VALUES ("+str(nattack)+",1,"+team+")")#attribue la première attaque au pokemon du pnj
                
        conn.commit()
        conn.close()


 

class initfight(play):
    def __init__(self,fen,pnjo):
        play.__init__(self)
        global joueur
        global login
        
        self.win=fen
        self.pnj=pnjo
        self.Pteam=[]#équipe du joueur
        self.Bteam=[]#pokemon sauvage/équipe du pnj
        #récupère toutes les données concernant le joueur et le PNJ concerné
        conn = sqlite3.connect('db.db')
        c = conn.cursor()
        nbpoke=0
        for row in c.execute("SELECT * FROM pokemon WHERE appartientequipe = "+str(joueur.numteam)):
            nbpoke+=1
            self.Pteam.append([])
            print(row)
            for i in range(0,len(row)):
                self.Pteam[nbpoke-1].append(row[i])
        for i in range(0,len(self.Pteam)):
            self.Pteam[i].append([])
            for row in c.execute("SELECT Attaques_idAttaques FROM attaquespokemon WHERE appartientpokemon = "+str(i+1)):
                self.Pteam[i][len(self.Pteam[i])-1].append(row[0])
        for i in range(0,len(self.Pteam)):
            for j in range(0,len(self.Pteam[i][len(self.Pteam[i])-1])):
                for row in c.execute("SELECT * FROM attaques WHERE idAttaques = "+str(self.Pteam[i][len(self.Pteam[i])-1][j])):
                    self.Pteam[i][len(self.Pteam[i])-1][j]=[]
                    for k in range(0,len(row)):
                        self.Pteam[i][len(self.Pteam[i])-1][j].append(row[k])
        self.bag=[]
        for i in ['Pokeball','Superball','Hyperball','Masterball','Potion','SuperPotion','HyperPotion','PotionMax','Rappel','RappelMax']:
            for row in c.execute("SELECT * FROM objets WHERE refsac = "+str(joueur.nsac)+" AND Nom='"+i+"'"):
                self.bag.append([row[1],row[2]])
        if self.pnj!=False:
            if pnjo.teamnumber==0:#verifie si le pnj possède une équipe, si non la créer
                moy=0
                for i in range(0,len(self.Pteam)):
                    moy+=self.Pteam[i][4]
                moy=int(moy/(i+1))
                self.pnj.createteam('normal',abs(int(random.randint(moy-10,moy)))+1)

            nbpoke=0
            for row in c.execute("SELECT * FROM pokemon WHERE appartientequipe = "+str(self.pnj.teamnumber)):
                nbpoke+=1
                self.Bteam.append([])
                for i in range(0,len(row)):
                    self.Bteam[nbpoke-1].append(row[i])
            for i in range(0,len(self.Bteam)):
                self.Bteam[i].append([])
                for row in c.execute("SELECT Attaques_idAttaques FROM attaquespokemon WHERE appartientpokemon = "+str(i+1)):
                    self.Bteam[i][len(self.Bteam[i])-1].append(row[0])
            for i in range(0,len(self.Bteam)):
                for j in range(0,len(self.Bteam[i][len(self.Bteam[i])-1])):
                    for row in c.execute("SELECT * FROM attaques WHERE idAttaques = "+str(self.Bteam[i][len(self.Bteam[i])-1][j])):
                        self.Bteam[i][len(self.Bteam[i])-1][j]=[]
                        for k in range(0,len(row)):
                            self.Bteam[i][len(self.Bteam[i])-1][j].append(row[k])
        else:
            print(self.Pteam)
            moy=int(self.Pteam[0][4])+random.randint(-2,2)
            poke=random.randint(1,151)
            for row in c.execute("SELECT * FROM basepokemon WHERE id="+str(poke)):
                pass
            lvl = abs(int(random.randint(moy-10,moy)))+1
            basehp = int(str(row[3]))
            basevitesse = int(str(row[4]))
            baseattack = int(str(row[5]))
            basedefence = int(str(row[6]))
            basehp = int((((int(basehp)*2) + (int((int(sqrt(int(str(row[7])))*100))/4))*int(lvl))/100)+5+10)
            basevitesse=int((((int(basevitesse)*2) +(int((int(sqrt(int(str(row[7])))*100))/4))*int(lvl))/100)+5)
            baseattack=int((((int(baseattack)*2) + (int((int(sqrt(int(str(row[7])))*100))/4))*int(lvl))/100)+5)
            basedefence=int((((int(basedefence)*2) + (int((int(sqrt(int(str(row[7])))*100))/4))*int(lvl))/100)+5)
            
            self.Bteam.append([0,row[0],row[1],row[2],lvl,basehp,basehp,basevitesse,baseattack,basedefence,row[7],joueur.numteam,[[2, 'Absorb', 20, 100, 'grass', 10]]])#gen du pokemon a randomiser
        conn.close()     

        
        


        #Chargement des images
        for i in range(0,len(self.Pteam)):
            poke=str(self.Pteam[i][1])
            img=pygame.image.load("./BattleScene/icons/"+poke+".png")
            self.Pteam[i].append(pygame.transform.scale(img,(img.get_width()*2,img.get_height()*2)))
            while len(poke)<3:
                poke='0'+poke
            img=pygame.image.load("./BattleScene/back/"+poke+".gif")
            self.Pteam[i].append(pygame.transform.scale(img,(img.get_width()*3,img.get_height()*3)))
        
        for i in range(0,len(self.Bteam)):
            poke=str(self.Bteam[i][1])
            img=pygame.image.load("./BattleScene/icons/"+poke+".png")
            self.Bteam[i].append(pygame.transform.scale(img,(img.get_width()*2,img.get_height()*2)))
            while len(poke)<3:
                poke='0'+poke
            img=pygame.image.load("./BattleScene/front/"+poke+".gif")
            self.Bteam[i].append(pygame.transform.scale(img,(img.get_width()*2,img.get_height()*2)))

        

        
        self.bg=pygame.image.load("./BattleScene/Font/Grass 2.png")
        self.bg=pygame.transform.scale(self.bg, (self.win.get_width(), self.bg.get_height()))
        self.menu=pygame.image.load("./BattleScene/battlemenu.png")
        self.attackmenu=pygame.image.load("./BattleScene/attackmenu.png")
        self.textbox=pygame.image.load("./BattleScene/textbox.png")
        self.textbox=pygame.transform.scale(self.textbox, (self.win.get_width(),96))
        self.fightselect=pygame.image.load("./BattleScene/fightselect.png")
        self.optionselect=pygame.image.load("./BattleScene/optionselect.png")
        self.attackselect=pygame.image.load("./BattleScene/attackselect.png")
        self.cancelselect=pygame.image.load("./BattleScene/cancelselect.png")
        self.pokemenu=pygame.image.load("./BattleScene/pokemenu.png")
        self.pokeframe=pygame.image.load("./BattleScene/pokeframe.png")
        self.pokeframeselect=pygame.image.load("./BattleScene/pokeframeselect.png")
        self.activepokeframeselect=pygame.image.load("./BattleScene/activepokeframeselect.png")
        self.emptyattackslot=pygame.image.load("./BattleScene/emptyattackslot.png")
        self.hpbox=pygame.image.load("./BattleScene/hpbox.png")
        self.attacksbg=pygame.image.load("./BattleScene/attacksbg.png")
        self.menubag=pygame.image.load("./BattleScene/menubag.png")
        self.items=pygame.image.load("./BattleScene/items.png")
        self.blankbottomscreen=pygame.image.load("./BattleScene/blankbottomscreen.jpg")



        self.wmenu="menu"#indique le menu choisi par le joueur
        self.select=""#variable tempon contenant le dernier menu survolé par l'utilisateur
        self.sel="soin"#indique la position du sac, si il est en mode soins ou balls
        self.bsel=""#indique la position temporaire du sac, si il est en mode soins ou balls
        self.cc=True#Vrai si l'utilisateur peut cliquer
        self.tsoin=False#Vrai si l'utilisateur veux utiliser un objet de soin
        
    def getstats(self,chosen):
        conn = sqlite3.connect('db.db')
        c = conn.cursor()
        for row in c.execute("SELECT * FROM basepokemon WHERE id = "+str(chosen)):#Récupère les données du pokemon generique corrspondant à notre starter
            base=row
        npokemon=1
        basehp = int(str(base[3]))
        basevitesse = int(str(base[4]))
        baseattack = int(str(base[5]))
        basedefence = int(str(base[6]))
        conn.commit()
        conn.close()
        stats = [basehp,basevitesse,baseattack,basedefence]
        return stats
    
    def fight(self):
        global joueur
        global login
        global run
        replace=False
        keepfight=True
        while keepfight and run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepfight = False
                    run=False
            
            
            self.win.fill((0,0,0))
            self.win.blit(self.bg, (0, -50))
            

            #affiche toutes les données relatives au pokemon adverse
            self.win.blit(self.Bteam[0][len(self.Bteam[0])-1],(385-self.Bteam[0][len(self.Bteam[0])-1].get_width()/2,135-self.Bteam[0][len(self.Bteam[0])-1].get_height()))
            self.win.blit(self.hpbox, (0, 20),(516,0,240,60))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(self.Bteam[0][2], 1, (0,0,0)), (5, 30))#a remplacer
            lvl=str(self.Bteam[0][4])
            if len(lvl)==1:#Affiche le lvl
                self.win.blit(self.hpbox, (164, 36),(self.numbers(lvl[0]),166,16,14))
            elif len(lvl)==2:
                self.win.blit(self.hpbox, (164, 36),(self.numbers(lvl[0]),166,16,14))
                self.win.blit(self.hpbox, (181, 36),(self.numbers(lvl[1]),166,16,14))
            else:
                self.win.blit(self.hpbox, (164, 36),(self.numbers(lvl[0]),166,16,14))
                self.win.blit(self.hpbox, (181, 36),(self.numbers(lvl[1]),166,16,14))
                self.win.blit(self.hpbox, (198, 36),(self.numbers(lvl[2]),166,16,14))

            if self.Bteam[0][5]>self.Bteam[0][6]/2:
                self.win.blit(self.hpbox, (100, 58),(0,166,96*self.Bteam[0][5]/self.Bteam[0][6],14))
            elif self.Bteam[0][5]>self.Bteam[0][6]/4:
                self.win.blit(self.hpbox, (100, 58),(0,182,96*self.Bteam[0][5]/self.Bteam[0][6],14))
            else:
                self.win.blit(self.hpbox, (100, 58),(0,198,96*self.Bteam[0][5]/self.Bteam[0][6],14))

            #affiche toutes les données relatives au pokemon allié
            self.win.blit(self.Pteam[0][len(self.Pteam[0])-1],(100-self.Pteam[0][len(self.Pteam[0])-1].get_width()/2,280-self.Pteam[0][len(self.Pteam[0])-1].get_height()))
            self.win.blit(self.hpbox, (270, 140),(516,82,240,82))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(self.Pteam[0][2], 1, (0,0,0)), (300, 150))#a remplacer
            lvl=str(self.Pteam[0][4])
            if len(lvl)==1:#Affiche le lvl du pokémon allié
                self.win.blit(self.hpbox, (458, 156),(self.numbers(lvl[0]),166,16,14))
            elif len(lvl)==2:
                self.win.blit(self.hpbox, (458, 156),(self.numbers(lvl[0]),166,16,14))
                self.win.blit(self.hpbox, (475, 156),(self.numbers(lvl[1]),166,16,14))
            else:
                self.win.blit(self.hpbox, (458, 156),(self.numbers(lvl[0]),166,16,14))
                self.win.blit(self.hpbox, (475, 156),(self.numbers(lvl[1]),166,16,14))
                self.win.blit(self.hpbox, (492, 156),(self.numbers(lvl[2]),166,16,14))
                
            hp=str(self.Pteam[0][5])
            if len(hp)==1:#affiche les hp du pokémon allié
                self.win.blit(self.hpbox, (428, 195),(self.numbers(hp[0]),166,16,14))
            elif len(hp)==2:
                self.win.blit(self.hpbox, (428, 195),(self.numbers(hp[1]),166,16,14))
                self.win.blit(self.hpbox, (410, 195),(self.numbers(hp[0]),166,16,14))
            else:
                self.win.blit(self.hpbox, (428, 195),(self.numbers(hp[2]),166,16,14))
                self.win.blit(self.hpbox, (410, 195),(self.numbers(hp[1]),166,16,14))
                self.win.blit(self.hpbox, (392, 195),(self.numbers(hp[0]),166,16,14))

            hpmax=str(self.Pteam[0][6])
            if len(hpmax)==1:#affiche les hpmax du pokémon allié
                self.win.blit(self.hpbox, (458, 195),(self.numbers(hpmax[0]),166,16,14))
            elif len(hpmax)==2:
                self.win.blit(self.hpbox, (458, 195),(self.numbers(hpmax[0]),166,16,14))
                self.win.blit(self.hpbox, (475, 195),(self.numbers(hpmax[1]),166,16,14))
            else:
                self.win.blit(self.hpbox, (458, 195),(self.numbers(hpmax[0]),166,16,14))
                self.win.blit(self.hpbox, (475, 195),(self.numbers(hpmax[1]),166,16,14))
                self.win.blit(self.hpbox, (492, 195),(self.numbers(hpmax[2]),166,16,14))


            if self.Pteam[0][5]>self.Pteam[0][6]/2:
                self.win.blit(self.hpbox, (394, 178),(0,166,96*self.Pteam[0][5]/self.Pteam[0][6],14))
            elif self.Pteam[0][5]>self.Pteam[0][6]/4:
                self.win.blit(self.hpbox, (394, 178),(0,182,96*self.Pteam[0][5]/self.Pteam[0][6],14))
            else:
                self.win.blit(self.hpbox, (394, 178),(0,198,96*self.Pteam[0][5]/self.Pteam[0][6],14))
                   
              
            
            self.win.blit(self.textbox, (0, 736-406-96))

            if self.Pteam[0][5]==0 and "pokemon" not in self.wmenu:
                self.wmenu="pokemenu"

            if replace:#En cas de capture et d'equipe complète
                self.win.blit(self.textbox, (0, 736-406-96))
                self.win.blit(pygame.font.SysFont("monospace", 15).render("Choisissez ou non quel pokémon voulez vous remplacer", 1, (0,0,0)), (20,736-490))
                if "pokemon" in self.wmenu:
                    self.Pteam[int(self.wmenu[7])]=self.Bteam[0]
                    keepfight=False
                    self.wmenu=False
                elif self.wmenu=="menu":
                    keepfight=False
                self.wmenu="pokemenu"
            played=False
            attack=False
            if self.wmenu=="menu":#si le menu qui doit etre affiché est le principal
                self.bmenu()
            elif self.wmenu=="fight":#si le menu qui doit etre affiché est le menu des attaques
                self.bfight()
            elif self.wmenu=="pokemenu":#si le menu qui doit etre affiché est le menu des pokémons
                self.bpokemenu()
            elif self.wmenu=="bag":#si le menu qui doit etre affiché est le menu du sac
                self.bbag()
            elif "pokemon" in self.wmenu:#si un pokémon à été sélectionné
                if self.tsoin==False:
                    if self.Pteam[int(self.wmenu[7])][5]==0:
                        self.wmessage("ce pokemon est KO, il ne peut plus combattre")
                        self.wmenu="pokemenu"
                    elif int(self.wmenu[7])==0:
                        self.wmessage("impossible, ce pokémon est déja sur le terrain")
                        self.wmenu="pokemenu"
                    else:
                        if self.Pteam[0][5]!=0:
                            played=True
                        temp=self.Pteam[int(self.wmenu[7])]
                        self.Pteam[int(self.wmenu[7])]=self.Pteam[0]
                        self.Pteam[0]=temp
                        self.wmenu="menu"
                else:
                    menu=self.wmenu
                    if self.tsoin[4] in ["0","1","2","3"]:
                        if self.Pteam[int(self.wmenu[7])][5]>0:
                            if self.Pteam[int(self.wmenu[7])][5]!=self.Pteam[int(self.wmenu[7])][6]:
                                if self.tsoin[4]=="0":
                                    self.Pteam[int(self.wmenu[7])][5]+=25
                                    played=True
                                elif self.tsoin[4]=="1":
                                    self.Pteam[int(self.wmenu[7])][5]+=50
                                    played=True
                                elif self.tsoin[4]=="2":
                                    self.Pteam[int(self.wmenu[7])][5]+=200
                                    played=True
                                elif self.tsoin[4]=="3":
                                    self.Pteam[int(self.wmenu[7])][5]+=self.Pteam[int(self.wmenu[7])][6]
                                    played=True
                                if self.Pteam[int(self.wmenu[7])][5]>self.Pteam[int(self.wmenu[7])][6]:
                                    self.Pteam[int(self.wmenu[7])][5]=self.Pteam[int(self.wmenu[7])][6]
                                self.bag[int(self.tsoin[4])+4][1]-=1
                                self.tsoin=False
                            else:
                                self.wmessage("Ce pokémon est déja en pleine santée")
                                menu="pokemenu"
                        else:
                            self.wmessage("Ce pokémon est KO")
                            menu="pokemenu"
                    else:
                        if self.Pteam[int(self.wmenu[7])][5]==0:
                            if self.tsoin[4]=="4":
                                self.Pteam[int(self.wmenu[7])][5]=int(self.Pteam[int(self.wmenu[7])][6]/2)
                                played=True
                            elif self.tsoin[4]=="5":
                                self.Pteam[int(self.wmenu[7])][5]=self.Pteam[int(self.wmenu[7])][6]
                                played=True
                            self.bag[int(self.tsoin[4])+4][1]-=1
                            self.tsoin=False
                        else:
                            self.wmessage("Ce pokémon n'est pas KO")
                            menu="pokemenu"
                    self.wmenu=menu
                    
            elif "attack" in self.wmenu:#si une attaque à été sélectionnée
                played=True
                attack=True
            elif "soin" in self.wmenu:#si un soin à été sélectionné
                if self.bag[int(self.wmenu[4])+4][1]>0:
                    self.tsoin=self.wmenu
                    self.wmenu="pokemenu"
                else:
                    self.wmessage("Vous ne possédez pas de "+self.bag[int(self.wmenu[4])+4][0])
                    self.wmenu="bag"
            elif "ball" in self.wmenu:#si une ball à été séléctionnée
                if self.bag[int(self.wmenu[4])][1]>0:
                    if self.pnj!=False:
                        self.wmessage("vous ne pouvez pas capturer un pokémon qui appartient à un dresseur")
                        self.wmenu="bag"
                    else:
                        self.bag[int(self.wmenu[4])][1]-=1
                        if self.wmenu[4]=="0":
                            luck=random.random()<0.25
                        elif self.wmenu[4]=="1":
                            luck=random.random()<0.50
                        elif self.wmenu[4]=="2":
                            luck=random.random()<0.75
                        else:
                            luck=True
                        if luck:
                            self.wmessage("vous avez capturé le pokémon")#ajouter à l'équipe si place sinon proposer d'enlever un pokémon
                            if len(self.Pteam)<6:
                                self.Pteam.append(self.Bteam[0])
                                keepfight=False
                            else:
                                replace=True
                        else:
                            self.wmessage("le pokémon s'est échapé!")
                            self.wmenu="menu"
                            played=True
                else:
                    self.wmessage("Vous ne possédez pas de "+self.bag[int(self.wmenu[4])][0])
                    self.wmenu="bag"
            elif self.wmenu=="run":#si le joueur tente de fuir le combat
                if self.pnj==False:
                    if random.random()>0.8:
                        keepfight=False
                    else:
                        self.played=True
                else:
                    self.wmessage("vous ne pouvez fuir le combat contre un dresseur")
                self.wmenu="menu"
            else:
                self.wmenu="menu"
                

            if played==True:#quand le joueur à joué
                if attack==True:#si le joueur à choisi d'attaquer
                    if self.Pteam[0][7]>=self.Bteam[0][7]:
                        damage=int(( ( ( (2*int(self.Pteam[0][4])/5) +2) *(int(self.Pteam[0][12][int(self.wmenu[6])-1][2]))*int(self.Pteam[0][8])/int(self.Pteam[0][9])) /50)+2)
                        damage=damage+random.randint(-int(damage/4),damage*2)
                        self.wmessage("Vous infligez "+str(damage)+" points de dégats")
                        self.Bteam[0][5]-=damage+random.randint(-int(damage/4),damage*2)
                        if self.Bteam[0][5]>0:
                            damage = int(( ( ( (2*int(self.Pteam[0][4])/5) +2) *(int(self.Bteam[0][12][0][2]))*int(self.Bteam[0][8])/int(self.Bteam[0][9])) /50)+2)
                            damage=damage+random.randint(-int(damage/4),damage*2)
                            self.wmessage("Le pokemon ennemi vous inflige "+str(damage)+" points de dégats")
                            self.Pteam[0][5]-=damage+random.randint(-int(damage/4),damage*2)
                        else:
                            self.Bteam[0][5]=0
                    else:
                        damage = int(( ( ( (2*int(self.Pteam[0][4])/5) +2) *(int(self.Bteam[0][12][0][2]))*int(self.Bteam[0][8])/int(self.Bteam[0][9])) /50)+2)
                        damage=damage+random.randint(-int(damage/4),damage*2)
                        self.wmessage("Le pokemon ennemi vous inflige "+str(damage)+" points de dégats")
                        self.Pteam[0][5]-=damage+random.randint(-int(damage/4),damage*2)
                        if self.Pteam[0][5]>0:
                            damage=int(( ( ( (2*int(self.Pteam[0][4])/5) +2) *(int(self.Pteam[0][12][int(self.wmenu[6])-1][2]))*int(self.Pteam[0][8])/int(self.Pteam[0][9])) /50)+2)
                            damage=damage+random.randint(-int(damage/4),damage*2)
                            self.wmessage("Vous infligez "+str(damage)+" points de dégats")
                            self.Bteam[0][5]-=damage+random.randint(-int(damage/4),damage*2)
                        else:
                            self.Pteam[0][5]=0
                else:
                    self.wmessage("Le pokemon ennemi vous inflige "+str(self.Bteam[0][12][0][2])+" points de dégats")
                    self.Pteam[0][5]-=self.Bteam[0][12][0][2]
                if self.Pteam[0][5]<0:
                    self.Pteam[0][5]=0
                if self.Bteam[0][5]<0:
                    self.Bteam[0][5]=0

                up=0
                for i in range(0,len(self.Pteam)):
                    up+=self.Pteam[i][5]
                if up==0:
                    lost=True
                    while lost:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                keepfight = False
                                run=False
                                lost=False
                        self.win.fill((255,255,255))
                        self.win.blit(pygame.font.SysFont("monospace", 100).render("Perdu", 1, (0,0,0)), (100, 100))
                        pygame.display.update()
                        #################################################







                        pygame.time.delay(2000)
                        run = False
                        pygame.quit()
                        if not joueur.tuto:
                            update2.update(login,'lose')
                        else :
                            launcherPOO.launch(login)











                        #############################################
                up=0
                for i in range(0,len(self.Bteam)):
                    up+=self.Bteam[i][5]
                if up==0:
                    keepfight=False
                    if self.pnj!=False:
                        self.pnj.active=False
                self.wmenu="menu"
            pygame.display.update()
        #Sauvegarde dans la database
        if run:
            conn = sqlite3.connect('db.db')
            c = conn.cursor()
            if self.Bteam[0][5]==0:
                if self.pnj!=False:
                    c.execute("DELETE FROM pokemon WHERE appartientequipe="+str(self.pnj.teamnumber))
                self.Pteam[0][4]+=1
                stats = self.getstats(self.Pteam[0][1])
                self.Pteam[0][6]=int((((int(stats[0])*2) + (int((int(sqrt(self.Pteam[0][10])*100))/4))*int(self.Pteam[0][4]))/100)+self.Pteam[0][4]+10)
                self.Pteam[0][5]=self.Pteam[0][6]
                self.Pteam[0][7]=int((((int(stats[1])*2) +(int((int(sqrt(self.Pteam[0][10])*100))/4))*int(self.Pteam[0][4]))/100)+5)
                self.Pteam[0][8]=int((((int(stats[2])*2) + (int((int(sqrt(self.Pteam[0][10])*100))/4))*int(self.Pteam[0][4]))/100)+5)
                self.Pteam[0][9]=int((((int(stats[3])*2) + (int((int(sqrt(self.Pteam[0][10])*100))/4))*int(self.Pteam[0][4]))/100)+5)
                self.wmessage("Vous remportez le combat,"+self.Pteam[0][2]+" monte au niveau "+str(self.Pteam[0][4])+"!")
                if joueur.tuto :
                    self.Pteam[0][6]=self.Pteam[0][6]+200
                    self.Pteam[0][5] = self.Pteam[0][6]
                    self.Pteam[0][7] = self.Pteam[0][7]*4
                if "," in self.Pteam[0][3]:
                    types=[self.Pteam[0][3][:self.Pteam[0][3].index(',')],self.Pteam[0][3][self.Pteam[0][3].index(',')+1:]]
                else:
                    types=[self.Pteam[0][3]]
                att=0
                for i in types:
                    #print(i)
                    for row in c.execute("SELECT idAttaques FROM attaques WHERE Type='"+str(i)+"' AND skilllevel="+str(self.Pteam[0][4])):
                        att=row[0]
                #print(att)
                if att!=0:
                    if len(self.Pteam[0][12])<4:
                        self.Pteam[0][12].append([])
                        for row in c.execute("SELECT * FROM attaques WHERE idAttaques = "+str(att)):
                            for k in range(0,len(row)):
                                self.Pteam[0][12][len(self.Pteam[0][12])-1].append(row[k])
                        self.wmessage(self.Pteam[0][2]+" apprends "+self.Pteam[0][12][len(self.Pteam[0][12])-1][1])
                    else:
                        for row in c.execute("SELECT Nom FROM attaques WHERE idAttaques = "+str(att)):
                            row
                        self.wmessage(self.Pteam[0][2]+" peut apprendre "+row[0])
                        selattack=True
                        self.wmenu="fight"
                        while selattack:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    keepfight = False
                                    run=False
                            self.win.blit(self.textbox, (0, 736-406-96))
                            self.win.blit(pygame.font.SysFont("monospace", 15).render("Voulez vous remplacer une attaque par "+row[0]+" ?", 1, (0,0,0)), (20,736-490))
                            self.bfight()
                            if "attack" in self.wmenu:
                                self.Pteam[0][12][int(self.wmenu[6])-1]=[]
                                for row in c.execute("SELECT * FROM attaques WHERE idAttaques = "+str(att)):
                                    for k in range(0,len(row)):
                                        self.Pteam[0][12][int(self.wmenu[6])-1].append(row[k])
                                selattack=False
                            elif self.wmenu=="menu":
                                selattack=False
                            pygame.display.update()
                                
                                
                            


                
            c.execute("DELETE FROM pokemon WHERE appartientequipe="+str(joueur.numteam))
            for i in range(0,len(self.Pteam)):
                npokemon=1
                for row in c.execute("SELECT * FROM pokemon"):
                    npokemon+=1
                npokemon=str(npokemon)
                
                c.execute("INSERT INTO pokemon VALUES ("+npokemon+","+str(self.Pteam[i][1])+",'"+self.Pteam[i][2]+"','"+self.Pteam[i][3]+"',"+str(self.Pteam[i][4])+","+str(self.Pteam[i][5])+","+str(self.Pteam[i][6])+","+str(self.Pteam[i][7])+","+str(self.Pteam[i][8])+","+str(self.Pteam[i][9])+","+str(self.Pteam[i][10])+","+str(joueur.numteam)+")")
                c.execute("DELETE FROM attaquespokemon WHERE appartientpokemon="+npokemon)

                for j in range(0,len(self.Pteam[i][12])):
                    c.execute("INSERT INTO attaquespokemon VALUES (NULL,"+str(self.Pteam[i][12][j][0])+","+npokemon+")")#attribue les attaques aux pokemons


            c.execute("DELETE FROM objets WHERE refsac="+str(joueur.nsac))
            for i in self.bag:
                    c.execute("INSERT INTO objets VALUES (NULL,'"+i[0]+"',"+str(i[1])+","+str(joueur.nsac)+")")




            conn.commit()
            conn.close()
        

        
            
    def bmenu(self):
        global joueur
        global login
        self.win.blit(self.menu,(0,736-406))
        self.win.blit(self.Pteam[0][len(self.Pteam[0])-2],(160,455))
        if 736-406<pygame.mouse.get_pos()[1]<736-110:
            if int((time.time()*1.5)%2)==0:
                self.win.blit(self.fightselect, (40, 736-406+80))
                self.select="fight"
        elif pygame.mouse.get_pos()[1]>736-110:
            if pygame.mouse.get_pos()[0]<512/3:
                if int((time.time()*1.5)%2)==0:
                    self.win.blit(self.optionselect, (0, 736-100))
                    self.select="bag"
            elif pygame.mouse.get_pos()[0]<512*2/3:
                if int((time.time()*1.5)%2)==0:
                    self.win.blit(self.optionselect, (512/3, 736-100))
                    self.select="run"
            else:
                if int((time.time()*1.5)%2)==0:
                    self.win.blit(self.optionselect, (512*2/3, 736-100))
                    self.select="pokemenu"
        else:
            self.select="menu"
        if pygame.mouse.get_pressed()[0]==1:
            if self.cc:
                self.cc=False
                self.wmenu=self.select
        else:
            self.cc=True

    def bfight(self):
        global joueur
        global login
        nbattack=len(self.Pteam[0][len(self.Pteam[0])-3])
        self.win.blit(self.attackmenu,(0,736-406))
        
        #première attaque
        loc=self.bgattacks(self.Pteam[0][12][0][4])
        self.win.blit(self.attacksbg, (4, 736-406+48),(loc[0],loc[1],248,110))
        self.win.blit(pygame.font.SysFont("monospace", 20).render(self.Pteam[0][12][0][1], 1, (0,0,0)), (80, 736-406+70))#a remplacer
        if nbattack>1:
            loc=self.bgattacks(self.Pteam[0][12][1][4])
            self.win.blit(self.attacksbg, (512/2+6, 736-406+48),(loc[0],loc[1],248,110))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(self.Pteam[0][12][1][1], 1, (0,0,0)), (350, 736-406+70))#a remplacer
        else:
            self.win.blit(self.emptyattackslot, (512/2+6, 736-406+48))
        if nbattack>2:
            loc=self.bgattacks(self.Pteam[0][12][2][4])
            self.win.blit(self.attacksbg, (4, 736-406+172),(loc[0],loc[1],248,110))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(self.Pteam[0][12][2][1], 1, (0,0,0)), (80, 736-406+200))#a remplacer
        else:
            self.win.blit(self.emptyattackslot, (4, 736-406+172))
        if nbattack>3:
            loc=self.bgattacks(self.Pteam[0][12][3][4])
            self.win.blit(self.attacksbg, (512/2+6, 736-406+172),(loc[0],loc[1],248,110))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(self.Pteam[0][12][3][1], 1, (0,0,0)), (350, 736-406+200))#a remplacer
        else:
            self.win.blit(self.emptyattackslot, (512/2+6, 736-406+172))
        
        if 736-406<pygame.mouse.get_pos()[1]<736-240:
            if pygame.mouse.get_pos()[0]<512/2:
                if int((time.time()*1.5)%2)==0:
                    self.win.blit(self.attackselect, (2, 736-360))
                self.select="attack1"
            else:
                if int((time.time()*1.5)%2)==0:
                    self.win.blit(self.attackselect, (512/2+2, 736-360))
                self.select="attack2"
        elif 736-240<pygame.mouse.get_pos()[1]<736-110:
            if pygame.mouse.get_pos()[0]<512/2:
                if int((time.time()*1.5)%2)==0:
                    self.win.blit(self.attackselect, (2, 736-236))
                self.select="attack3"
            else:
                if int((time.time()*1.5)%2)==0:
                    self.win.blit(self.attackselect, (512/2+2, 736-236))
                self.select="attack4"
        elif pygame.mouse.get_pos()[1]>736-110:
            if int((time.time()*1.5)%2)==0:
                self.win.blit(self.cancelselect, (10, 736-100))
            self.select="menu"
        else:
            self.select="fight"
        
        if "attack" in self.select:
            if int(self.select[6])>len(self.Pteam[0][12]):
                self.select="fight"


        
        if pygame.mouse.get_pressed()[0]==1:
            if self.cc:
                self.cc=False
                self.wmenu=self.select
        else:
            self.cc=True

    def bgattacks(self,typ):
        global joueur
        global login
        if typ=="ground":
            return [0,0]
        elif typ=="fight":
            return [0,112]
        elif typ=="normal":
            return [0,224]
        elif typ=="steel":
            return [0,336]
        elif typ=="flying":
            return [0,448]
        elif typ=="water":
            return [250,0]
        elif typ=="psycho":
            return [250,112]
        elif typ=="poison":
            return [250,224]
        elif typ=="rock":
            return [250,336]
        elif typ=="fire":
            return [250,448]
        elif typ=="ghost":
            return [250,0]
        elif typ=="grass":
            return [500,112]
        elif typ=="electric":
            return [500,224]
        elif typ=="dragon":
            return [500,336]
        elif typ=="ice":
            return [500,448]
        elif typ=="bug":
            return [750,0]
        elif typ=="dark":
            return [750,112]
        else:
            return [750,224]
        

    def bpokemenu(self):
        global joueur
        global login
        nbpoke=len(self.Pteam)
        self.win.blit(self.pokemenu,(0,736-406))
        self.win.blit(pygame.font.SysFont("monospace", 20).render(self.Pteam[0][2], 1, (0,0,0)), (90, 350))#a remplacer
        if nbpoke>1:
            self.win.blit(self.pokeframe, (512/2+2, 736-384))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(self.Pteam[1][2], 1, (0,0,0)), (340, 366))#a remplacer
        if nbpoke>2:
            self.win.blit(self.pokeframe, (2, 736-304))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(self.Pteam[2][2], 1, (0,0,0)), (90, 446))#a remplacer
        if nbpoke>3:
            self.win.blit(self.pokeframe, (512/2+2, 736-288))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(self.Pteam[1][2], 1, (0,0,0)), (340, 462))#a remplacer
        if nbpoke>4:
            self.win.blit(self.pokeframe, (2, 736-208))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(self.Pteam[2][2], 1, (0,0,0)), (90, 542))#a remplacer
        if nbpoke>5:
            self.win.blit(self.pokeframe, (512/2+2, 736-192))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(self.Pteam[1][2], 1, (0,0,0)), (340, 558))#a remplacer
            
        if 736-406<pygame.mouse.get_pos()[1]<736-300:
            if pygame.mouse.get_pos()[0]<512/2:
                self.win.blit(self.activepokeframeselect, (2, 736-406))
                self.win.blit(pygame.font.SysFont("monospace", 20).render(self.Pteam[0][2], 1, (0,0,0)), (90, 350))#a remplacer
                self.select="pokemon0"
            elif nbpoke>1:
                self.win.blit(self.pokeframeselect, (512/2, 736-390))
                self.win.blit(pygame.font.SysFont("monospace", 20).render(self.Pteam[1][2], 1, (0,0,0)), (340, 366))#a remplacer
                self.select="pokemon1"
        elif 736-300<pygame.mouse.get_pos()[1]<736-210:
            if pygame.mouse.get_pos()[0]<512/2 and nbpoke>2:
                self.win.blit(self.pokeframeselect, (0, 736-310))
                self.win.blit(pygame.font.SysFont("monospace", 20).render(self.Pteam[2][2], 1, (0,0,0)), (90, 446))#a remplacer
                self.select="pokemon2"
            elif nbpoke>3:
                self.win.blit(self.pokeframeselect, (512/2, 736-294))
                self.win.blit(pygame.font.SysFont("monospace", 20).render(self.Pteam[1][2], 1, (0,0,0)), (340, 462))#a remplacer
                self.select="pokemon3"
        elif 736-210<pygame.mouse.get_pos()[1]<736-100:
            if pygame.mouse.get_pos()[0]<512/2 and nbpoke>4:
                self.win.blit(self.pokeframeselect, (0, 736-214))
                self.win.blit(pygame.font.SysFont("monospace", 20).render(self.Pteam[2][2], 1, (0,0,0)), (90, 542))#a remplacer
                self.select="pokemon4"
            elif nbpoke>5:
                self.win.blit(self.pokeframeselect, (512/2, 736-198))
                self.win.blit(pygame.font.SysFont("monospace", 20).render(self.Pteam[1][2], 1, (0,0,0)), (340, 558))#a remplacer
                self.select="pokemon5"
        elif pygame.mouse.get_pos()[1]>736-100 and pygame.mouse.get_pos()[0]>512-130:
            if int((time.time()*2)%2)==0:
                self.win.blit(self.cancelselect, (10, 736-100))
            if self.tsoin==False:
                self.select="menu"
            else:
                self.select="bag"
        else:
            self.select="pokemenu"


        #corriger avec la vraie police d'écriture######################################################################################################################################################
        self.win.blit(self.Pteam[0][len(self.Pteam[0])-2],(30,320))
        self.win.blit(pygame.font.SysFont("monospace", 20).render(str(self.Pteam[0][4]), 1, (0,0,0)), (40, 395))
        self.win.blit(pygame.font.SysFont("monospace", 20).render(str(self.Pteam[0][5]), 1, (0,0,0)), (130, 395))
        self.win.blit(pygame.font.SysFont("monospace", 20).render(str(self.Pteam[0][6]), 1, (0,0,0)), (190, 395))
        if nbpoke>1:
            self.win.blit(self.Pteam[1][len(self.Pteam[1])-2],(286,336))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(str(self.Pteam[1][4]), 1, (0,0,0)), (296, 412))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(str(self.Pteam[1][5]), 1, (0,0,0)), (130+256, 412))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(str(self.Pteam[1][6]), 1, (0,0,0)), (190+256, 412))
        if nbpoke>2:
            self.win.blit(self.Pteam[2][len(self.Pteam[2])-2],(30,416))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(str(self.Pteam[2][4]), 1, (0,0,0)), (40, 495))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(str(self.Pteam[2][5]), 1, (0,0,0)), (130, 495))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(str(self.Pteam[2][6]), 1, (0,0,0)), (190, 495))
        if nbpoke>3:
            self.win.blit(self.Pteam[3][len(self.Pteam[3])-2],(286,432))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(str(self.Pteam[3][4]), 1, (0,0,0)), (296, 512))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(str(self.Pteam[3][5]), 1, (0,0,0)), (130+256, 512))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(str(self.Pteam[3][6]), 1, (0,0,0)), (190+256, 512))
        if nbpoke>4:
            self.win.blit(self.Pteam[4][len(self.Pteam[4])-2],(30,512))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(str(self.Pteam[4][4]), 1, (0,0,0)), (40, 595))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(str(self.Pteam[4][5]), 1, (0,0,0)), (130, 595))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(str(self.Pteam[4][6]), 1, (0,0,0)), (190, 595))
        if nbpoke>5:
            self.win.blit(self.Pteam[5][len(self.Pteam[5])-2],(286,528))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(str(self.Pteam[5][4]), 1, (0,0,0)), (296, 612))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(str(self.Pteam[5][5]), 1, (0,0,0)), (130+256, 612))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(str(self.Pteam[5][6]), 1, (0,0,0)), (190+256, 612))






        
        if pygame.mouse.get_pressed()[0]==1:
            if self.cc:
                self.cc=False
                self.wmenu=self.select
        else:
            self.cc=True

    def bbag(self):
        global joueur
        global login
        self.tsoin=False
        self.bsel=self.sel
        self.win.blit(self.menubag,(0,736-406),(0,0,512,390))
        self.win.blit(self.menubag, (388, 736-71),(87,411,122,48))
        if 736-406<pygame.mouse.get_pos()[1]<736-340:
            if 230<pygame.mouse.get_pos()[0]<286:
                self.win.blit(self.menubag,(231,736-406+7),(821,277,56,56))
                self.bsel="soin"
            if 389<pygame.mouse.get_pos()[0]<445:
                self.win.blit(self.menubag,(390,736-406+7),(821,277,56,56))
                self.bsel="ball"

        if self.sel=="soin":
            self.win.blit(self.menubag,(234,736-406+12),(528,12,47,47))
            
            self.win.blit(self.menubag,(10,736-406+87),(526,126,244,75))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(self.bag[4][0]+":"+str(self.bag[4][1]), 1, (0,0,0)), (70,736-406+112))
            self.win.blit(self.menubag,(266,736-406+87),(526,126,244,75))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(self.bag[5][0]+":"+str(self.bag[5][1]), 1, (0,0,0)), (326,736-406+112))
            self.win.blit(self.menubag,(10,736-406+164),(526,126,244,75))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(self.bag[6][0]+":"+str(self.bag[6][1]), 1, (0,0,0)), (70,736-406+189))
            self.win.blit(self.menubag,(266,736-406+164),(526,126,244,75))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(self.bag[7][0]+":"+str(self.bag[7][1]), 1, (0,0,0)), (326,736-406+189))
            self.win.blit(self.menubag,(10,736-406+241),(526,126,244,75))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(self.bag[8][0]+":"+str(self.bag[8][1]), 1, (0,0,0)), (70,736-406+266))
            self.win.blit(self.menubag,(266,736-406+241),(526,126,244,75))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(self.bag[9][0]+":"+str(self.bag[9][1]), 1, (0,0,0)), (326,736-406+266))
                
            if 736-406+88<pygame.mouse.get_pos()[1]<736-406+165:
                if pygame.mouse.get_pos()[0]<512/2:
                    self.win.blit(self.menubag,(12,736-406+89),(528,207,244,75))
                    self.select="soin0"
                else:
                    self.win.blit(self.menubag,(268,736-406+89),(528,207,244,75))
                    self.select="soin1"
            elif 736-406+163<pygame.mouse.get_pos()[1]<736-406+241:
                if pygame.mouse.get_pos()[0]<512/2:
                    self.win.blit(self.menubag,(12,736-406+166),(528,207,244,75))
                    self.select="soin2"
                else:
                    self.win.blit(self.menubag,(268,736-406+166),(528,207,244,75))
                    self.select="soin3"
            elif 736-406+240<pygame.mouse.get_pos()[1]<736-406+318:
                if pygame.mouse.get_pos()[0]<512/2:
                    self.win.blit(self.menubag,(12,736-406+243),(528,207,244,75))
                    self.select="soin4"
                else:
                    self.win.blit(self.menubag,(268,736-406+243),(528,207,244,75))
                    self.select="soin5"
            elif pygame.mouse.get_pos()[1]>736-80 and pygame.mouse.get_pos()[0]>512-130:
                self.win.blit(self.menubag, (390, 736-71),(215,413,118,48))
                self.select="menu"
            else:
                self.select="bag"

            
                
            
            self.win.blit(self.items,(20,736-406+100),(0,0,30,44))
            self.win.blit(self.items,(276,736-406+100),(32,0,30,44))
            self.win.blit(self.items,(20,736-406+178),(64,0,30,44))
            self.win.blit(self.items,(276,736-406+178),(98,0,34,44))
            self.win.blit(self.items,(20,736-406+256),(134,0,20,44))
            self.win.blit(self.items,(276,736-406+256),(158,0,40,44))

        else:
            self.win.blit(self.menubag,(394,736-406+12),(579,12,47,47))
            self.win.blit(self.menubag,(10,736-406+87),(526,126,244,75))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(self.bag[0][0]+":"+str(self.bag[0][1]), 1, (0,0,0)), (70,736-406+112))
            self.win.blit(self.menubag,(266,736-406+87),(526,126,244,75))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(self.bag[1][0]+":"+str(self.bag[1][1]), 1, (0,0,0)), (326,736-406+112))
            self.win.blit(self.menubag,(10,736-406+164),(526,126,244,75))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(self.bag[2][0]+":"+str(self.bag[2][1]), 1, (0,0,0)), (70,736-406+189))
            self.win.blit(self.menubag,(266,736-406+164),(526,126,244,75))
            self.win.blit(pygame.font.SysFont("monospace", 20).render(self.bag[3][0]+":"+str(self.bag[3][1]), 1, (0,0,0)), (326,736-406+189))
                
            if 736-406+88<pygame.mouse.get_pos()[1]<736-406+165:
                if pygame.mouse.get_pos()[0]<512/2:
                    self.win.blit(self.menubag,(12,736-406+89),(528,207,244,75))
                    self.select="ball0"
                else:
                    self.win.blit(self.menubag,(268,736-406+89),(528,207,244,75))
                    self.select="ball1"
            elif 736-406+163<pygame.mouse.get_pos()[1]<736-406+241:
                if pygame.mouse.get_pos()[0]<512/2:
                    self.win.blit(self.menubag,(12,736-406+166),(528,207,244,75))
                    self.select="ball2"
                else:
                    self.win.blit(self.menubag,(268,736-406+166),(528,207,244,75))
                    self.select="ball3"
            elif pygame.mouse.get_pos()[1]>736-80 and pygame.mouse.get_pos()[0]>512-130:
                self.win.blit(self.menubag, (390, 736-71),(215,413,118,48))
                self.select="menu"
            else:
                self.select="bag"
            
            self.win.blit(self.items,(20,736-406+100),(202,0,36,44))
            self.win.blit(self.items,(276,736-406+100),(240,0,36,44))
            self.win.blit(self.items,(20,736-406+178),(278,0,36,44))
            self.win.blit(self.items,(276,736-406+178),(316,0,36,44))


            
        if pygame.mouse.get_pressed()[0]==1:
            if self.cc:
                self.cc=False
                self.wmenu=self.select
                self.sel=self.bsel
        else:
            self.cc=True   
                    
            
        
                
            
            
    def numbers(self,num):#police d'écriture des nombres
        global joueur
        global login
        if num=="0":
            return 100
        elif num=="1":
            return 118
        elif num=="2":
            return 134
        elif num=="3":
            return 152
        elif num=="4":
            return 170
        elif num=="5":
            return 188
        elif num=="6":
            return 206
        elif num=="7":
            return 224
        elif num=="8":
            return 242
        elif num=="9":
            return 260

    def wmessage(self,mes):
        global joueur
        self.win.blit(self.textbox, (0, 736-406-96))
        self.win.blit(pygame.font.SysFont("monospace", 15).render(mes, 1, (0,0,0)), (20,736-490))
        self.win.blit(self.blankbottomscreen,(0,736-406))
        pygame.display.update()
        wmes=True
        while wmes:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    global run
                    keepfight = False
                    run=False
            if pygame.mouse.get_pressed()[0]==1:
                if self.cc:
                    self.cc=False
                    wmes=False
            else:
                self.cc=True
            
    
        

def jouer(logon,state):
    global run
    global joueur
    global login
    login=logon
    run = True
    pygame.init()
    pygame.display.set_caption("Pokeroyal")
    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    #S'assure que les tables contenant les données de la partie soient vides
    c.execute("DELETE FROM pnj")
    c.execute("DELETE FROM personnage")
    c.execute("DELETE FROM sac")
    c.execute("DELETE FROM objets")
    c.execute("DELETE FROM equipe")
    c.execute("DELETE FROM pokemon")
    c.execute("DELETE FROM attaquespokemon")
    conn.commit()
    conn.close()
    joueur=play(state)
    joueur.choosestarter()
    while run==True:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                launcherPOO.launch(logon)
        joueur.move()
        pygame.display.update()
    pygame.quit()

