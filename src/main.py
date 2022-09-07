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
from .constants import W, H
from .screens import home_screen

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
        self.caption = "The Red Planet"
        pygame.display.set_caption(self.caption)
        self.screen = 0

 
    def execute(self):
        self.on_init()

        while( self.running ):
            for event in pygame.event.get():
                # event handling
                if event.type == pygame.QUIT:
                    self.running = False
            
            # loop
            if self.screen == 0:
                home_screen.run_home_screen(self)
            elif self.screen == 1:
                print("screen 1")

            pygame.display.update()
        
        # CLEANUP
        pygame.quit()

        
def main():
    game = Game()
    game.execute()
    