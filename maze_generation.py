import pygame
from pygame.locals import *
import numpy as np
import random
from random import randint as x
import cover as c

pygame.init()
# Defining font and some useful colors
WHITE=(255,255,255)
BLACK=(0,0,0)
GREY=(200,200,200)
RED=(255,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
BROWN=(200,0,200)


# levels in beginner
def beglevel1(screen,importwall):
    global maze, startx,starty,endx,endy,dist
    ground=pygame.image.load("Grass1.jpg")
    ground=pygame.transform.scale(ground,screen.get_size())
    startx = 0
    starty = 5
    endy = 7
    endx = 11
    screen.fill(WHITE)
    screen.blit(ground,(0,0))
    ROWS=12
    COLS=9
    dist=1000/ROWS
    CELL_WIDTH= CELL_HEIGHT = dist
    # making wall image
    wall=pygame.transform.scale(importwall,(dist,dist))
    
    maze=[
        [1,1,1,1,1,1,1,1,1,1,1,1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,0,0,0,0,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,0,x(0,1),x(0,1),0,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,0,x(0,1),x(0,1),0,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [0,0,x(0,1),x(0,1),0,0,0,0,x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),0,x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),0,0,0,0,0],
        [1,1,1,1,1,1,1,1,1,1,1,1]
    ]
    
    for row in range(COLS):
        for col in range(ROWS):
            if maze[row][col] == 1:
                screen.blit(wall,(col * CELL_WIDTH, row * CELL_HEIGHT))
    pygame.display.flip()

def beglevel2(screen,importwall):
    global maze, startx,starty,endx,endy,dist
    ground=pygame.image.load("Grass1.jpg")
    ground=pygame.transform.scale(ground,screen.get_size())
    startx = 0
    starty = 5
    endy = 8
    endx = 11
    screen.fill(WHITE)
    ROWS=12
    COLS=9
    dist=1000/ROWS
    CELL_WIDTH= CELL_HEIGHT = dist
    # making wall image
    wall=pygame.transform.scale(importwall,(dist,dist))
    maze=[
        [1,1,1,1,1,1,1,1,1,1,1,1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,1,1,1,1,1,1,1,1,1,1,1]
    ]
    for row in range(COLS):
        for col in range(ROWS):
            if maze[row][col] == 1:
                screen.blit(wall,(col * CELL_WIDTH, row * CELL_HEIGHT))
    pygame.display.flip()
  
    
def beglevel3(screen,importwall):
    global maze, startx,starty,endx,endy,dist
    ground=pygame.image.load("Grass1.jpg")
    ground=pygame.transform.scale(ground,screen.get_size())
    startx = 0
    starty = 5
    endy = 8
    endx = 11
    screen.fill(WHITE)
    ROWS=12
    COLS=9
    dist=750/ROWS
    CELL_WIDTH= CELL_HEIGHT = dist
    # making wall image
    wall=pygame.transform.scale(importwall,(dist,dist))
    maze=[
        [1,1,1,1,1,1,1,1,1,1,1,1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,1,1,1,1,1,1,1,1,1,1,1]
    ]
    for row in range(COLS):
        for col in range(ROWS):
            if maze[row][col] == 1:
                screen.blit(wall,(col * CELL_WIDTH, row * CELL_HEIGHT))
    pygame.display.flip()


def beglevel4(screen,importwall):
    global maze, startx,starty,endx,endy,dist
    ground=pygame.image.load("Grass1.jpg")
    ground=pygame.transform.scale(ground,screen.get_size())
    startx = 0
    starty = 5
    endy = 8
    endx = 11
    screen.fill(WHITE)
    ROWS=12
    COLS=9
    dist=1000/ROWS
    CELL_WIDTH= CELL_HEIGHT = dist
    # making wall image
    wall=pygame.transform.scale(importwall,(dist,dist))
    maze=[
        [1,1,1,1,1,1,1,1,1,1,1,1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,1,1,1,1,1,1,1,1,1,1,1]
    ]
    for row in range(COLS):
        for col in range(ROWS):
            if maze[row][col] == 1:
                screen.blit(wall,(col * CELL_WIDTH, row * CELL_HEIGHT))
    pygame.display.flip()

# levels in medium
def medlevel1(screen,importwall):
    global maze, startx,starty,endx,endy,dist
    ground=pygame.image.load("Grass1.jpg")
    ground=pygame.transform.scale(ground,screen.get_size())
    startx = 0
    starty = 5
    endy = 1
    endx = 15
    screen.fill(WHITE)
    ROWS=16
    COLS=12
    dist=1000/ROWS
    CELL_WIDTH= CELL_HEIGHT = dist
    # making wall image
    wall=pygame.transform.scale(importwall,(dist,dist))
    maze=[
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]
    for row in range(COLS):
        for col in range(ROWS):
            if maze[row][col] == 1:
                screen.blit(wall,(col * CELL_WIDTH, row * CELL_HEIGHT))
    pygame.display.flip()
    

