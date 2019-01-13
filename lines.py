import pygame
linecolor=(255,255,255)
pygame.init()
windowSurface=pygame .display.set_mode((300,300),0,32)
windowSurface.fill((0,0,0))
k=200
x=1
while 2==2:
    pygame.draw.line(windowSurface,linecolor,(k,100),(k+7,100),3)
    if (x==1000):
        x=0
        k=k+10
    x=x+1
    pygame.display.update()
