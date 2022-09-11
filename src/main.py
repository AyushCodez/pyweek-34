# Copyright (c) 2021 Ayush Gupta, Pranjal Rastogi
# -----------------------------------------------
# main.py
#
# Main game code
# -----------------------------------------------

if __name__ == "__main__":
    import sys
    print("Do not run this file!\nRun run_game.py instead!\n")
    sys.exit()


import pygame
from .utils.constants import W, H
from .screens import home_screen, map_screen, war_screen

class Game:
    def __init__(self):
        self.running = True
        self.display_surface = None
        self.size = (self.width, self.height) = (W, H)
        self.screen = None
        self.caption = None
        self.icon = None # TODO: implement


    def on_init(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.running = True
        self.caption = "Empyrean: The War for Freedom"
        pygame.display.set_caption(self.caption)
        self.screen = 0

 
    def execute(self):
        self.on_init()
        dic = dict()
        dic['metal'] = 100
        dic['scouts'] = 2
        dic['discovered_areas'] = []
        dic['base_locations'] = []
        dic['destroyed_bases'] = []
        dic['last_beaten_level'] = 0
        with open("data/data1.txt",'w') as f:
            f.write(str(dic))   

        while( self.running ):

            for event in pygame.event.get():
                # event handling
                if event.type == pygame.QUIT:
                    self.running = False
            
            # loop
            if self.screen == 0:
                home_screen.run_home_screen(self)
            elif self.screen == 1:
                 
                map_screen.run_map_screen(self)
            elif self.screen == 2:
                war_screen.run_war_screen(self)

            pygame.display.update()
        
        # CLEANUP
        pygame.quit()

        
def main():
    game = Game()
    game.execute()
    