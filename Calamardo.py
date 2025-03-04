import pygame, sys
import time
from pygame.locals import *

AMPLE = 800
ALT = 600
TAMANY = (AMPLE,ALT)
RED = (255,0,0)
GREEN = (51,153,102)
GREEN_2 = (51,153,115)
BLUE = (0,0,255)
INDIGO = (75, 0, 130)
ORANGE = (255, 165, 0)
YELLOW = (255,255,153)
VIOLET = (148,0,211)
GREY = (128,128,128)
MARRON = (128,0,0)
BLACK = (0,0,0)
OLIVE = (134,139,73)
CYAN = (0,255,255)
PINK = (255,153,204)
MAGENTA = (255,0,255)
TAN = (210,180,140)
TEAL = (0,128,128)
WHITE = (255,255,255)

pygame.init()
pantalla = pygame.display.set_mode(TAMANY)
pygame.display.set_caption('Rectangle')
i = 125
d = 1
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill(WHITE)


    pygame.draw.ellipse(pantalla, GREEN, (50, 417, 450, 90))
    pygame.draw.ellipse(pantalla, GREEN, (50, 50, 500, 350))
    pygame.draw.rect(pantalla, GREEN, (150, 100, 250, 400))
    pygame.draw.rect(pantalla, BLACK, (75, 445, 400, 30))
    pygame.draw.ellipse(pantalla, GREEN_2, (200, 260, 150, 350))
    pygame.draw.ellipse(pantalla, YELLOW, (150, 150, 100, 200))
    pygame.draw.ellipse(pantalla, YELLOW, (300, 150, 100, 200))
    pygame.draw.rect(pantalla, BLACK, (75, i, 400, 30))
    pygame.draw.rect(pantalla, RED, (330, 175, 40, 150))
    pygame.draw.rect(pantalla, RED, (180, 175, 40, 150))
    i += d
    time.sleep(0.003)
    if i< 30 or i>125:
        d *= -1


    pygame.display.update()
