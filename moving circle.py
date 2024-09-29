import pygame
import sys
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Circle")

# Colors
BLUE = (0, 0, 255)

# Initial position of the circle
posx = 0
posy = 0

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_DOWN:
                posy += 1000 / 12
            elif event.key == K_UP:
                posy -= 1000 / 12
            elif event.key == K_LEFT:
                posx -= 1000 / 9
            elif event.key == K_RIGHT:
                posx += 1000 / 9

    # Draw the circle directly onto the screen
    pygame.draw.circle(screen, BLUE, (posx, posy), 10, 10)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
