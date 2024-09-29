import pygame
from pygame.locals import *
import maze_generation as m
import level

#levelsel shows the level selected in the given 4 levels.
def detec_level(mouse_pos,grade,screen,importwall):
    global levelsel
    if grade==1:
        if level.level1.collidepoint(mouse_pos):
            m.beglevel1(screen,importwall)
            levelsel=1
            return False
        elif level.level2.collidepoint(mouse_pos):
            m.beglevel2(screen,importwall)
            levelsel=2
            return False
        elif level.level3.collidepoint(mouse_pos):
            m.beglevel3(screen,importwall)
            levelsel=3
            return False
        elif level.level4.collidepoint(mouse_pos):
            m.beglevel4(screen,importwall)
            levelsel=4
            return False
    elif grade==2:
        if level.level1.collidepoint(mouse_pos):
            m.medlevel1(screen,importwall)
            levelsel=1
            return False
        elif level.level2.collidepoint(mouse_pos):
            m.medlevel2(screen,importwall)
            levelsel=2
            return False
        elif level.level3.collidepoint(mouse_pos):
            m.medlevel3(screen,importwall)
            levelsel=3
            return False
        elif level.level4.collidepoint(mouse_pos):
            m.medlevel4(screen,importwall)
            levelsel=4
            return False
    elif grade==3:
        if level.level1.collidepoint(mouse_pos):
            m.advlevel1(screen,importwall)
            levelsel=1
            return False
        elif level.level2.collidepoint(mouse_pos):
            m.advlevel2(screen,importwall)
            levelsel=2
            return False
        elif level.level3.collidepoint(mouse_pos):
            m.advlevel3(screen,importwall)
            levelsel=3
            return False
        elif level.level4.collidepoint(mouse_pos):
            m.advlevel4(screen,importwall)
            levelsel=4
            return False