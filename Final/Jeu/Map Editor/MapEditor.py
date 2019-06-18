import pygame
import time
import tileset
import temp
from itertools import repeat, chain
import ast

class play:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Map Editor")

        self.height=1024 #32
        self.width=1920 #60

        self.win = pygame.display.set_mode((self.width,self.height),pygame.FULLSCREEN)
        self.x = 0
        self.y = 0
        self.vel = 1
        self.yt = 0
        self.xt = 0
        self.lvlts=[0,0]
        self.tsts=[0,0]
        self.nts=1
        self.myfont = pygame.font.SysFont("monospace", 50)
        self.bestfont = pygame.font.SysFont("monospace", 10)
        try:
            self.level=temp.niv
        except:
            self.level=[[[[1,20]]]]
        self.tileset = pygame.image.load("tileset.png").convert_alpha()
        self.cmove=True
        self.crc=True
        self.run = True

        
        self.trainers = pygame.image.load("characters.png").convert_alpha()
        self.trainers = pygame.transform.scale(self.trainers, (self.trainers.get_width()*2, self.trainers.get_height()*2))

        self.trainer=True
        self.range=0
        self.direction=["D",True]
        self.trainerclass = [0,0]
        while self.run:
            try:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.run = False
                self.keyp()
                pygame.display.update()
            except:
                pass
        pygame.quit()

    def addpnj(self):
        
        self.trainer=True
        self.range=0
        self.direction=["D",True]
        self.trainerclass = [0,0]
        
        txt="Trainer"
        ran='0123456789:'
        h='Sens Horloger'
        conti=True
        while conti:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        conti = False
            keys = pygame.key.get_pressed()
            self.win.fill((255,255,255))
            pygame.draw.rect(self.win,(0,0,0),(self.trainerclass[0]*64,self.trainerclass[1]*64, 64, 64))
            pygame.draw.rect(self.win,(255,255,255),(self.trainerclass[0]*64+1,self.trainerclass[1]*64+1, 62, 62))
            for i in range(0,int(self.trainers.get_width()/(64*3))):
                for j in range(0,int(self.trainers.get_height()/(64*4)+1)):
                    self.win.blit(self.trainers, (i*64, j*64),(i*64*3+128, j*64*4+64,64,64))
            if pygame.mouse.get_pressed()[0]==1:
                if pygame.mouse.get_pos()[0]<64*10 and pygame.mouse.get_pos()[1]<64*8:
                    self.trainerclass=[pygame.mouse.get_pos()[0]//64,pygame.mouse.get_pos()[1]//64]
                    print('trained selected')
                elif pygame.mouse.get_pos()[1]<600:
                    if self.cmove==True:
                        if self.trainer==True:
                            self.trainer=False
                            txt='Not Trainer'
                        else:
                            self.trainer=True
                            txt='Trainer'
                        self.cmove=False
                elif pygame.mouse.get_pos()[1]<650:
                    if self.cmove==True:
                        if pygame.mouse.get_pos()[0]<30:
                            self.range=0
                        elif pygame.mouse.get_pos()[0]<60:
                            self.range=1
                        elif pygame.mouse.get_pos()[0]<90:
                            self.range=2
                        elif pygame.mouse.get_pos()[0]<120:
                            self.range=3
                        elif pygame.mouse.get_pos()[0]<150:
                            self.range=4
                        elif pygame.mouse.get_pos()[0]<180:
                            self.range=5
                        elif pygame.mouse.get_pos()[0]<210:
                            self.range=6
                        elif pygame.mouse.get_pos()[0]<240:
                            self.range=7
                        elif pygame.mouse.get_pos()[0]<270:
                            self.range=8
                        elif pygame.mouse.get_pos()[0]<300:
                            self.range=9
                        self.cmove=False
                elif pygame.mouse.get_pos()[1]<700:
                    if self.cmove==True:
                        if self.direction[1]==True:
                            self.direction[1]=False
                            h='Sens Anti-Horloger'
                        else:
                            self.direction[1]=True
                            h='Sens Horloger'
                        self.cmove=False
                elif pygame.mouse.get_pos()[1]>700 and pygame.mouse.get_pos()[0]<800:
                    try:
                        self.level[self.lvlts[1]][self.lvlts[0]][0][2]=[self.trainer,self.range,self.direction,self.trainerclass]
                    except:
                        self.level[self.lvlts[1]][self.lvlts[0]][0].append([self.trainer,self.range,self.direction,self.trainerclass])
                    conti=False
                else:
                    conti=False
                    
                    
            
            elif keys[pygame.K_LEFT]:
                if self.cmove==True:
                    self.direction[0]="L"
                    self.cmove=False
            elif keys[pygame.K_RIGHT]:
                if self.cmove==True:
                    self.direction[0]="R"
                    self.cmove=False
            elif keys[pygame.K_UP]:
                if self.cmove==True:
                    self.direction[0]="U"
                    self.cmove=False
            elif keys[pygame.K_DOWN]:
                if self.cmove==True:
                    self.direction[0]="D"
                    self.cmove=False
            else:
                self.cmove=True
            
            self.win.blit(self.myfont.render(txt, 1, (0,0,0)), (0, 550))
            self.win.blit(self.myfont.render(ran, 1, (0,0,0)), (0, 600))
            self.win.blit(self.myfont.render('range='+str(self.range), 1, (0,0,0)), (330, 600))
            self.win.blit(self.myfont.render(h, 1, (0,0,0)), (0, 650))
            self.win.blit(self.myfont.render('direction de départ:'+self.direction[0], 1, (0,0,0)), (0, 700))
            self.win.blit(self.myfont.render('Confirm', 1, (0,0,0)), (0, 750))
            self.win.blit(self.myfont.render('Cancel', 1, (0,0,0)), (1400, 750))




                    
            pygame.display.update()
            pygame.time.delay(10)
            

    def keyp(self):
        self.win.fill((255,255,255))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.run=False
        if keys[pygame.K_LEFT] and self.x!=0:
            self.x -= self.vel
            
        elif keys[pygame.K_RIGHT] :
            self.x += self.vel
            
        elif keys[pygame.K_UP] and self.y!=0:
            self.y -= self.vel
            
        elif keys[pygame.K_DOWN]:
            self.y += self.vel

        if keys[pygame.K_DELETE]:
            self.xt -= self.vel
        elif keys[pygame.K_PAGEDOWN]:
            self.xt += self.vel
        elif keys[pygame.K_HOME]:
            self.yt -= self.vel
        elif keys[pygame.K_END]:
            self.yt += self.vel
        
        if pygame.mouse.get_pressed()[0]==1:
            ts=""
            if pygame.mouse.get_pos()[0]<1617:
                self.lvlts=[pygame.mouse.get_pos()[0]//33+self.x,pygame.mouse.get_pos()[1]//33+self.y]
                ts="lvlts"
            elif pygame.mouse.get_pos()[1]<33:
                if pygame.mouse.get_pos()[0]//33-50>=0:
                    self.nts=pygame.mouse.get_pos()[0]//33-50
                ts="nts"
            else:
                if pygame.mouse.get_pos()[0]//33-50>=0 and pygame.mouse.get_pos()[1]>66:
                    self.tsts=[pygame.mouse.get_pos()[0]//33-50+self.xt,pygame.mouse.get_pos()[1]//33-2+self.yt]
                    ts="tsts"

            if ts=="tsts":
                if self.nts==0:
                    self.level[self.lvlts[1]][self.lvlts[0]][self.nts]=self.tsts
                else:
                    try:
                        self.level[self.lvlts[1]][self.lvlts[0]][self.nts]=self.tsts
                    except:
                        self.level[self.lvlts[1]][self.lvlts[0]].append(self.tsts)
        if keys[pygame.K_KP_PLUS] or keys[pygame.K_t]:
            self.addpnj()

        if keys[pygame.K_KP_MINUS]:
            if len(self.level[self.lvlts[1]][self.lvlts[0]][0])==3:
                del self.level[self.lvlts[1]][self.lvlts[0]][0][2]
        
        if keys[pygame.K_KP0]:
            self.nts=0
        if keys[pygame.K_KP1]:
            self.nts=1
        if keys[pygame.K_KP2]:
            self.nts=2
        if keys[pygame.K_KP3]:
            self.nts=3
        
        if keys[pygame.K_KP4]:
            if self.cmove==True:
                self.lvlts[0]-=1
                self.cmove=False
        elif keys[pygame.K_KP5]:
            if self.cmove==True:
                self.lvlts[1]+=1
                self.cmove=False
        elif keys[pygame.K_KP6]:
            if self.cmove==True:
                self.lvlts[0]+=1
                self.cmove=False
        elif keys[pygame.K_KP8]:
            if self.cmove==True:
                self.lvlts[1]-=1
                self.cmove=False
        else:
            self.cmove=True
            
        
        if pygame.mouse.get_pressed()[2]==1:
            if pygame.mouse.get_pos()[0]<1617:
                try:
                    self.level[pygame.mouse.get_pos()[1]//33+self.y][pygame.mouse.get_pos()[0]//33+self.x][self.nts]=self.tsts
                except:
                    self.level[pygame.mouse.get_pos()[1]//33+self.y][pygame.mouse.get_pos()[0]//33+self.x].append([self.tsts])
            else:
                if self.nts==0:
                    self.level[self.lvlts[1]][self.lvlts[0]][self.nts]=[1,20]
                elif self.crc==True:
                    try:
                        del self.level[self.lvlts[1]][self.lvlts[0]][self.nts]
                        self.crc=False
                    except:
                        pass
        else:
            self.crc=True

        if keys[pygame.K_KP_DIVIDE]:
            if self.nts==0:
                self.level[self.lvlts[1]][self.lvlts[0]][self.nts]=[1,20]
            elif self.crc==True:
                try:
                    del self.level[self.lvlts[1]][self.lvlts[0]][self.nts]
                    self.crc=False
                except:
                    pass
            
        
        if keys[pygame.K_RETURN]:
            f= open("lvl.py","w+")
            f.write("niv="+str(self.level))
            f.close()
            print('Saved')
        
        if keys[pygame.K_RSHIFT]:
            print('Loading')
            f= open("lvl.py","r")
            self.level=ast.literal_eval(f.read()[4:])
            print(type(self.level))
            print(self.level)
            f.close()
            print('Loaded')

        
        
        pygame.draw.rect(self.win,(0,0,0),((self.lvlts[0]-self.x)*33-1,(self.lvlts[1]-self.y)*33-1, 34, 34))
        pygame.draw.rect(self.win,(255,255,255),((self.lvlts[0]-self.x)*33,(self.lvlts[1]-self.y)*33, 32, 32))
        
        pygame.draw.rect(self.win,(0,0,0),((self.nts+50)*33-1,0, 34, 33))
        pygame.draw.rect(self.win,(255,255,255),((self.nts+50)*33,0, 32, 32))
        
        pygame.draw.rect(self.win,(0,0,0),((self.tsts[0]-self.xt+50)*33-1,(self.tsts[1]-self.yt+2)*33-1, 34, 34))
        pygame.draw.rect(self.win,(255,255,255),((self.tsts[0]-self.xt+50)*33,(self.tsts[1]-self.yt+2)*33, 32, 32))
        
        for j in range(0,31):
            for i in range(0,49):
                try:
                    if type(self.level[self.y+j][self.x+i][0]).__name__=="list":
                        for k in range(0,len(self.level[self.y+j][self.x+i])):
                            self.win.blit(self.tileset, (i*33, j*33),(self.level[self.y+j][self.x+i][k][0]*32,self.level[self.y+j][self.x+i][k][1]*32,32,32))
                    else:
                        self.win.blit(self.tileset, (i*33, j*33),(self.level[self.y+j][self.x+i][0]*32,self.level[self.y+j][self.x+i][1]*32,32,32))
                except:
                    try:
                        self.level[self.y+j].append([[1,20]])
                        i-=1
                    except:
                        nl=[]
                        for k in range(0,len(self.level[0])):
                            nl.append([[1,20]])
                        self.level.append(nl)
                        j-=1
                if j==0:
                    self.win.blit(self.bestfont.render(str(i+self.x+1), 1, (0,0,0)), (i*33, 0))
            self.win.blit(self.bestfont.render(str(j+self.y+1), 1, (0,0,0)), (0, j*33))

        for j in range(2,32):
            for i in range(50,58):
                self.win.blit(self.tileset, (i*33, j*33),((self.xt+i-50)*32,(self.yt+j-2)*32,32,32))
        for i in range(50,50+len(self.level[self.lvlts[1]][self.lvlts[0]])):
            self.win.blit(self.tileset, (i*33, 0),((self.level[self.lvlts[1]][self.lvlts[0]][i-50][0])*32,(self.level[self.lvlts[1]][self.lvlts[0]][i-50][1])*32,32,32))







        for i in range(0,len(self.level)):
            for j in range(0,len(self.level[i])):
                if len(self.level[i][j][0])==3:
                    self.win.blit(self.trainers, (j*33-16-self.x*33,i*33-32-self.y*33),(self.level[i][j][0][2][3][0]*64*3+128, self.level[i][j][0][2][3][1]*64*4+64,64,64))










                
        f= open("temp.py","w+")
        f.write("niv="+str(self.level))
        f.close()
        
                        
play()
