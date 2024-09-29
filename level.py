import pygame
from pygame.locals import *

pygame.init()
# Defining font and some useful colors
font1 = pygame.font.Font(None, 54)
font2= pygame.font.Font(None,45)
font3=pygame.font.Font(None,27)
font4 = pygame.font.Font(None,18)
WHITE=(255,255,255)
BLACK=(0,0,0)
GREY=(200,200,200)
RED=(255,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)

# Main Headings to be placed
head1 = font1.render("Welcome to the Maze World!", True, WHITE)
footer1 = font2.render("Click ESC to exit game",True,WHITE)

# BEGINNER LEVEL 
def beglevel(screen,chooselevelnum):
    swidth,sheight=screen.get_size()
    global level1,level2,level3,level4
    screen.fill(BLACK)
    screen.blit(chooselevelnum,(0,0))
    level1 = pygame.draw.rect(screen, BLACK, (0, sheight/8, swidth/8, 3*sheight/16),1)
    level2 = pygame.draw.rect(screen, BLACK, (0, 17*sheight/32, swidth/8, 3*sheight/16),1)
    level3 = pygame.draw.rect(screen, BLACK, (7*swidth/8, sheight/8, swidth/8, 3*sheight/16),1)
    level4 = pygame.draw.rect(screen, BLACK, (7*swidth/8, 17*sheight/32, swidth/8, 3*sheight/16),1)
    pygame.display.flip()

# MEDIUM LEVEL
def medlevel(screen,chooselevelnum):
    swidth,sheight=screen.get_size()
    global level1,level2,level3,level4
    screen.fill(BLACK)
    screen.blit(chooselevelnum,(0,0))
    level1 = pygame.draw.rect(screen, BLACK, (0, sheight/8, swidth/8, 3*sheight/16),1)
    level2 = pygame.draw.rect(screen, BLACK, (0, 17*sheight/32, swidth/8, 3*sheight/16),1)
    level3 = pygame.draw.rect(screen, BLACK, (7*swidth/8, sheight/8, swidth/8, 3*sheight/16),1)
    level4 = pygame.draw.rect(screen, BLACK, (7*swidth/8, 17*sheight/32, swidth/8, 3*sheight/16),1)
    pygame.display.flip()

# ADVANCED LEVEL
def advlevel(screen,chooselevelnum):
    swidth,sheight=screen.get_size()
    global level1,level2,level3,level4
    screen.fill(BLACK)
    screen.blit(chooselevelnum,(0,0))
    level1 = pygame.draw.rect(screen, BLACK, (0, sheight/8, swidth/8, 3*sheight/16),1)
    level2 = pygame.draw.rect(screen, BLACK, (0, 17*sheight/32, swidth/8, 3*sheight/16),1)
    level3 = pygame.draw.rect(screen, BLACK, (7*swidth/8, sheight/8, swidth/8, 3*sheight/16),1)
    level4 = pygame.draw.rect(screen, BLACK, (7*swidth/8, 17*sheight/32, swidth/8, 3*sheight/16),1)
    pygame.display.flip()

