import pygame
import sys
import time


# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400 

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jumanji Dash")

#load images
sc_background = pygame.image.load("assets/background/bg_startscreen.png").convert()


# Game loop
running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
  
  
  screen.blit(sc_background, (0,0))
    
pygame.quit()
sys.exit()