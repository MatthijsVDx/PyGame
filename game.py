import pygame
pygame.init()


screen_height = 600
screen_width = 800

screen = pygame.display.set_mode((screen_width, screen_height))

player = pygame.Rect((300,250,50,50))

run = True
while run:
    
    player.move_ip(1,1)
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,0,0), player)
    
    key = pygame.key.get_pressed()

#Moving up
    if key [pygame.K_w] == True:
        player.move_ip(0, -2)

    elif key [pygame.K_ESCAPE] == True:
        pygmae.QUIT
    
    white = (255,255,255)
    
    groundstart_pos = (200, 200)
    groundend_pos = (800, 200)
    ground_height = 10
    
    pygame.draw.line(screen, white, groundstart_pos, groundend_pos, ground_height)
    
 
            
    pygame.display.update()        
pygame.quit()

