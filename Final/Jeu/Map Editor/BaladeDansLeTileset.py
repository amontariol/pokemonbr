import pygame
import time
pygame.init()

height=720
width=512

win = pygame.display.set_mode((width,height))
pygame.display.set_caption("First Game")


x = 0
y = 0
vel = 10

run = True
tileset = pygame.image.load("tileset.png").convert_alpha()
level=[]
for j in range(0,int(tileset.get_height()/32)):
    ligne=[]
    for i in range(0,int(tileset.get_width()/32)):
        coo=[i,j]
        ligne.append(coo)
    level.append(ligne)
imgplayer = pygame.image.load("characters.png").convert_alpha()
imgplayer = pygame.transform.scale(imgplayer, (imgplayer.get_width()*2, imgplayer.get_height()*2))
xs=len(level[0])*32
ys=len(level)*32
way=""
while run:
    pygame.time.delay(10)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] :
        way="L"
        if x<0:
            x += vel
            if int((time.time()*4)%2)==0:
                playertilepos=[0,1344]
            else:
                playertilepos=[0,1472]
        else:
            playertilepos=[0,1410]
        print(abs(int(x/33)-2),abs(int(y/33)-2))
            
    elif keys[pygame.K_RIGHT] :
        way="R"
        if 1==1:
            x -= vel
            if int((time.time()*vel/4)%2)==0:
                playertilepos=[64,1344]
            else:
                playertilepos=[64,1408]
        else:
            playertilepos=[64,1280]
        print(abs(int(x/33)-2),abs(int(y/33)-2))
    elif keys[pygame.K_UP]:
        way="U"
        if y<0:
            y += vel
            if int((time.time()*4)%2)==0:
                playertilepos=[128,1280]
            else:
                playertilepos=[64,1472]
        else:
            playertilepos=[0,1280]
        print(abs(int(x/33)-2),abs(int(y/33)-2))
    elif keys[pygame.K_DOWN]:
        way="D"
        if 1==1:
            y -= vel
            if int((time.time()*4)%2)==0:
                playertilepos=[128,1408]
            else:
                playertilepos=[128,1472]
        else:
            playertilepos=[128,1344]
        print(abs(int(x/33)-2),abs(int(y/33)-2))
    else:
        if way=="L":
            playertilepos=[0,1410]
        elif way=="R":
            playertilepos=[64,1280]
        elif way=="U":
            playertilepos=[0,1280]
        else:
            playertilepos=[128,1344]

    win.fill((255,255,255))
    for j in range(0,len(level)):
        for i in range(0,len(level[j])):
            win.blit(tileset, (i*33+x, j*33+y),(level[j][i][0]*32,level[j][i][1]*32,32,32))
    win.blit(imgplayer, (0,0),(playertilepos[0],playertilepos[1],64,64))  
    pygame.display.update()
    
pygame.quit()
#<>
