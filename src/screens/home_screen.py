import pygame
from ..widgets import buttons

def run_home_screen(game):
    pygame.init()
    # game loop
    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False

        # Draw screen
        test = buttons.TextButton(game.display_surface, (400,60), 100, 80, (0,0,0), (255,255,255), pygame.font.SysFont("arial", 6), "hi")
        
    pass

