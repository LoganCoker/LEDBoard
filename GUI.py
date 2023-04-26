import pygame
from Constants import *
from Functions import *
from Classes import *
import debugpy

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

test = True

LED_Locations = []
LED_Collision = []

Color_Locations = []
Color_Collision = []

Color = WHITE

RUNNING = True

for i in range(LED_COUNT):
    LED_Locations.append(LEDS(screen))

for i in range(Color_Count):
    newfill = ColorList[i]
    Color_Locations.append(LEDS(screen, fill=newfill))


def create_GUI():
    global startX, startY
    index = 0
    
    X = 45
    Y = 45
    
    for i in range(Color_Count):
        rect = Color_Locations[i].rect
        rect.center = ((X,Y))
        LEDS.createLED(Color_Locations[i])
        Color_Collision.append(rect)
        X += 45
    
    for _ in range(Rows):
        for i in range(Columns):
            if startY % 10 == 0:
                rect = LED_Locations[index].rect
                rect.center = ((startX, startY))
                LEDS.createLED(LED_Locations[index])
                LED_Collision.append(rect)
                index += 1
                startX += 45
                if i == 17:
                    startX -= 45
              
            else:
                rect = LED_Locations[index].rect
                rect.center = ((startX, startY))
                LEDS.createLED(LED_Locations[index])
                LED_Collision.append(rect)
                index += 1
                startX -= 45
                if i == 17:
                    startX += 45
                
            
        startY += 45


while (RUNNING):

    for event in pygame.event.get():
        if (event.type == KEYDOWN and event.key == K_ESCAPE):
            RUNNING = False
        elif (event.type == QUIT):
            RUNNING = False
    
    screen.fill(WHITE)

    startX = 115
    startY = 300
    create_GUI()
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            Xtouch = event.pos[0]
            Ytouch = event.pos[1]
            
            for i in Color_Collision:
                if i.collidepoint(Xtouch,Ytouch):
                    print(f'{i}')
                    newindex = Color_Collision.index(i)
                    newcolor = Color_Locations[newindex]
                    Color = newcolor.fill
            
            for i in LED_Collision:
                if i.collidepoint(Xtouch, Ytouch):
                    print(f'{i}')
                    led = LED_Collision.index(i)
                    LED_Locations[led] = LEDS(screen, fill=Color)
    
                                    


    pygame.display.flip()
    clock.tick(60)

