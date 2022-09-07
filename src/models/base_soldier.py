# import pygame

# class BaseSoldier:
#     def __init__(self):
#         self.X = 100
#         self.Y = 80
#         self.velocityY = 10
 
#     def on_init(self):
#         pygame.init()

#     def on_event(self, event):
#         if event.type == pygame.QUIT:
#             self._running = False
        
#     def on_loop(self):
#         pass

#     def on_render(self):
#         self._display.fill((200,200,200))

#     def on_cleanup(self):
#         pygame.quit()
 
#     def on_execute(self):
#         if self.on_init() == False:
#             self._running = False
 
#         while( self._running ):
#             for event in pygame.event.get():
#                 self.on_event(event)
#             self.on_loop()
#             self.on_render()
        
#         self.on_cleanup()