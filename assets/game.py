import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400 
CUBE_SIZE = 52
PLATFORM_HEIGHT = 20
INITIAL_CUBE_SPEED = 5  # 5 pixels per frame
JUMP_HEIGHT = 20  # 20 pixels per frame
GRAVITY = 1  # 1 pixel per frame
SPEED_INCREASE_RATE = 0.05
current_pos = (265, 180)

# Screen management
current_screen = 'menu'

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Geometry Dash")

# Load images
background_image = pygame.image.load("./background/background.png").convert()
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

cube_image = pygame.image.load("./player/cube_player.png").convert_alpha()
cube_image = pygame.transform.scale(cube_image, (CUBE_SIZE, CUBE_SIZE))

ground_image = pygame.image.load("./platforms/main-platform/floor.png").convert()
ground_width, ground_height = ground_image.get_size()
ground_image = pygame.transform.scale(ground_image, (int(ground_width * 1.5), int(ground_height * 1.5)))
ground_width, ground_height = ground_image.get_size()

obs_1_image = pygame.image.load("./spikes/obstacle_1.png").convert_alpha()
obs_1_image = pygame.transform.scale(obs_1_image, (75, 75)) 

#startscreen background
sc_background_size = pygame.image.load("./background/bg_startscreen.png")
sc_background = pygame.transform.scale(sc_background_size, (800, 400))
sc_decoration = pygame.image.load("./tekst/decoration.png")

#startscreen game name
game_name_image = pygame.image.load("./tekst/jumanji_dash.png").convert_alpha()
game_name = pygame.transform.scale(game_name_image, (380, 75))
game_name_rect = game_name.get_rect(midbottom = (212.5, 90))

#settings screen
setting_bg = pygame.image.load("./background/volume_bg.png").convert_alpha()
exit_btn = pygame.image.load("./tekst/setting_sc/exit_btn.png").convert_alpha()
exit_btn_rect = exit_btn.get_rect(midbottom = (715,125))
volume_icon = pygame.image.load("./tekst/setting_sc/volume.png").convert_alpha()
volume_line = pygame.image.load("./tekst/setting_sc/volume_line.png").convert_alpha()

point1 = pygame.image.load("./tekst/setting_sc/point1.png").convert_alpha()
point1_rect = point1.get_rect(midbottom = (275, 243))

point2 = pygame.image.load("./tekst/setting_sc/point2.png").convert_alpha()
point2_rect = point1.get_rect(midbottom = (375, 243))

point3 = pygame.image.load("./tekst/setting_sc/point3.png").convert_alpha()
point3_rect = point1.get_rect(midbottom = (475, 243))

point4 = pygame.image.load("./tekst/setting_sc/point4.png").convert_alpha()
point4_rect = point1.get_rect(midbottom = (585, 243))

point5 = pygame.image.load("./tekst/setting_sc/point5.png").convert_alpha()
point5_rect = point1.get_rect(midbottom = (700, 243))

selector = pygame.image.load("./tekst/setting_sc/selector.png").convert_alpha()
selector_rect = selector.get_rect(midbottom = (current_pos))

#Tutorial Button
sc_tutorial_btn = pygame.image.load("./tekst/tutorial.png").convert_alpha()
sc_tutorial1_btn = pygame.image.load("./explanation/nl/1.png").convert_alpha()
sc_tutorial2_btn = pygame.image.load("./explanation/nl/2.png").convert_alpha()
sc_tutorial3_btn = pygame.image.load("./explanation/nl/3.png").convert_alpha()
sc_tutorial4_btn = pygame.image.load("./explanation/nl/4.png").convert_alpha()
sc_tutorial5_btn = pygame.image.load("./explanation/nl/5.png").convert_alpha()
sc_tutorial6_btn = pygame.image.load("./explanation/nl/6.png").convert_alpha()
sc_tutorial_btn_back = pygame.image.load("./buttons/arrow_back.png").convert_alpha()
sc_tutorial_btn_forward = pygame.image.load("./buttons/arrow_forward.png").convert_alpha()
sc_tutorial_bg = pygame.image.load("./background/tutorial_bg.png").convert_alpha()
home_button_image = pygame.image.load("./buttons/home_button.png").convert_alpha()
home_button_image = pygame.transform.scale(home_button_image, (50, 50))
home_button_rect = home_button_image.get_rect(topleft=(10, 10))
tutorial_btn_rect = sc_tutorial_btn.get_rect(midbottom = (100,230))
tutorial_btn_forward_rect = sc_tutorial_btn_forward.get_rect(midbottom = (775,250))
tutorial_btn_back_rect = sc_tutorial_btn_back.get_rect(midbottom = (25,250))

#Play Button
sc_play_btn = pygame.image.load("./tekst/play.png").convert_alpha()
play_btn_rect = sc_play_btn.get_rect(midbottom = (78,285))

#Quit Button
sc_quit_btn = pygame.image.load("./tekst/quit.png").convert_alpha()
quit_btn_rect = sc_quit_btn.get_rect(midbottom = (74,345))

#settings Button
sc_setting_btn = pygame.image.load("./tekst/setting.png").convert_alpha()
setting_btn_rect = sc_setting_btn.get_rect(midbottom = (750,75))

# Load music
pygame.mixer.music.load("./songs/Clubstep.mp3")

# Set volume
MUSIC_VOLUME = 0.1  # Volume level from 0.0 to 1.0
pygame.mixer.music.set_volume(MUSIC_VOLUME)

