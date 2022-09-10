import random
import pygame

from src.utils.load_utils import load_png
from ..widgets import buttons
from src.utils.constants import W,H
from src.models.scout import Scout
import pygame.freetype

def run_map_screen(game):

    metal = 100
    metal_needed = 50
    mine_level = 1
    # game loop
    # Draw screen
    Scouts = Scout()
    Scouts.create(2)
    surface = game.display_surface
    modal_showing = False
    scout_sending = False
    x_btn = None

    scout,scout_size = load_png("scout.png")
    cloud,cloud_size = load_png("clouds.png")
    enemy_base, enemy_base_size = load_png("enemy_base.png")
    bg,bg_size = load_png("map_screen_bg.png")
    dust,dust_size = load_png("dust.png")
    dust = pygame.transform.scale(dust, (32,32))
    bg = pygame.transform.scale(bg, (800,600))
    l1 = [dust]*1200
    noise = 5
    l1_loc = [(20*(i%40) + random.randint(-noise,noise),20*(i//40)+ random.randint(-noise,noise)) for i in range(1200)]
    discovered_areas = []
    base_locations = []
    scout_death = False
    scout_notif_time = 0
    scout_notif = 0



    def show_modal(title, text, color, type=1):

        nonlocal modal_showing
        modal_showing = True

        
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

            surface.blit(bg,(0,0))
            
            
            for i in range(len(l1)):
                l1[i].set_alpha(80)
                for a in discovered_areas:
                    b = l1_loc[i]
                    if ((b[0]-a[0])**2 + (b[1]-a[1])**2)**1/2 <= 3600:
                        l1[i].set_alpha(0)
                
                a = l1_loc[i]
                if (380-a[0])**2/22500 + (280-a[1])**2/12000 >=1:
                    surface.blit(l1[i], a)

            for i in base_locations:
                surface.blit(enemy_base,i)
                loc = pygame.mouse.get_pos()
                if 0<loc[0]-i[0]<64 and 0<loc[1]-i[1]<64:
                    text = pygame.font.Font('freesansbold.ttf', 25).render('Battle!', True, (0,0,0))
                    surface.blit(text, (i[0],i[1]-25))
                    if mouse_down:
                        game.screen = 2
                        return

            test = buttons.TextButton(surface, (400,60), 100, 50, (0,0,0), (255,255,255), pygame.font.SysFont("arial", 20), "go back make map")
            create_scout = buttons.TextButton(surface, (0,570), 90, 20, (0,0,0), (255,255,255), pygame.font.SysFont("arial", 15), "Create Scout")
            send_scout = buttons.TextButton(surface, (100,570), 90, 20, (0,0,0), (255,255,255), pygame.font.SysFont("arial", 15), "Send Scout")
            mine_metal = buttons.TextButton(surface, (200,570), 90, 20, (0,0,0), (255,255,255), pygame.font.SysFont("arial", 15), "Mine Metal")
            
            text = pygame.font.Font('freesansbold.ttf', 15).render(f'Available Scouts: {Scouts.active.count(0)}/{Scouts.num}  ', True, (0,0,0))
            surface.blit(text, (0,0))
            text = pygame.font.Font('freesansbold.ttf', 15).render(f'Metal left: {metal}  ', True, (0,0,0))
            surface.blit(text, (0,15))

            if scout_sending:

                maj_sur = pygame.Surface((800,600))
                
                maj_sur.set_alpha(100)
                maj_sur.fill((0,0,0))
                loc = pygame.mouse.get_pos()
                a = loc 
                if (380-a[0])**2/40000 + (280-a[1])**2/25454 >1:
                    for i in discovered_areas:
                        if ((i[0]-a[0])**2 + (i[1]-a[1])**2)**1/2 <= 8100:
                            pygame.draw.circle(maj_sur, (100,0,0), loc, 60, 0)
                            break
                    else:
                        pygame.draw.circle(maj_sur, (0,100,0), loc, 60, 0)
                else:
                    pygame.draw.circle(maj_sur, (100,0,0), loc, 60, 0)
                surface.blit(maj_sur,(0,0))

                text = pygame.font.Font('freesansbold.ttf', 20).render(f'Click where you want to send scout', True, (255,255,255))
                surface.blit(text, (260,10))
                cancel = buttons.TextButton(surface, (700,570), 90, 20, (0,0,0), (255,255,255), pygame.font.SysFont("arial", 15), "Cancel")

                

                

                if mouse_down:
                    a = loc 
                    if (380-a[0])**2/40000 + (280-a[1])**2/25454 >1:
                        for i in discovered_areas:
                            if ((i[0]-a[0])**2 + (i[1]-a[1])**2)**1/2 <= 8100:
                                pass
                        else:
                            Scouts.send(loc = loc)
                            scout_sending = False
                    
                
                
                if cancel.hovered:
                    cancel.toggle_bg((0,100,0))

                    if mouse_down:
                        cancel.toggle_bg((255,255,255))
                        scout_sending = False

                      

            if create_scout.hovered and not(scout_sending):
                create_scout.toggle_bg((0,100,0))

                if mouse_down:
                    create_scout.toggle_bg((255,255,255))
                    if metal>=metal_needed:
                        Scouts.create()
                        metal-=metal_needed
                    else:
                        REL_COORDS = show_modal(title='Error!', text=f"You need {metal_needed} metal to make scout", color=(100, 0, 0))
                        
                    
            else:
                create_scout.toggle_bg((255,255,255))

            if send_scout.hovered and not(scout_sending):
                send_scout.toggle_bg((0,100,0))

                if mouse_down:
                    send_scout.toggle_bg((255,255,255))
                    if 0 in Scouts.active:
                        scout_sending = True
                    else:
                        REL_COORDS = show_modal(title='Error!', text=f"No scouts left!", color=(100, 0, 0))

            else:
                send_scout.toggle_bg((255,255,255))

            if mine_metal.hovered and not(scout_sending):#TODO: remove when game finalised
                mine_metal.toggle_bg((0,100,0))

                if mouse_down:
                    mine_metal.toggle_bg((255,255,255))
                    metal+=50
                    
            else:
                mine_metal.toggle_bg((255,255,255))

            

            

            
            if test.hovered:
                test.toggle_bg((0,100,0))

                if mouse_down:
                    test.toggle_bg((255,255,255))
                    game.screen = 0
                    return
                    
            else:
                test.toggle_bg((255,255,255))

            
                
                
        
        elif modal_showing:
            row, col = pygame.mouse.get_pos()

            if REL_COORDS[0] <= row <= REL_COORDS[0] + 30 and REL_COORDS[1] <= col <= REL_COORDS[1] + 30:
                if mouse_down:
                    modal_showing = False
        


        for i in range(len(Scouts.active)):

                if Scouts.active[i] == 1:
                    if Scouts.death_time[i]>0 and Scouts.time_taken[i] < Scouts.timetofind:
                        Scouts.death_time[i]-= 1
                        Scouts.time_taken[i]+= 1
                    elif Scouts.death_time[i] <=0:
                        scout_notif = 1
                        scout_notif_time = 0
                        Scouts.die(i)
                    elif Scouts.time_taken[i] >= Scouts.timetofind:
                        scout_notif = 2
                        scout_notif_time = 0
                        discovered_areas.append(Scouts.loc[i])
                        base_loc = (Scouts.loc[i][0] - random.randint(-30,60),Scouts.loc[i][1] - random.randint(-30,60))
                        while 0>base_loc[0] or base_loc[0]>(800-64) or 0>base_loc[1] or base_loc[1]>(600-64):
                            base_loc = (Scouts.loc[i][0] - random.randint(-30,60),Scouts.loc[i][1] - random.randint(-30,60))
                        base_locations.append(base_loc)
                        Scouts.reveal(i)

        if scout_notif_time<300:
            if scout_notif == 1:

                ft_font = pygame.freetype.SysFont('Times New Roman', 20)

                ft_font.render_to(surface, (300,570), 'Your scout died!', (0, 0, 0, (255-(scout_notif_time**2/903))))

                scout_notif_time+=1

            if scout_notif == 2:

                ft_font = pygame.freetype.SysFont('Times New Roman', 20)

                ft_font.render_to(surface, (300,570), 'Your scout discovered an enemy base!', (0, 0, 0, (255-(scout_notif_time**2/903))))

                scout_notif_time+=1
        else:
            scout_notif_time = 0
            scout_notif = 0

        pygame.display.update()
        pygame.time.Clock().tick(60)
        

