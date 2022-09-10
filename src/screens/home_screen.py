import pygame
from ..widgets import buttons
from src.utils.load_utils import load_png

def run_home_screen(game):
    pygame.init()
    surface = game.display_surface
    # game loop

    # Draw screen
    test = buttons.TextButton(game.display_surface, (400,60), 100, 50, (0,0,0), (255,255,255), pygame.font.SysFont("arial", 20), "play game")

    war = buttons.TextButton(game.display_surface, (400,60), 100, 50, (0,0,0), (255,255,255), pygame.font.SysFont("arial", 20), "screen 2")
    bg,bg_size = load_png("title_screen.png")
    bg = pygame.transform.scale(bg, (800,600))


    while game.running:
        mouse_down = False

        surface.blit(bg,(0,0))

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

