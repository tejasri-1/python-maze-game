import pygame
from pygame.locals import *

def gamescreen(screen,x,y,dist,grade,copiedscreen):
    if grade == 1 :
        if x>=3 and y>=2:
            camera = pygame.Rect((x-3)*dist,(y-2)*dist,7*dist,5*dist)
        elif x>=3 and y<2:
            camera = pygame.Rect((x-3)*dist,0,7*dist,5*dist)
        elif x<3 and y>=2:
            camera = pygame.Rect(0,(y-2)*dist,7*dist,5*dist)
        elif x<3 and y<2:
            camera = pygame.Rect(0,0,7*dist,5*dist)
        if x>9 and y>6:
            camera = pygame.Rect(6*dist,4*dist,7*dist,5*dist)
        if x>9 and y<=6:
            camera = pygame.Rect(6*dist,(y-2)*dist,7*dist,5*dist)
        if x<=9 and y>6:
            camera = pygame.Rect((x-3)*dist,4*dist,7*dist,5*dist)
        
        camerascreen=pygame.Surface((int(7*dist),int(7*dist)))
        camerascreen.blit(copiedscreen,(0,0),camera)
        screen.blit(camerascreen, (0, 0))
        
        