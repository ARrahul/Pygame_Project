import pygame, random, sys
from pygame.locals import *

WINDOWWIDTH = 700
WINDOWHEIGHT = 550
ALLIENTEXTCOLOR = (255,0,0 )
PRESSCOLOR=(255,255,255)
TOPCOLOR=(50,200,025)
SCORECOLOR=(100,000,150)
LIFECOLOR=(200,0,0)
LEVECOLOR=(0,0,200)
BACKGROUNDCOLOR = (0, 0, 0)
FPS = 40
BADDIEMINSIZE = 40
BADDIEMAXSIZE = 80
BADDIEMINSPEED = 8
BADDIEMAXSPEED = 1
ADDNEWBADDIERATE = 20
PLAYERMOVERATE = 5
LEVEL=1
n=1
k=45
l=45
q=0
d=1
e=1
lev=1
def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # pressing escape quits
                    terminate()
                return

def playerHasHitBaddie(playerRect, baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            return True
    return False

def bulletHasHitBaddie(playerRect, brect):
    if playerRect.colliderect(brect):
        return True
    return False

def drawText(text, font, surface, x, y,TEXTCOLOR):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)



#OPENbackgroud
oi = pygame.image.load('backgroundimg.jpeg')
ooi=pygame.transform.scale(oi,(WINDOWWIDTH,WINDOWHEIGHT))

#GAMEBACKGROUND
gi = pygame.image.load('onebackgroundimg.jpeg')
ggi=pygame.transform.scale(gi,(WINDOWWIDTH,WINDOWHEIGHT))

#bullet
bulletimage=pygame.image.load('enenybullet.png')
bulletsi=pygame.transform.scale(bulletimage,(15,35))
bulletrect=bulletsi.get_rect()
enemybullet=pygame.image.load('bullet.png')
bbulletsi=pygame.transform.scale(enemybullet,(8,35))

# set up pygame, the window, and the mouse cursor
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('ALLIEN ATTACK')
windowSurface.blit(ooi,(0,0))

# set up fonts
font = pygame.font.SysFont(None, 48)
lifefont = pygame.font.SysFont(None, 25)


# set up sounds
gameOverSound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('background.mid')

# set up images
playerImage = pygame.image.load('player1.png')
playerstrImage=pygame.transform.scale(playerImage,(80,75))
playerRect = playerstrImage.get_rect()
baddieImage = pygame.image.load('baddie.png')

