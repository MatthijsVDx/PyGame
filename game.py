import pygame
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_height, screen_width))

player = pygame.Rect((300,250,50,50))

run = True
while run:
    
    
    pygame.draw.rect(screen,(255,0,0), player)
    
    key = pygame.key.get_pressed()
#Moving left
    if key [pygame.K_a] == True:
        player.move_ip(-1, 0)
#Moving right
    elif key [pygame.K_d] == True:
        player.move_ip(1, 0)
#Moving up
    elif key [pygame.K_w] == True:
        player.move_ip(0, -1)
#Moving down
    elif key [pygame.K_s] == True:
        player.move_ip(0, 1)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()
            
pygame.quit()

