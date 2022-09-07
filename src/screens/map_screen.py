import pygame
from ..widgets import buttons

def run_map_screen(game):
    pygame.init()
    # game loop

    # Draw screen
    game.display_surface.fill((255,0,255))
    test = buttons.TextButton(game.display_surface, (400,60), 100, 50, (0,0,0), (255,255,255), pygame.font.SysFont("arial", 20), "go back make map")
    
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
                game.screen = 0
                return
                
        else:
            test.toggle_bg((255,255,255))

        pygame.display.update()
        
    pass

