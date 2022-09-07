import pygame
from ..widgets import buttons

def run_home_screen(game):
    pygame.init()
    # game loop

    # Draw screen
    game.display_surface.fill((0,255,255))
    test = buttons.TextButton(game.display_surface, (400,60), 100, 50, (0,0,0), (255,255,255), pygame.font.SysFont("arial", 20), "hi")
    
    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False


        pygame.display.update()
        
    pass

