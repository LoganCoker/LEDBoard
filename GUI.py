import pygame
from Constants import *
from Functions import *
from Classes import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))


LED_Locations = []
LED_Collision = []
Color_Locations = []
Color_Collision = []

color = WHITE

RUNNING = True

while (RUNNING):

    for event in pygame.event.get():
        if (event.type == KEYDOWN and event.key == K_ESCAPE):
            RUNNING = False
        elif (event.type == QUIT):
            RUNNING = False
    
    screen.fill(WHITE)

    startX = 300
    startY = 200
    for _ in range(10):
        for i in range(10):
            LED = LEDS(screen)
            rect = LED.rect
            rect.center = ((startX, startY))
            LED_Locations.append(LEDS.createLED(LED))
            LED_Collision.append(rect)
            startX += 45
        startX = 300
        startY += 45
    
    colorX = 25
    colorY = 25
    colorIndex = 0
    for _ in range(5):
        COLOR = Colors(screen)
        rect = COLOR.get_rect()
        rect.center = ((colorX, colorY))
        COLOR.color = ColorList[colorIndex]
        Color_Locations.append(Colors.createColors(COLOR))
        Color_Collision.append(rect)
        colorX += 45
        colorIndex += 1
        

    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            Xtouch = event.pos[0]
            Ytouch = event.pos[1]
            for i in LED_Collision:
                if i.collidepoint(Xtouch, Ytouch):
                    print(f'{i}')
                    

    Color = BLUE

    pygame.display.flip()