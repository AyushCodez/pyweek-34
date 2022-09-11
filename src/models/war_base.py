from ..utils.load_utils import load_png
import pygame

class WarBase():

    def __init__(self,type,level):
        self.level = level
        self.health = 10000 + (level*50)
        self.type = type # 0 is good, 1 is bad
        self.image, self.image_rect = load_png("war_base_good_base.png")  if type == 0 else load_png("war_base_bad_base.png")
        self.image = pygame.transform.scale(self.image, (216,216))
    
    def draw(self, surface, pos):
        surface.blit(self.image, pos)
    
    def take_damage(self, dmg):
        self.health -= dmg
    

    

    
