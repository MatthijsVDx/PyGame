#function for second screen
def menu_screen():
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
  
