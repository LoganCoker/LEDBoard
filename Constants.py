import pygame

HEIGHT = 700
WIDTH = 1000

RED = [255, 0, 0]
DARK_RED = [128, 0, 0]
DARKEST_RED = [62, 0, 0]
BLUE = [0,0,255]
DARK_BLUE = [0, 0, 128]
DARKEST_BLUE = [0, 0, 62]
GREEN = [0, 255, 0]
DARK_GREEN = [0, 128, 0]
DARKEST_GREEN = [0, 62, 0]
GREY = [128, 128, 128]
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
YELLOW = [255, 255, 0]
CYAN = [0, 255, 255]
MAGENTA = [255, 0, 255]
ORANGE = [255, 128, 0]
NICE_BLUE = [0, 128, 255]
PURPLE = [128, 0, 128]
GROSS = [128,128, 0]
TEAL = [0, 128, 128]
DURPLE = [128,0, 255]

ColorList = [WHITE, RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA, 
             GREY, DARK_RED, ORANGE, DARK_GREEN, NICE_BLUE, DARK_BLUE, PURPLE,
             BLACK, DARKEST_RED, GROSS, DARKEST_GREEN,TEAL, DARKEST_BLUE, DURPLE]


TRANSPARENT = [0, 0, 0, 0]
LED_COUNT = 144
Color_Count = len(ColorList)
Color_Rows = 3
Color_Columns = 7
Columns = 18
Rows = 8


# keys from pygame
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_SPACE,
)