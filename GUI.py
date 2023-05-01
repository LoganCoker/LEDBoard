import pygame
from Constants import *
from Functions import *
from Classes import *
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
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

R = 255
B = 255
G = 255




sliderR = Slider(screen, 600, 45, 300, 15, colour = (R, 0, 0), min=0, max=255)
outputR = TextBox(screen, 553, 40, 38, 30, fontSize=25)
outputR.disable()

sliderB = Slider(screen, 600, 80, 300, 15, colour = (0, 0, B), min=0, max=255)
outputB = TextBox(screen, 553, 75, 38, 30, fontSize=25)
outputB.disable()

sliderG = Slider(screen, 600, 115, 300, 15, colour = (0, G, 0), min=0, max=255)
outputG = TextBox(screen, 553, 110, 38, 30, fontSize=25)
outputG.disable()


RUNNING = True

for i in range(LED_COUNT):
    LED_Locations.append(LEDS(screen))

for i in range(Color_Count):
    newfill = ColorList[i]
    Color_Locations.append(LEDS(screen, fill=newfill))
Color_Locations.append(LEDS(screen))

def slider_color(SR, SG, SB, R, G, B, CLED):
    SR.colour = (R, 0, 0)
    SG.colour = (0, G, 0)
    SB.colour = (0, 0, B)
    CLED.fill = (R, G, B)

def create_GUI():
    global startX, startY   
    index = 0

    for _ in range(Rows):
        for i in range(Columns):
            if startY % 10 == 0:
                rect = LED_Locations[index].rect
                rect.center = ((startX, startY))
                LEDS.createLED(LED_Locations[index])
                LED_Collision.append(rect)
                index += 1
                startX += 45
                if i == 15:
                    startX -= 45
              
            else:
                rect = LED_Locations[index].rect
                rect.center = ((startX, startY))
                LEDS.createLED(LED_Locations[index])
                LED_Collision.append(rect)
                index += 1
                startX -= 45
                if i == 15:
                    startX += 45
                
            
        startY += 45
    
def CreateColors():
    ColorX = 115
    ColorY = 45
    
    color_index = 0
    
    for a in range(Color_Rows):
        for b in range(Color_Columns):
            rect = Color_Locations[color_index].rect
            rect.center = ((ColorX, ColorY))
            LEDS.createLED(Color_Locations[color_index])
            Color_Collision.append(rect)
            color_index += 1
            ColorX += 45
        ColorY += 45
        ColorX = 115
    rect = Color_Locations[color_index].rect
    rect.center = ((945, 87))
    LEDS.createLED(Color_Locations[color_index])
    Color_Collision.append(rect)

while (RUNNING):
    
    
    for event in pygame.event.get():
        if (event.type == KEYDOWN and event.key == K_ESCAPE):
            RUNNING = False
        elif (event.type == QUIT):
            RUNNING = False
    
    outputR.setText(sliderR.getValue())
    outputB.setText(sliderB.getValue())
    outputG.setText(sliderG.getValue())
    slider_color(sliderR, sliderG, sliderB, sliderR.getValue(), sliderG.getValue(), sliderB.getValue(), Color_Locations[-1])
    
    screen.fill(WHITE)

    startX = 160
    startY = 250
    create_GUI()
    CreateColors()
    
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
                                    
    pygame_widgets.update(event)

    pygame.display.flip()
    clock.tick(60)

