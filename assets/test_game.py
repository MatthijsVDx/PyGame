import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
current_pos = (265, 180)
mouse_pos = (0, 0)  # Initialize with a default value
# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Geometry Dash")

#settings screen
setting_bg = pygame.image.load("./background/volume_bg.png")
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
selector_rect = selector.get_rect(midbottom = current_pos)

# Main game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if point1_rect.collidepoint(mouse_pos):
                current_pos = (265, 180)
            elif point2_rect.collidepoint(mouse_pos):
                current_pos = (365, 180)
            elif point3_rect.collidepoint(mouse_pos):
                current_pos = (465, 180)
            elif point4_rect.collidepoint(mouse_pos):
                current_pos = (575, 180)
            elif point5_rect.collidepoint(mouse_pos):
                current_pos = (690, 180)


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



    # Update the display
    pygame.display.update()
pygame.quit()
sys.exit()