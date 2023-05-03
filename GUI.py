import pygame
from Constants import *
from Functions import *
from Classes import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))


LEDs = pygame.sprite.Group()
allSprites = pygame.sprite.Group()

color = WHITE

RUNNING = True

while (RUNNING):

    for event in pygame.event.get():
        if (event.type == KEYDOWN and event.key == K_ESCAPE):
            RUNNING = False
        elif (event.type == QUIT):
            RUNNING = False
    
    screen.fill(WHITE)

    startX = 10
    startY = 10
    
    for i in range(0, 256, 20):
        x = startX
        y = startY
        for j in range(0, 256, 20):
            for k in range(0, 256, 20):
                color = [i, j, k]
                led = LEDS(screen, x, y, fill=color)
                rect = led.rect
                rect.center = ((startX, startY))
                allSprites.add(led)
                x += 5
            x = startX
            y += 5
            
        

    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            Xtouch = event.pos[0]
            Ytouch = event.pos[1]
            
                    
    for i in allSprites:
        screen.blit(i.sprite, i.rect)


    Color = BLUE

    pygame.display.flip()