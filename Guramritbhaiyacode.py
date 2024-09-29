import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Number Grid")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Define font
font = pygame.font.SysFont(None, 36)

# Define box dimensions
box_width = screen_width // 4
box_height = screen_height // 4

# Function to draw grid
def draw_grid():
    for i in range(4):
        for j in range(4):
            pygame.draw.rect(screen, black, (i * box_width, j * box_height, box_width, box_height), 2)
            number = i * 4 + j + 1
            text_surface = font.render(str(number), True, black)
            text_rect = text_surface.get_rect(center=(i * box_width + box_width // 2, j * box_height + box_height // 2))
            screen.blit(text_surface, text_rect)

# Main loop
running = True
while running:
    screen.fill(white)
    draw_grid()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
