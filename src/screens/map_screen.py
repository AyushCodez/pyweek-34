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
    Scouts = Scout()
    Scouts.create(2)
    surface = game.display_surface
    modal_showing = False
    x_btn = None

    def show_modal(title, text, color):

        nonlocal modal_showing
        modal_showing = True
        maj_sur = pygame.Surface((800, 600))
        maj_sur.set_alpha(180)
        maj_sur.fill((0,0,0))
        surface.blit(maj_sur, (0, 0))
        text_aaa = pygame.font.Font('freesansbold.ttf', 25).render(title, True, color)
        text_bbb = pygame.font.Font('freesansbold.ttf', 25).render(text, True, (255, 255, 255))

        surf = pygame.Surface((500,
                               20 + text_aaa.get_height() + 5 + text_bbb.get_height() + 20))

        surf.blit(text_aaa, (20, 20))
        surf.blit(text_bbb, (20, 20 + text_aaa.get_rect().height + 5))
        nonlocal x_btn
        x_btn = buttons.TextButton(surface=surf, pos=(470, 0), width=30, height=30, fg_color=(255,255,255),
                           bg_color=(240, 0, 0), font= pygame.font.Font('freesansbold.ttf', 30),
                           text=f'X')

        surface.blit(surf, (W / 2 - 250, H / 2 -
                                        (20 + text_aaa.get_height() + 5 + text_bbb.get_height() + 20)))
        btn_x = W / 2 - 250 + 470
        btn_y = H / 2 - (20 + text_aaa.get_height() + 5 + text_bbb.get_height() + 20) + 0
        return btn_x, btn_y

    while game.running:

        mouse_down = False
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_down = True

        if not(modal_showing):
            surface.fill((255,0,255))
            test = buttons.TextButton(surface, (400,60), 100, 50, (0,0,0), (255,255,255), pygame.font.SysFont("arial", 20), "go back make map")
            scout,scout_size = load_png("scout.png")
            base,base_size = load_png("base.png")
            surface.blit(base,base_coords)
            create_scout = buttons.TextButton(surface, (0,570), 90, 20, (0,0,0), (255,255,255), pygame.font.SysFont("arial", 15), "Create Scout")
            send_scout = buttons.TextButton(surface, (100,570), 90, 20, (0,0,0), (255,255,255), pygame.font.SysFont("arial", 15), "Send Scout")
            text = pygame.font.Font('freesansbold.ttf', 15).render(f'Available Scouts: {Scouts.active.count(0)}/{Scouts.num}  ', True, (0,0,0), (0,0,255))
            surface.blit(text, (0,0))
            text = pygame.font.Font('freesansbold.ttf', 15).render(f'Metal left: {10}  ', True, (0,0,0), (0,0,255)) # TODO: Put variable in
            surface.blit(text, (0,15))
                      

            if create_scout.hovered:
                create_scout.toggle_bg((0,100,0))

                if mouse_down:
                    create_scout.toggle_bg((255,255,255))
                    print("HI")
                    Scouts.create()
                    #TODO: use money/metal
                    
            else:
                test.toggle_bg((255,255,255))

            if send_scout.hovered:
                send_scout.toggle_bg((0,100,0))

                if mouse_down:
                    send_scout.toggle_bg((255,255,255))
                    if 0 in Scouts.active:
                        ind = Scouts.active.index(0)
                        Scouts.send(ind)
                    else:
                        REL_COORDS = show_modal(title='Error!', text=f"You not have enough coin!", color=(100, 0, 0))

            else:
                test.toggle_bg((255,255,255))

            

            for i in range(len(Scouts.active)):

                if Scouts.active[i] == 1:
                    if Scouts.death_time[i]>0 and Scouts.time_taken[i] < Scouts.timetofind:
                        Scouts.death_time[i]-= 1
                        Scouts.time_taken[i]+= 1
                    elif Scouts.death_time[i] <=0:
                        print("DIE")
                        Scouts.die(i)
                    elif Scouts.time_taken[i] >= Scouts.timetofind:
                        print("FOUND")
                        Scouts.reveal(i, (0,0))

            
            if test.hovered:
                test.toggle_bg((0,100,0))

                if mouse_down:
                    test.toggle_bg((255,255,255))
                    game.screen = 0
                    return
                    
            else:
                test.toggle_bg((255,255,255))
        
        else:
            row, col = pygame.mouse.get_pos()

            if REL_COORDS[0] <= row <= REL_COORDS[0] + 30 and REL_COORDS[1] <= col <= REL_COORDS[1] + 30:
                if mouse_down:
                    modal_showing = False

        pygame.display.update()
        pygame.time.Clock().tick(60)
        
