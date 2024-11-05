import pygame
import sys



# Initialize Pygame
pygame.init()

current_screen = "menu"


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

#Quit Button
sc_quit_btn = pygame.image.load("assets/tekst/quit.png").convert()
quit_btn_rect = sc_quit_btn.get_rect(midbottom = (200,325))

#startscreen game name
game_name_image = pygame.image.load("assets/tekst/jumanji_dash.png").convert()
game_name = pygame.transform.scale(game_name_image, (250, 125))
game_name_rect = game_name.get_rect(midbottom = (400, 170))

def menu_screen():
     #click event

    if event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse click
            mouse_pos = pygame.mouse.get_pos()  #Mouse position

            # Check if the click is within the rect
            if play_btn_rect.collidepoint(mouse_pos):
                current_screen = "main"
            elif quit_btn_rect.collidepoint(mouse_pos):
                running = False
                
      #click event

                
                  
    #Load images on screen
    screen.blit(sc_background, (0,0))
    screen.blit(game_name, game_name_rect)
    screen.blit(sc_decoration, (70,200))
    screen.blit(sc_play_btn, play_btn_rect)
    screen.blit(sc_quit_btn, quit_btn_rect)
    
                
def main_screen():
      # Calculate elapsed time
  elapsed_time = time.time() - start_time

  # Cube speed
  cube_speed = 16

  # Move the cube automatically to the right
  cube_x += cube_speed

  # Handle jumping and descending
  keys = pygame.key.get_pressed()
  if (keys[pygame.K_w] or keys[pygame.K_UP]) and not is_jumping:
    cube_y_velocity = -JUMP_HEIGHT
    is_jumping = True
  if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and is_jumping:
    cube_y_velocity += GRAVITY

  # Apply gravity
  cube_y_velocity += GRAVITY
  cube_y += cube_y_velocity

  # Check if the cube is on the platform
  if cube_y >= SCREEN_HEIGHT - ground_height - CUBE_SIZE:
    cube_y = SCREEN_HEIGHT - ground_height - CUBE_SIZE
    cube_y_velocity = 0
    is_jumping = False

  # Calculate the offset to keep the cube centered
  offset_x = cube_x - SCREEN_WIDTH // 2

  # Move the background to the left
  background_x -= 0.8
  if background_x <= -SCREEN_WIDTH:
    background_x = 0


  # Clear the screen and draw the background
  screen.blit(background_image, (background_x, 0))
  screen.blit(background_image, (background_x + SCREEN_WIDTH, 0))

  # Draw the ground segments
  for segment in ground_segments:
    segment_x, segment_y = segment
    screen.blit(ground_image, (segment_x - offset_x, segment_y))
     #screen.blit(obs_1_image, (600, segment_y /1.32))


  # Regenerate ground segments/
    if ground_segments[0][0] - offset_x < -ground_width:
        ground_segments.pop(0)
        new_segment_x = ground_segments[-1][0] + ground_width
        ground_segments.append((new_segment_x, SCREEN_HEIGHT - ground_height))

  # Draw the cube at the center of the screen
    screen.blit(cube_image, (SCREEN_WIDTH // 2 - CUBE_SIZE // 2, cube_y))

  # Draw the timer
    font = pygame.font.SysFont(None, 36)
    timer_text = font.render(f"Time: {int(elapsed_time)}s", True, WHITE)
    screen.blit(timer_text, (10, 10))

  # Update the display

  # Cap the frame rate
    pygame.time.Clock().tick(60)
  



# Game loop
running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
          
    if current_screen == "menu":
      menu_screen()
    elif current_screen == "main":
      main_screen()
    
    pygame.display.update()

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
    
    
   

    
pygame.quit()
sys.exit()