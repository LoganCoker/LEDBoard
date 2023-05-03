import pygame

HEIGHT = 700
WIDTH = 1000

RED = [255, 0, 0]
RED_ORANGE = [255, 88, 0]
ORANGE = [255, 128, 0]
DANDELION = [255, 180, 0]
YELLOW = [255, 255, 0]
BLACK = [0, 0, 0]
GREEN = [0, 255, 0]
LIGHT_GREEN = [0, 255, 80]
SKY_BLUE = [0, 255, 160]
NICE_BLUE = [0, 128, 255]
DARK_BLUE = [0, 0, 200]
DEEP_BLUE = [80, 0, 255]
GREY = [128, 128, 128]
BLUE = [0,0,255]
LIGHTER_BLUE = [100, 0, 255]
PURPLE = [128, 0, 128]
MAHOGONY = [150, 0, 255]
MAGENTA = [255, 0, 255]
WHITE = [255, 255, 255]


ColorList = [RED, RED_ORANGE, ORANGE, DANDELION, YELLOW, BLACK,  
             GREEN, LIGHT_GREEN, SKY_BLUE, NICE_BLUE, DEEP_BLUE, GREY,
             BLUE, LIGHTER_BLUE, PURPLE, MAHOGONY, MAGENTA, WHITE]


TRANSPARENT = [0, 0, 0, 0]
LED_COUNT = 144
Color_Count = len(ColorList)
Color_Rows = 3
Color_Columns = 6
Columns = 16
Rows = 9

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
    K_BACKSPACE,
    K_1, K_2, K_3
)
