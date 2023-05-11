import pygame
from Constants import *
from Functions import *
from Classes import *
# import pygame_widgets
# from pygame_widgets.slider import Slider
# from pygame_widgets.textbox import TextBox
import testy
from rpi_ws281x import *
import argparse
from time import sleep


LED_COUNT      = 144     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating a signal (try 10)
LED_BRIGHTNESS = 100      # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0      

test = True
RUNNING = True

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


LED_Locations = []
LED_Collision = []
Color_Locations = []
Color_Collision = []


Color = WHITE
R = 255
B = 255
G = 255

# sliderR = Slider(screen, 600, 45, 300, 15, colour = (R, 0, 0), min=0, max=255)
# outputR = TextBox(screen, 553, 40, 38, 30, fontSize=25)
# outputR.disable()

# sliderB = Slider(screen, 600, 80, 300, 15, colour = (0, 0, B), min=0, max=255)
# outputB = TextBox(screen, 553, 75, 38, 30, fontSize=25)
# outputB.disable()

# sliderG = Slider(screen, 600, 115, 300, 15, colour = (0, G, 0), min=0, max=255)
# outputG = TextBox(screen, 553, 110, 38, 30, fontSize=25)
# outputG.disable()

# sliderR = Slider(screen, 600, 45, 300, 15, colour = (R, 0, 0), min=0, max=255)
# outputR = TextBox(screen, 553, 40, 38, 30, fontSize=25)
# outputR.disable()

# sliderB = Slider(screen, 600, 80, 300, 15, colour = (0, 0, B), min=0, max=255)
# outputB = TextBox(screen, 553, 75, 38, 30, fontSize=25)
# outputB.disable()

# sliderG = Slider(screen, 600, 115, 300, 15, colour = (0, G, 0), min=0, max=255)
# outputG = TextBox(screen, 553, 110, 38, 30, fontSize=25)
# outputG.disable()


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
    
    

def Anim1():
    print('Anim1')
    testy.techSign(strip)
    
def Anim2():
    print('Anim2')
    testy.randomColors(strip)


parser = argparse.ArgumentParser()
parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
args = parser.parse_args()

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()

while (RUNNING):
    
    
    for event in pygame.event.get():
        if (event.type == KEYDOWN and event.key == K_ESCAPE):
            testy.clearOff(strip)
            RUNNING = False
        elif (event.type == QUIT):
            testy.clearOff(strip)
            RUNNING = False

    keys = pygame.key.get_pressed()
    
    if keys[K_SPACE]:
        sleep(0.2)
        testy.update(strip, LED_Locations)

    if keys[K_BACKSPACE]:
        testy.clearOn(strip)
        for i in range(len(LED_Locations)):
            led = LED_Locations[i]
            led.fill = WHITE
            LED_Locations[i] = led
        sleep(0.2)

    if keys[K_1]:
        testy.techSignAni(strip)
        sleep(0.2)

    if keys[K_2]:
        testy.randomColors(strip)
        sleep(0.2)
    
    if keys[K_3]:
        testy.rainbowCycle(strip, iterations=2)
        sleep(0.2)
    
    if keys[K_0]:
        testy.techSign(strip)
        sleep(.2)
    
    if keys[K_MINUS]:
        LED_BRIGHTNESS -= 10
        if LED_BRIGHTNESS <= 0:
            LED_BRIGHTNESS = 1
        strip.setBrightness(LED_BRIGHTNESS)
        strip.show()
        sleep(.1)
    
    if keys[K_EQUALS]:
        LED_BRIGHTNESS += 10
        if LED_BRIGHTNESS >= 255:
            LED_BRIGHTNESS = 255
        strip.setBrightness(LED_BRIGHTNESS)
        strip.show()
        sleep(.1)


    # outputR.setText(sliderR.getValue())
    # outputB.setText(sliderB.getValue())
    # outputG.setText(sliderG.getValue())
    # slider_color(sliderR, sliderG, sliderB, sliderR.getValue(), sliderG.getValue(), sliderB.getValue(), Color_Locations[-1])
    
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
                    newindex = Color_Collision.index(i)
                    newcolor = Color_Locations[newindex]
                    Color = newcolor.fill
            
            for i in LED_Collision:
                if i.collidepoint(Xtouch, Ytouch):
                    led = LED_Collision.index(i)
                    LED_Locations[led] = LEDS(screen, fill=Color)
        
    # pygame_widgets.update(event)

    pygame.display.flip()
    clock.tick(120)