# show the "Start" screen
drawText('ALLIEN ATTACK', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 5),ALLIENTEXTCOLOR)
drawText('Press a key to start.', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 5) + 50,PRESSCOLOR)
pygame.display.update()
waitForPlayerToPressKey()
topScore = 0
v=0
score=0
while True:
    t=50
    h=50
    w=50    
    v=v+1
    drawText('life : %s ' % (4-v), lifefont, windowSurface, (WINDOWWIDTH -60), ((WINDOWHEIGHT / 10)+15),SCORECOLOR)
    pygame.display.update()
    BADDIEMINSIZE = 20
    BADDIEMAXSIZE = 40
    BADDIEMINSPEED = 1
    BADDIEMAXSPEED = 3
    n=1
    k=45
    l=45
    q=0
    d=1
    e=1
    h=random.randint(0,50)
    # set up the start of the game
    baddies = []
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    baddieAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)

    while True: # the game loop runs while the game part is playing
        score += 0.1 # increase score
        LEVEL+=0.1
        SCORECOLOR=(100-t,20+t,100+3*t)
        LIFECOLOR=(200-h/2,0+h,0+3*h)
        LEVELCOLOR=(100+w,0+2*w,150+w/2)
        playerstrImage=pygame.transform.scale(playerImage,(80,75))
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == ord('z'):
                    reverseCheat = True
                if event.key == ord('x'):
                    slowCheat = True
                if event.key == K_LEFT or event.key == ord('a'):
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == ord('w'):
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == ord('s'):
                    moveUp = False
                    moveDown = True
         

            if event.type == KEYUP:
                if event.key == ord('z'):
                    reverseCheat = False
                    score = 0
                if event.key == ord('x'):
                    slowCheat = False
                    score = 0
                if event.key == K_ESCAPE:
                        terminate()

                if event.key == K_LEFT or event.key == ord('a'):
                    moveLeft = False
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveRight = False
                if event.key == K_UP or event.key == ord('w'):
                    moveUp = False
                if event.key == K_DOWN or event.key == ord('s'):
                    moveDown = False

            if event.type == MOUSEMOTION:
                # If the mouse moves, move the player where the cursor is.
                playerRect.move_ip(event.pos[0] - playerRect.centerx, event.pos[1] - playerRect.centery)

        # Add new  at the top of the screen, if needed.
        if not reverseCheat and not slowCheat:
            baddieAddCounter +=1
        if baddieAddCounter >=ADDNEWBADDIERATE:
            baddieAddCounter = 0
            baddieSize = random.randint(BADDIEMINSIZE, BADDIEMAXSIZE)
            newBaddie = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH-baddieSize), 0 - baddieSize, baddieSize, baddieSize),
                        'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                        'surface':pygame.transform.scale(baddieImage, (baddieSize, baddieSize)),
                         'count':0,
                         'bbulletrect':bbulletsi.get_rect()
                        }

            baddies.append(newBaddie)

        # Move the player around.
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)

        # Move the mouse cursor to match the player.
        pygame.mouse.set_pos(playerRect.centerx, playerRect.centery)

        # Move the enimies down.
        for b in baddies:
            if not reverseCheat and not slowCheat:
                b['rect'].move_ip(0, b['speed'])
            elif reverseCheat:
                b['rect'].move_ip(0, -5)
            elif slowCheat:
                b['rect'].move_ip(0, 1)
    
         # Delete enemies that have fallen past the bottom.
        for b in baddies[:]:
            if b['rect'].top > WINDOWHEIGHT:
                baddies.remove(b)
            if bulletHasHitBaddie(bulletrect, b['rect']):
                d=2
                bulletrect.top=0
                bulletrect.left=0
                windowSurface.blit(bulletsi, bulletrect)
                b['count']+=1
            if b['count']==4 :
                score +=200
                t=random.randint(0,50)
                baddies.remove(b)
                q=q-5
            
        # Draw the game world on the window.
        #windowSurface.fill(BACKGROUNDCOLOR)
        windowSurface.blit(ggi,(0,0))
        #pygame.display.update()

        # Draw the score and top score.
        drawText('Score: %s' % (score), font, windowSurface, 10, 0,SCORECOLOR)
        drawText('Top Score: %s' % (topScore), lifefont, windowSurface, WINDOWWIDTH-150, 0,TOPCOLOR)
        drawText('LIFE : %s ' % (4-v), font, windowSurface, 10,40,LIFECOLOR)
        if 40<LEVEL<60:
            g=1
            lev=2
            BADDIEMINSIZE = 30
            BADDIEMAXSIZE = 60
            BADDIEMINSPEED = 3
            BADDIEMAXSPEED = 5
            ADDNEWBADDIERATE=15
            w=random.randint(0,50)
            playerImage = pygame.image.load('player2.png')
        elif 60<LEVEL<260:
            lev=3
            BADDIEMINSIZE = 60
            BADDIEMAXSIZE = 80
            BADDIEMINSPEED = 6
            BADDIEMAXSPEED = 9
            ADDNEWBADDIERATE=10
            w=random.randint(0,50)
            playerImage = pygame.image.load('player3.png')
        elif 260<LEVEL<560:
            lev=4
            BADDIEMINSIZE = 80
            BADDIEMAXSIZE = 100
            BADDIEMINSPEED = 10
            BADDIEMAXSPEED = 13
            ADDNEWBADDIERATE=7
            w=random.randint(0,50)
            playerImage = pygame.image.load('player4.png')
        elif 560<LEVEL<700:
            lev=5
            BADDIEMINSIZE = 100
            BADDIEMAXSIZE = 200
            BADDIEMINSPEED = 15
            BADDIEMAXSPEED = 17
            ADDNEWBADDIERATE=5
            w=random.randint(0,50)
            playerImage = pygame.image.load('player5.png')
        elif LEVEL>160:
            lev=6
        else :
            ADDNEWBADDIERATE=20

        if lev<6:
            drawText('LEVEL: %s' % (lev), font, windowSurface, 10,80 ,TOPCOLOR)  
        else:
            drawText('GAME COMPLETED' , font, windowSurface, WINDOWWIDTH/2-400,WINDOWHEIGHT/2-20 ,TOPCOLOR)
        pygame.display.update()
        
        # Draw the player's 
        windowSurface.blit(playerstrImage, playerRect)

        #Draw the bullets
        bulletrect.centerx=playerRect.centerx
        bulletrect.bottom=playerRect.top
        bulletrect.bottom-=k
        if d==1:
            k=k+35
        elif d==2:
            k=k+600
        windowSurface.blit(bulletsi, bulletrect)   
        if k>WINDOWHEIGHT:
            k=0
        d=1

        # Draw each enemy and enemy bullet
        for b in baddies:
            windowSurface.blit(b['surface'], b['rect'])
            pygame.display.update()
            if bulletHasHitBaddie(b['bbulletrect'],playerRect):
                l=l+1000
                q=q+1
            b['bbulletrect'].centerx=b['rect'].centerx
            b['bbulletrect'].top=b['rect'].bottom
            b['bbulletrect'].bottom+=l
            l=l+10
            windowSurface.blit(bbulletsi, b['bbulletrect'])
            pygame.display.update()
            if l>WINDOWHEIGHT:
                l=0


        #draw the power remaining
        drawText('power: %s ' % (20-q), font, windowSurface, 10, 120,(150,0,0))
        pygame.display.update()
        # Check if any of the bullet have hit the player.
        if (playerHasHitBaddie(playerRect, baddies) or q==20  or lev==6):
            if score > topScore:
                topScore = score # set new top score
            break
            q=0
        mainClock.tick(50)
    drawText('life remaining: %s ' % (3-v), font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3),LIFECOLOR)
    pygame.display.update()
    if (v==3):
        LEVEL=0
        v=0
        score=0
        # Stop the game and show the "Game Over" screen.
        pygame.mixer.music.stop()
        gameOverSound.play()

        drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3)+30,ALLIENTEXTCOLOR)
        drawText('Press a key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 100,(255,255,255))
        pygame.display.update()
        waitForPlayerToPressKey()

        gameOverSound.stop()
