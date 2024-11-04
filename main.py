import pygame
import random
import sys
import math
from pygame.locals import *

#global variables

SCREENWIDTH=800
SCREENHEIGHT=600
PLAYER=pygame.image.load('spaceship.png')
ENEMY=pygame.image.load('enemy.png')
BULLET=pygame.image.load('bullet 1.png')
LOGO=pygame.image.load('ufo.png')
BACKGROUND=pygame.image.load('background.png')
SCORE={}

# player cords

playerX=370
playerY=480
playerX_change=0

# enemy cords
multi_enemy=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
wave1=6
for enemies in range(wave1):
    multi_enemy.append(ENEMY)
    enemyX.append(random.randint(0,SCREENWIDTH))
    enemyY.append(random.randint(0,100))
    enemyX_change.append(6)


# bullet cords

bulletX=370
bulletY=480
bullet_state="ready"
bulletY_change=10
score=0
#important functions
def player(x,y):
    SCREEN.blit(PLAYER,(x,y))
def enemy(x,y,enemies):
    SCREEN.blit(ENEMY,(x,y))
def fire_bullet(x,y):
    global bullet_state,bulletY,bulletY_change
    bullet_state="fire"
    SCREEN.blit(BULLET,(x+16,y+10))
def isCollide(enemyX,enemyY,bulletX,bulletY,):
    distnace=math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
    if distnace<27:
        return True
# def score_Display():
#         SCREEN.blit(SCORE[0],(620,50))
if __name__ == "__main__":

    #initalizing game
    pygame.init()

    SCREEN=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))

    pygame.display.set_caption("Space Invaders")
    pygame.display.set_icon(LOGO)

    SCORE[0]=pygame.image.load('0.png').convert_alpha(),
    SCORE[1]=pygame.image.load('1.png').convert_alpha(),
    SCORE[2]=pygame.image.load('2.png').convert_alpha(),
    SCORE[3]=pygame.image.load('3.png').convert_alpha(),
    SCORE[4]=pygame.image.load('4.png').convert_alpha(),
    SCORE[5]=pygame.image.load('5.png').convert_alpha(),
    SCORE[6]=pygame.image.load('6.png').convert_alpha(),
    SCORE[7]=pygame.image.load('7.png').convert_alpha(),
    SCORE[8]=pygame.image.load('8.png').convert_alpha(),
    SCORE[9]=pygame.image.load('9.png').convert_alpha(),

#game loop

while True:

    #background
    SCREEN.blit(BACKGROUND,(0,0))


    for event in pygame.event.get():
        # player movement

        if event.type==QUIT:
            pygame.quit()
            sys.exit()

        if event.type==KEYDOWN and (event.key==K_RIGHT):
            playerX_change= 8

        if event.type==KEYDOWN and (event.key==K_LEFT):
            playerX_change= -8
        
        if event.type==KEYUP and(event.key==K_LEFT or event.key==K_RIGHT):
            playerX_change=0
        
        if event.type==KEYDOWN and event.key==K_SPACE:
            fire_bullet(bulletX,bulletY)
        

    # player border

    if playerX>=736:
        playerX=736
    elif playerX<=0:
        playerX=0
    playerX+=playerX_change

    # enemy movemnt
    for enemies in range(wave1):
        if enemyX[enemies]>=736:
            enemyX_change[enemies]=-6
            enemyY[enemies]+=20
        elif enemyX[enemies]<=0:
            enemyX_change[enemies]=6
            enemyY[enemies]+=20
        enemyX[enemies]+=enemyX_change[enemies]
        collision=isCollide(enemyX[enemies],enemyY[enemies],bulletX,bulletY)
        if collision:
            bulletY=480
            bullet_state="ready"
            score+=1
            enemyX[enemies]=random.randint(0,SCREENWIDTH)
            enemyY[enemies]=random.randint(0,120)

        enemy(enemyX[enemies],enemyY[enemies],enemies)
            # score_Display()
        
        print(score)
    #bullet movemnt

    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change

    if bulletY<=0:
        bulletY=480
        bullet_state="ready"
    
    
    if bullet_state is "ready":
        bulletX=playerX
    player(playerX,playerY)
    print(score)
    pygame.display.update()
