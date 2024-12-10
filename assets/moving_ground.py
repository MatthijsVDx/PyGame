import pygame
import math

# Initialize Pygame
pygame.init()

# Frame rate
clock = pygame.time.Clock()
fps = 60

# Contants
SCREEN_WIDTH = 950
SCREEN_HEIGHT = 550

# Display screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load image
bg = pygame.image.load('background/background_2.png').convert()
bg_width = bg.get_width()
bg_floor = pygame.image.load("platforms/main-platform/ground_2.png").convert()
bg_floor_width = bg_floor.get_width()
bg_floor_height = bg_floor.get_height()

# Define game variables
tiles_bg = math.ceil(SCREEN_WIDTH / bg_width) + 1
tiles_floor = math.ceil(SCREEN_WIDTH / bg_floor_width) + 1
scroll_bg = 0
scroll_floor = 0


# Game loop
run = True
while run:
    clock.tick(fps)

    # Draw background
    for i in range(0, tiles_bg):
        screen.blit(bg, (i * bg_width + scroll_bg, 0))
    for i in range(0, tiles_floor):
        screen.blit(bg_floor, (i * bg_floor_width + scroll_floor, SCREEN_HEIGHT - bg_floor_height))


    # Scroll background
    scroll_bg -= 1
    scroll_floor -= 6

    # Reset scroll
    if abs(scroll_bg) > bg_width:
        scroll_bg = 0
    if abs(scroll_floor) > bg_floor_width:
        scroll_floor = 0




    # Event handeler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()