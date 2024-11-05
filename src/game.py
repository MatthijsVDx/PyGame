import pygame
import sys
import time
from menu_screen import menu_screen
from main_screen import main_screen


#screen management
current_screen = 'main'

# Initialize Pygame
pygame.init()


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
                

    #change to menu screen
    if current_screen == 'menu':
      
      if event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse click
          mouse_pos = pygame.mouse.get_pos()  #Mouse position

          # Check if the click is within the rect
          if play_btn_rect.collidepoint(mouse_pos):
                  current_screen = "main"
          elif quit_btn_rect.collidepoint(mouse_pos):
                  running = False
                
      
      #Load images on screen
      screen.blit(sc_background, (0,0))
      screen.blit(game_name, game_name_rect)
      screen.blit(sc_decoration, (70,200))
      screen.blit(sc_play_btn, play_btn_rect)
      screen.blit(sc_quit_btn, quit_btn_rect)
          
                      

      pygame.display.update()

          # Update the display
      pygame.display.update()

        # Cap the frame rate
      pygame.time.Clock().tick(60)
      
      
      

    #display main screen
    elif current_screen == 'main':
    
      # Calculate elapsed time
      elapsed_time = time.time() - start_time

      # Increase speed every second
      cube_speed = INITIAL_CUBE_SPEED * (1 + SPEED_INCREASE_RATE * int(elapsed_time))

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

      # Clear the screen
      screen.blit(background_image, (0, 0))

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
      pygame.display.flip()

      # Cap the frame rate
      pygame.time.Clock().tick(60)

    else:
      pass

    
pygame.quit()
sys.exit()
