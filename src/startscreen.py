import pygame
import sys



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
sc_background = pygame.image.load("assets/background/bg_startscreen.png")
sc_decoration = pygame.image.load("assets/tekst/decoration.png")

#Play Button
sc_play_btn = pygame.image.load("assets/tekst/play.png").convert()
play_btn_rect = sc_play_btn.get_rect(midbottom = (600,325))

#startscreen game name
game_name_image = pygame.image.load("assets/tekst/jumanji_dash.png").convert()
game_name = pygame.transform.scale(game_name_image, (250, 125))
game_name_rect = game_name.get_rect(midbottom = (400, 170))

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
  
  
    #Load images on screen
    screen.blit(sc_background, (0,0))
    screen.blit(game_name, game_name_rect)
    screen.blit(sc_decoration, (70,200))
    screen.blit(sc_play_btn, play_btn_rect)

    
pygame.quit()
sys.exit()