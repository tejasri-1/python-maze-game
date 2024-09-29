import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Text Example")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define font
font = pygame.font.Font(None, 36)

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Render text
    text_surface = font.render("Hello, Pygame!", True, BLACK)

    # Get the rectangle of the text surface
    text_rect = text_surface.get_rect()

    # Center the text on the screen
    text_rect.center = (screen_width // 2, screen_height // 2)

    # Blit the text surface onto the screen
    screen.blit(text_surface, text_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
