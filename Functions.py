import pygame
import pygame.gfxdraw
from Constants import *

def draw_rounded_rect(surface, rect, color, corner_radius):
    
    if rect.width < 2 * corner_radius or rect.height < 2 * corner_radius:
        raise ValueError(f"Both height (rect.height) and width (rect.width) must be > 2 * corner radius ({corner_radius})")

    # need to use anti aliasing circle drawing routines to smooth the corners
    pygame.gfxdraw.aacircle(surface, rect.left+corner_radius, rect.top+corner_radius, corner_radius, color)
    pygame.gfxdraw.aacircle(surface, rect.right-corner_radius-1, rect.top+corner_radius, corner_radius, color)
    pygame.gfxdraw.aacircle(surface, rect.left+corner_radius, rect.bottom-corner_radius-1, corner_radius, color)
    pygame.gfxdraw.aacircle(surface, rect.right-corner_radius-1, rect.bottom-corner_radius-1, corner_radius, color)

    pygame.gfxdraw.filled_circle(surface, rect.left+corner_radius, rect.top+corner_radius, corner_radius, color)
    pygame.gfxdraw.filled_circle(surface, rect.right-corner_radius-1, rect.top+corner_radius, corner_radius, color)
    pygame.gfxdraw.filled_circle(surface, rect.left+corner_radius, rect.bottom-corner_radius-1, corner_radius, color)
    pygame.gfxdraw.filled_circle(surface, rect.right-corner_radius-1, rect.bottom-corner_radius-1, corner_radius, color)

    rect_tmp = pygame.Rect(rect)

    rect_tmp.width -= 2 * corner_radius
    rect_tmp.center = rect.center
    pygame.draw.rect(surface, color, rect_tmp)

    rect_tmp.width = rect.width
    rect_tmp.height -= 2 * corner_radius
    rect_tmp.center = rect.center
    pygame.draw.rect(surface, color, rect_tmp)


def draw_bordered_rounded_rect(surface, rect, color, border_color, corner_radius, border_thickness):
    if corner_radius < 0:
        raise ValueError(f"border radius ({corner_radius}) must be >= 0")

    rect_tmp = pygame.Rect(rect)
    center = rect_tmp.center

    if border_thickness:
        if corner_radius <= 0:
            pygame.draw.rect(surface, border_color, rect_tmp)
        else:
            draw_rounded_rect(surface, rect_tmp, border_color, corner_radius)

        rect_tmp.inflate_ip(-2*border_thickness, -2*border_thickness)
        inner_radius = corner_radius - border_thickness + 1
    else:
        inner_radius = corner_radius

    if inner_radius <= 0:
        pygame.draw.rect(surface, color, rect_tmp)
    else:
        draw_rounded_rect(surface, rect_tmp, color, inner_radius)
        

# Imports
import sys
import pygame

# Configuration
# pygame.init()
# fps = 60
# fpsClock = pygame.time.Clock()
# width, height = 640, 480
# screen = pygame.display.set_mode((width, height))

# font = pygame.font.SysFont('TimesNewRoman', 15)

# objects = []

# class Button():
#     def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.onclickFunction = onclickFunction
#         self.onePress = onePress

#         self.fillColors = {
#             'normal': (0, 160, 255),
#             'hover': NICE_BLUE,
#             'pressed': NICE_BLUE,
#         }

#         self.buttonSurface = pygame.Surface((self.width, self.height))
#         self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

#         self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

#         self.alreadyPressed = False

#         objects.append(self)

#     def process(self):

#         mousePos = pygame.mouse.get_pos()
        
#         self.buttonSurface.fill(self.fillColors['normal'])
#         if self.buttonRect.collidepoint(mousePos):
#             self.buttonSurface.fill(self.fillColors['hover'])

#             if pygame.mouse.get_pressed(num_buttons=3)[0]:
#                 self.buttonSurface.fill(self.fillColors['pressed'])

#                 if self.onePress:
#                     self.onclickFunction()

#                 elif not self.alreadyPressed:
#                     self.onclickFunction()
#                     self.alreadyPressed = True

#             else:
#                 self.alreadyPressed = False

#         self.buttonSurface.blit(self.buttonSurf, [
#             self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
#             self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
#         ])
#         screen.blit(self.buttonSurface, self.buttonRect)




