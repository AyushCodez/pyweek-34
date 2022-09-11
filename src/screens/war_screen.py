import imp
import pygame

from src.utils.load_utils import load_png
from ..widgets import buttons
from src.utils.constants import W,H
from src.models.scout import Scout

def run_war_screen(game):
    pygame.init()
    surface = game.display_surface
    bg,bg_size = load_png("war_screen.png")
    bg = pygame.transform.scale(bg, (800,600))

    while game.running:

        surface.blit(bg,(0,0))

        test = buttons.TextButton(surface, (400,60), 100, 50, (0,0,0), (255,255,255), pygame.font.SysFont("arial", 20), "go back make map")

        base_1, base_1_size = load_png("war_base_good_base.png");
        base_2, base_2_size = load_png("war_base_bad_base.png");

        surface.blit(base_1, (400,0))
        surface.blit(base_2, (400,300))


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
        

        pygame.display.update()