#function for music
def play_music():
  pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely
  
#count for music so it plaus in the loop
count = 0

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

# Initialize tutorial page index
tutorial_page = 1

# Initialize clock
clock = pygame.time.Clock()

# Function to update tutorial screen
def update_tutorial_screen():
  screen.blit(sc_tutorial_bg, (-20, 0))
  tutorial_images = [sc_tutorial1_btn, sc_tutorial2_btn, sc_tutorial3_btn, sc_tutorial4_btn, sc_tutorial5_btn, sc_tutorial6_btn]
  screen.blit(tutorial_images[tutorial_page - 1], (55, 21))

  if tutorial_page > 1:
    screen.blit(sc_tutorial_btn_back, tutorial_btn_back_rect)
  if tutorial_page < 6:
    screen.blit(sc_tutorial_btn_forward, tutorial_btn_forward_rect)
  screen.blit(home_button_image, home_button_rect)

# Main game loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if event.type == pygame.MOUSEBUTTONDOWN:
      mouse_pos = pygame.mouse.get_pos()

      if current_screen == 'menu':
        if play_btn_rect.collidepoint(mouse_pos):
          current_screen = "main"
        elif tutorial_btn_rect.collidepoint(mouse_pos):
          current_screen = 'tutorial'
        elif quit_btn_rect.collidepoint(mouse_pos):
          running = False
        elif setting_btn_rect.collidepoint(mouse_pos):
          current_screen = 'setting'
      elif current_screen == 'setting':
        if exit_btn_rect.collidepoint(mouse_pos):
          current_screen = "menu"
      elif current_screen == 'tutorial':
        if tutorial_btn_back_rect.collidepoint(mouse_pos) and tutorial_page > 1:
          tutorial_page -= 1
        elif tutorial_btn_forward_rect.collidepoint(mouse_pos) and tutorial_page < 6:
          tutorial_page += 1
        if home_button_rect.collidepoint(mouse_pos):
          current_screen = 'menu'

      if point1_rect.collidepoint(mouse_pos):
        current_pos = (265, 180)
        MUSIC_VOLUME = 0.2
      elif point2_rect.collidepoint(mouse_pos):
        current_pos = (365, 180)
        MUSIC_VOLUME = 0.4
      elif point3_rect.collidepoint(mouse_pos):
        current_pos = (465, 180)
        MUSIC_VOLUME = 0.6
      elif point4_rect.collidepoint(mouse_pos):
        current_pos = (575, 180)
        MUSIC_VOLUME = 0.8
      elif point5_rect.collidepoint(mouse_pos):
        current_pos = (690, 180)
        MUSIC_VOLUME = 1.0

  if current_screen == 'menu':
    screen.blit(sc_background, (0, 0))
    screen.blit(game_name, game_name_rect)
    screen.blit(sc_play_btn, play_btn_rect)
    screen.blit(sc_tutorial_btn, tutorial_btn_rect)
    screen.blit(sc_quit_btn, quit_btn_rect)
    screen.blit(sc_setting_btn, setting_btn_rect)
    screen.blit(sc_decoration, (45, 235))
    screen.blit(sc_decoration, (45, 290))
    screen.blit(sc_decoration, (45, 350))
    pygame.display.update()
  elif current_screen == 'main':
    if count < 1:
      play_music()
    count += 1
    elapsed_time = time.time() - start_time
    cube_speed = INITIAL_CUBE_SPEED * (1 + SPEED_INCREASE_RATE * int(elapsed_time))
    cube_x += cube_speed
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_SPACE]) and not is_jumping:
      cube_y_velocity = -JUMP_HEIGHT
      is_jumping = True
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and is_jumping:
      cube_y_velocity += GRAVITY
    cube_y_velocity += GRAVITY
    cube_y += cube_y_velocity
    if cube_y >= SCREEN_HEIGHT - ground_height - CUBE_SIZE:
      cube_y = SCREEN_HEIGHT - ground_height - CUBE_SIZE
      cube_y_velocity = 0
      is_jumping = False
    offset_x = cube_x - SCREEN_WIDTH // 2
    screen.blit(background_image, (0, 0))
    for segment in ground_segments:
      segment_x, segment_y = segment
      screen.blit(ground_image, (segment_x - offset_x, segment_y))
    if ground_segments[0][0] - offset_x < -ground_width:
      ground_segments.pop(0)
      new_segment_x = ground_segments[-1][0] + ground_width
      ground_segments.append((new_segment_x, SCREEN_HEIGHT - ground_height))
    screen.blit(cube_image, (SCREEN_WIDTH // 2 - CUBE_SIZE // 2, cube_y))
    font = pygame.font.SysFont(None, 36)
    timer_text = font.render(f"Time: {int(elapsed_time)}s", True, WHITE)
    screen.blit(timer_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)
  elif current_screen == 'setting':
    # Define a list of elements to blit
    elements_to_blit = [
        (setting_bg, (80, 80)),
        (exit_btn, exit_btn_rect),
        (volume_icon, (140, 170)),
        (volume_line, (265, 205)),
        (point1, point1_rect),
        (point2, point2_rect),
        (point3, point3_rect),
        (point4, point4_rect),
        (point5, point5_rect),
        (selector, current_pos)
    ]
    # Blit all elements in a loop
    for element, position in elements_to_blit:
        screen.blit(element, position)
    pygame.display.update()
  elif current_screen == 'tutorial':
    update_tutorial_screen()
    pygame.display.update()
  pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()