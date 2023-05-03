import pygame
from Constants import *
from Functions import *

collisionRect = pygame.Surface((40,40))

class LEDS(pygame.sprite.Sprite):

    def __init__(self, screen, xPos , yPos, fill = WHITE, outline = BLACK, radius = 5, thickness = 1):
        pygame.sprite.Sprite.__init__(self)
        self.color = fill
        self.screen = screen
        self.outline = outline
        self.radius = radius
        self.thickness = thickness
        self.sprite = pygame.Surface((5,5))
        self.rect = self.sprite.get_rect()
        self.rect.center = (xPos, yPos)

    
    def createLED(self):
        draw_bordered_rounded_rect(self.screen, self.rect, self.color, self.outline, self.radius, self.thickness)

    def position(self):
        return self.rect.center


class Colors(pygame.Surface):

    def __init__(self, screen, fill = WHITE, outline = BLACK, radius = 5, thickness = 1):
        pygame.Surface.__init__(self, (40, 40))
        self.color = fill
        self.screen = screen
        self.rect = collisionRect.get_rect()
        self.outline = outline
        self.radius = radius
        self.thickness = thickness

    
    def createColors(self):
        draw_bordered_rounded_rect(self.screen, self.rect, self.color, self.outline, self.radius, self.thickness)
    