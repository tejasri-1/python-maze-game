import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Arrow Key Input Example")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        # Check for keyboard inputs
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                print("Left arrow key pressed")
            elif event.key == K_RIGHT:
                print("Right arrow key pressed")
            elif event.key == K_UP:
                print("Up arrow key pressed")
            elif event.key == K_DOWN:
                print("Down arrow key pressed")

    # Clear the screen
    screen.fill(WHITE)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
