import imp
import pygame

from src.utils.load_utils import load_png
from ..widgets import buttons
from src.utils.constants import W,H
from src.models.scout import Scout

def run_map_screen(game):
    pygame.init()
    # game loop
    base_coords = (W/2,H/2)
    # Draw screen
    Scouts = Scout(base_coords)
    Scouts.create(2)
    surface = game.display_surface

    while game.running:
        surface.fill((255,0,255))
        test = buttons.TextButton(surface, (400,60), 100, 50, (0,0,0), (255,255,255), pygame.font.SysFont("arial", 20), "go back make map")
        scout,scout_size = load_png("scout.png")
        base,base_size = load_png("base.png")
        surface.blit(base,base_coords)
        create_scout = buttons.TextButton(surface, (0,570), 90, 20, (0,0,0), (255,255,255), pygame.font.SysFont("arial", 15), "Create Scout")
        send_scout = buttons.TextButton(surface, (100,570), 90, 20, (0,0,0), (255,255,255), pygame.font.SysFont("arial", 15), "Send Scout")
        text = pygame.font.Font('freesansbold.ttf', 15).render(f'Number of Scouts: {Scouts.num}  ', True, (0,0,0), (0,0,255))
        surface.blit(text, (0,0))
        text = pygame.font.Font('freesansbold.ttf', 15).render(f'Metal left: {10}  ', True, (0,0,0), (0,0,255)) # TODO: Put variable in
        surface.blit(text, (0,15))
        


        mouse_down = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True

        if create_scout.hovered:
            create_scout.toggle_bg((0,100,0))

            if mouse_down:
                create_scout.toggle_bg((255,255,255))
                Scouts.create()
                
        else:
            test.toggle_bg((255,255,255))

        if send_scout.hovered:
            send_scout.toggle_bg((0,100,0))

            if mouse_down:
                send_scout.toggle_bg((255,255,255))
                Scouts.create()
                
        else:
            test.toggle_bg((255,255,255))

        
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

