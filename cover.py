import pygame
from pygame.locals import *

def coverscr(x,y,dist,screen):
    uncoverarea = pygame.Rect(x*dist,y*dist,6*dist,5*dist)
    coverarea1=pygame.Rect()
    pygame.draw.rect(screen,(200,200,200),coverarea)
    pygame.display.flip()