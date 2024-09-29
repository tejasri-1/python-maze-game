import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Button Touch Example")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)

# Define font
font = pygame.font.Font(None, 36)

# Create a button
button_rect = pygame.Rect(300, 200, 200, 100)
button_text = font.render("Click Me", True, BLACK)

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_pos = pygame.mouse.get_pos()
                if button_rect.collidepoint(mouse_pos):
                    print("Button clicked!")  # Do something when the button is clicked

    # Clear the screen
    screen.fill(WHITE)

    # Draw the button
    pygame.draw.rect(screen, GRAY, button_rect)
    screen.blit(button_text, (button_rect.centerx - button_text.get_width() / 2, button_rect.centery - button_text.get_height() / 2))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
