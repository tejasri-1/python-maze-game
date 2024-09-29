import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Object")

# Load an image
image = pygame.image.load("Redpanda.png")
image_rect = image.get_rect()
image_rect.center = (screen_width // 2, screen_height // 2)  # Center the image initially

# Set the initial movement speed
speed = 5

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the object (image in this case)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        image_rect.move_ip(-speed, 0)
    if keys[pygame.K_RIGHT]:
        image_rect.move_ip(speed, 0)
    if keys[pygame.K_UP]:
        image_rect.move_ip(0, -speed)
    if keys[pygame.K_DOWN]:
        image_rect.move_ip(0, speed)

    # Clear the screen
    screen.fill((0, 0, 0))

    # Blit (draw) the image onto the screen at its updated position
    screen.blit(image, image_rect)

    # Update the display
    pygame.display.flip()

    # Add a small delay to control the frame rate
    pygame.time.delay(30)

# Quit Pygame
pygame.quit()
sys.exit()
