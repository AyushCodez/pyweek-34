import pygame
from ..widgets import buttons
from src.utils.load_utils import load_png
from ..utils import constants
from src.utils import music_controller

def run_home_screen(game):

    music_controller.update_volume()
    music_controller.stop_fx2()
    music_controller.stop_fx3()
    music_controller.stop_fx4()
    music_controller.stop_bg()
    music_controller.play_home_bg()

    pygame.init()
    
    # game loop
    bg,bg_size = load_png("title_screen.png")
    bg = pygame.transform.scale(bg, (800,600))
    game.display_surface.blit(bg,(0,0))

    # Draw screen
    test = buttons.TextButton(game.display_surface, (400,60), 100, 50, (0,0,0), (255,255,255), pygame.font.SysFont("arial", 20), "play game")

    war = buttons.TextButton(game.display_surface, (500,20), 100, 50, (0,0,0), (255,255,255), pygame.font.SysFont("arial", 20), "screen 2")

    title_text = constants.FONT_MAIN_SCREEN.render('Empyrean', True, (255, 100, 56))
    caption_text = constants.FONT_CAPTION_TEXT.render('The war for freedom', True, (255,132,73))
    game.display_surface.blit(title_text, (constants.W / 2 - title_text.get_width() / 2, 140))
    game.display_surface.blit(caption_text, (constants.W / 2 - caption_text.get_width() / 2, 240))


    while game.running:
        mouse_down = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True

        if test.hovered:
            test.toggle_bg((0,100,0))
            if mouse_down:
                test.toggle_bg((255,255,255))
                game.screen = 1 
                return
        else:
            test.toggle_bg((255,255,255))
        
        if war.hovered:
            war.toggle_bg((0,100,0))
            if mouse_down:
                war.toggle_bg((255,255,255))
                game.screen = 2
                return

        pygame.display.update()
        
    pass

