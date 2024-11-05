def main_screen():
    # Constants
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 400 
    CUBE_SIZE = 52
    PLATFORM_HEIGHT = 20
    INITIAL_CUBE_SPEED = 5  # 5 pixels per frame
    JUMP_HEIGHT = 20  # 15 pixels per frame
    GRAVITY = 1  # 1 pixel per frame
    SPEED_INCREASE_RATE = 0.05 



    # 5% increase
    current_screen = "menu"

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Geometry Dash")

    # Load images
    background_image = pygame.image.load("assets/background/background.png").convert()
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    cube_image = pygame.image.load("assets/player/cube_player.png").convert_alpha()
    cube_image = pygame.transform.scale(cube_image, (CUBE_SIZE, CUBE_SIZE))

    ground_image = pygame.image.load("assets/platforms/main-platform/floor.png").convert()
    ground_width, ground_height = ground_image.get_size()
    ground_image = pygame.transform.scale(ground_image, (int(ground_width * 1.5), int(ground_height * 1.5)))
    ground_width, ground_height = ground_image.get_size()

    obs_1_image = pygame.image.load("assets\spikes\obstacle_1.png").convert_alpha()
    obs_1_image = pygame.transform.scale(obs_1_image, (75, 75))
    #obs_1_hitbox = obs_1_image.get_t
    
    #from click things
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