def medlevel2(screen,importwall):
    global maze, startx,starty,endx,endy,dist
    ground=pygame.image.load("Grass1.jpg")
    ground=pygame.transform.scale(ground,screen.get_size())
    startx = 0
    starty = 5
    endy = 11
    endx = 15
    screen.fill(WHITE)
    ROWS=16
    COLS=12
    dist=1000/ROWS
    CELL_WIDTH= CELL_HEIGHT = dist
    # making wall image
    wall=pygame.transform.scale(importwall,(dist,dist))
    maze=[
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]
    for row in range(COLS):
        for col in range(ROWS):
            if maze[row][col] == 1:
                screen.blit(wall,(col * CELL_WIDTH, row * CELL_HEIGHT))
    pygame.display.flip()

    
def medlevel3(screen,importwall):
    global maze, startx,starty,endx,endy,dist
    ground=pygame.image.load("Grass1.jpg")
    ground=pygame.transform.scale(ground,screen.get_size())
    startx = 0
    starty = 5
    endy = 11
    endx = 15
    screen.fill(WHITE)
    ROWS=16
    COLS=12
    dist=1000/ROWS
    CELL_WIDTH= CELL_HEIGHT = dist
    # making wall image
    wall=pygame.transform.scale(importwall,(dist,dist))
    maze=[
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]
    for row in range(COLS):
        for col in range(ROWS):
            if maze[row][col] == 1:
                screen.blit(wall,(col * CELL_WIDTH, row * CELL_HEIGHT))
    pygame.display.flip()


def medlevel4(screen,importwall):
    global maze, startx,starty,endx,endy,dist
    ground=pygame.image.load("Grass1.jpg")
    ground=pygame.transform.scale(ground,screen.get_size())
    startx = 0
    starty = 5
    endy = 11
    endx = 15
    screen.fill(WHITE)
    ROWS=16
    COLS=12
    dist=1000/ROWS
    CELL_WIDTH= CELL_HEIGHT = dist
    # making wall image
    wall=pygame.transform.scale(importwall,(dist,dist))
    maze=[
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]
    for row in range(COLS):
        for col in range(ROWS):
            if maze[row][col] == 1:
                screen.blit(wall,(col * CELL_WIDTH, row * CELL_HEIGHT))
    pygame.display.flip()


# levels in advanced
def advlevel1(screen,importwall):
    global maze, startx,starty,endx,endy,dist
    ground=pygame.image.load("Grass1.jpg")
    ground=pygame.transform.scale(ground,screen.get_size())
    startx = 0
    starty = 5
    endy = 14
    endx = 19
    screen.fill(WHITE)
    ROWS=20
    COLS=16
    dist=1000/ROWS
    CELL_WIDTH= CELL_HEIGHT = dist
    # making wall image
    wall=pygame.transform.scale(importwall,(dist,dist))
    maze=[
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]
    for row in range(COLS):
        for col in range(ROWS):
            if maze[row][col] == 1:
                screen.blit(wall,(col * CELL_WIDTH, row * CELL_HEIGHT))
    pygame.display.flip()


def advlevel2(screen,importwall):
    global maze, startx,starty,endx,endy,dist
    ground=pygame.image.load("Grass1.jpg")
    ground=pygame.transform.scale(ground,screen.get_size())
    startx = 0
    starty = 5
    endy = 14
    endx = 19
    screen.fill(WHITE)
    ROWS=20
    COLS=16
    dist=1000/ROWS
    CELL_WIDTH= CELL_HEIGHT = dist
    # making wall image
    wall=pygame.transform.scale(importwall,(dist,dist))
    maze=[
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]
    for row in range(COLS):
        for col in range(ROWS):
            if maze[row][col] == 1:
                screen.blit(wall,(col * CELL_WIDTH, row * CELL_HEIGHT))
    pygame.display.flip()

    
def advlevel3(screen,importwall):
    global maze, startx,starty,endx,endy,dist
    ground=pygame.image.load("Grass1.jpg")
    ground=pygame.transform.scale(ground,screen.get_size())
    startx = 0
    starty = 5
    endy = 14
    endx = 19
    screen.fill(WHITE)
    ROWS=20
    COLS=16
    dist=1000/ROWS
    CELL_WIDTH= CELL_HEIGHT = dist
    # making wall image
    wall=pygame.transform.scale(importwall,(dist,dist))
    maze=[
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]
    for row in range(COLS):
        for col in range(ROWS):
            if maze[row][col] == 1:
                screen.blit(wall,(col * CELL_WIDTH, row * CELL_HEIGHT))
    pygame.display.flip()


def advlevel4(screen,importwall):
    global maze, startx,starty,endx,endy,dist
    ground=pygame.image.load("Grass1.jpg")
    ground=pygame.transform.scale(ground,screen.get_size())
    startx = 0
    starty = 5
    endy = 14
    endx = 19
    screen.fill(WHITE)
    ROWS=20
    COLS=16
    dist=1000/ROWS
    CELL_WIDTH= CELL_HEIGHT = dist
    # making wall image
    wall=pygame.transform.scale(importwall,(dist,dist))
    maze=[
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),x(0,1),1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]
    for row in range(COLS):
        for col in range(ROWS):
            if maze[row][col] == 1:
                screen.blit(wall,(col * CELL_WIDTH, row * CELL_HEIGHT))
    pygame.display.flip()
