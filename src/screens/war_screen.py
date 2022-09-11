import pygame
from src.models.war_base import WarBase
import math

from src.utils.load_utils import load_png
from ..widgets import buttons
from src.utils.constants import W,H

def run_war_screen(game):
    pygame.init()
    surface = game.display_surface
    bg,bg_size = load_png("war_screen.png")
    bg = pygame.transform.scale(bg, (800,600))

    surface.blit(bg,(0,0))

    test = buttons.TextButton(surface, (400,60), 100, 50, (0,0,0), (255,255,255), pygame.font.SysFont("arial", 20), "go back make map")

    base_g = WarBase(0, 1)
    base_b = WarBase(1, 1)

    base_g.draw(surface, (10, 250))
    base_b.draw(surface, (672, 275))

    draw_health_bar(surface, (10, 300), base_g.health, width=100)
    draw_health_bar(surface, (574, 300), base_b.health, width=100)

    while game.running:


        # draw_timer()


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



def draw_health_bar(screen, position, health, width):
    background_box = pygame.draw.rect(screen, (80,80,80), pygame.Rect(position[0], position[1], width, 10))
    fill_width = health//100
    health_box = pygame.draw.rect(screen, (72, 255, 78), pygame.Rect(position[0], position[1], fill_width, 10))
