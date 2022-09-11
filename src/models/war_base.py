from ..utils.load_utils import load_png
class WarBase():

    def __init__(self,type,level):
        self.level = level
        self.health = 10000 + (level*50)
        self.type = type # 0 is good, 1 is bad
        self.image, self.image_rect = load_png("war_base_good_base.png")  if type == 0 else load_png("war_base_bad_base.png")
    
    def draw(self, surface):
        surface.blit()
