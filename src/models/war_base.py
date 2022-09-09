class WarBase():

    def __init__(self,type,level):
        self.level = level
        self.health = 10000 + (level*50)
        self.type
