import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Copy Rectangle Example")

# Create an old surface (e.g., a background image)
old_surface = pygame.Surface((width, height))
old_surface.fill((255, 255, 255))  # Fill with white for demonstration purposes
pygame.draw.rect(old_surface, (255, 0, 0), (100, 100, 200, 150))  # Draw a red rectangle on the old surface

# Define the rectangle to copy
copy_rect = pygame.Rect(100, 100, 200, 150)

# Create a new surface to copy the rectangle onto
new_surface = pygame.Surface((copy_rect.width, copy_rect.height))

# Copy the rectangle from the old surface to the new one
new_surface.blit(old_surface, (0, 0), copy_rect)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with white
    screen.fill((255, 255, 255))
    
    # Blit the new surface onto the screen at position (100, 100)
    screen.blit(new_surface, (0,0))
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
