import pygame
from sys import exit

pygame.init()

screen  = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")

# variable framerate
clock = pygame.time.Clock()

test_font = pygame.font.Font( "font\Pixeltype.ttf", 50)



sky_surface = pygame.image.load("graphics\Sky.png").convert()
ground_surface = pygame.image.load("graphics\ground.png").convert()


score_surf = test_font.render("My Game", False, "black").convert()
score_rect = score_surf.get_rect(center = (400, 50))



snail_surface = pygame.image.load("graphics\snail\snail1.png").convert_alpha()
snail_hitbox  = snail_surface.get_rect(midbottom = (400, 312.5))




player_surface = pygame.image.load("graphics\Player\player_walk_1.png").convert_alpha()
player_hitbox = player_surface.get_rect( midbottom = (80, 312.5))

while True:
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    
#    if event.type == pygame.MOUSEMOTION:
#        if player_hitbox.collidepoint(event.pos):
#            print("Collison")
        
    
    
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, 300))
    
    pygame.draw.rect(screen, "pink", score_rect)
    pygame.draw.rect(screen, "pink", score_rect, 10)
    
    
    screen.blit(score_surf, score_rect)
    screen.blit(player_surface, player_hitbox)
    screen.blit(snail_surface, snail_hitbox)
    
    snail_hitbox.left += -4
    

    if snail_hitbox.right < 0:
        snail_hitbox.left += 900


    
    
    
#framerate
    clock.tick(60)
    pygame.display.update()