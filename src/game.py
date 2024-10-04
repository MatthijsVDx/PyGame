import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 750 
CUBE_SIZE = 65
PLATFORM_HEIGHT = 20
INITIAL_CUBE_SPEED = 5  # 5 pixels per frame
JUMP_HEIGHT = 20  # 15 pixels per frame
GRAVITY = 1  # 1 pixel per frame
SPEED_INCREASE_RATE = 0.05  # 5% increase

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Geometry Dash")

# Load images
background_image = pygame.image.load("assets/background/bg.png").convert()
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

cube_image = pygame.image.load("assets/player/cube_player.png").convert_alpha()
cube_image = pygame.transform.scale(cube_image, (CUBE_SIZE, CUBE_SIZE))

ground_image = pygame.image.load("assets/platforms/main-platform/ground_1.png").convert()
ground_width, ground_height = ground_image.get_size() 
ground_image = pygame.transform.scale(ground_image, (int(ground_width * 0.75), int(ground_height * 0.75)))
ground_width, ground_height = ground_image.get_size()



# Load music
pygame.mixer.music.load('songs/Clubstep.mp3')

# Set volume
MUSIC_VOLUME = 0.1  # Volume level from 0.0 to 1.0
pygame.mixer.music.set_volume(MUSIC_VOLUME)

# Play the music
pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely

# Cube position and velocity
cube_x = 100
cube_y = SCREEN_HEIGHT - ground_height - CUBE_SIZE 
cube_y_velocity = 0
is_jumping = False

# Ground segments
ground_segments = [(i * ground_width, SCREEN_HEIGHT - ground_height / 2) for i in range(3)]
ground_height = ground_height // 2

# Timer
start_time = time.time()

# Initialize background position
background_x = 0

# Game loop
running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Calculate elapsed time
  elapsed_time = time.time() - start_time

  # Cube speed
  cube_speed = 12.5

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
  background_x -= 1
  if background_x <= -SCREEN_WIDTH:
    background_x = 0

  # Clear the screen and draw the background
  screen.blit(background_image, (background_x, 0))
  screen.blit(background_image, (background_x + SCREEN_WIDTH, 0))

  # Draw the ground segments
  for segment in ground_segments:
    segment_x, segment_y = segment
    screen.blit(ground_image, (segment_x - offset_x, segment_y))

  # Regenerate ground segments
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
  pygame.display.update()

  # Cap the frame rate
  pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
