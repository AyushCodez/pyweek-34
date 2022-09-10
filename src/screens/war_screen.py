import imp
import pygame

from src.utils.load_utils import load_png
from ..widgets import buttons
from src.utils.constants import W,H
from src.models.scout import Scout

def run_war_screen(game):
    pygame.init()
    surface = game.display_surface
    bg,bg_size = load_png("map_screen_bg.png")
    bg = pygame.transform.scale(bg, (800,600))

    while game.running:

        surface.blit(bg,(0,0))

        mouse_down = False
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_down = True
        pygame.display.update()

