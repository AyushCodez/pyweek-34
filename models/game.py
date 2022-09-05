import pygame
import constants

class Game:
    def __init__(self):
        self._running = True
        self._display = None
        self.size = (self.width, self.height) = (constants.W, constants.H)
        # self.icon = pygame.image.load(os.path.join(""))
 
    def on_init(self):
        pygame.init()
        self._display = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        
    def on_loop(self):
        pass

    def on_render(self):
        self._display.fill((200,200,200))

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        
        self.on_cleanup()