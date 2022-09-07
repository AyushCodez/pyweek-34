class Troop:

    def __init__(self,level):
        self.dps = level*10
        self.health = level*100

    def take_damage(self,damage):
        self.health -= damage

    def die(self):
        #kill troop
        pass

class troop1(Troop):

    def attack(self):
        #attack animation
        pass

class troop2(Troop):

    def attack(self):
        #attack animation
        pass

class troop3(Troop):

    def attack(self):
        #attack animation
        pass

class troop4(Troop):

    def attack(self):
        #attack animation
        pass