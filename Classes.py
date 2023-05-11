import pygame
from Constants import *
from Functions import *

collisionRect = pygame.Surface((60,60))



class LEDS(pygame.Surface):

    def __init__(self, screen, fill = WHITE, outline = BLACK, radius = 5, thickness = 1):
        pygame.Surface.__init__(self, (60, 60))
        self.fill = fill
        self.screen = screen
        self.rect = collisionRect.get_rect()
        self.outline = outline
        self.radius = radius
        self.thickness = thickness

    
    def createLED(self):
        draw_bordered_rounded_rect(self.screen, self.rect, self.fill, self.outline, self.radius, self.thickness)


    def Update(self, color):
        self.fill = color
        self.createLED()
        pygame.display.flip()


class Colors(pygame.Surface):

    def __init__(self, screen, fill = WHITE, outline = BLACK, radius = 5, thickness = 1):
        pygame.Surface.__init__(self, (60, 60))
        self.fill = fill
        self.screen = screen
        self.rect = collisionRect.get_rect()
        self.outline = outline
        self.radius = radius
        self.thickness = thickness

    
    def createColors(self):
        draw_bordered_rounded_rect(self.screen, self.rect, self.color, self.outline, self.radius, self.thickness)


