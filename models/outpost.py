class Outpost():

    def __init__(self,level):
        self.level = level
        self.troops = []
        self.deployed_troops = []
        self.dps = 50 + self.level*10

    def build(self):
        # Put on screen
        pass

    def deploy(self,troop):
        if troop in self.troops:
            self.troops.remove(troop)
            self.deployed_troops.append(troop)
            #send out troop
        elif troop in self.deployed_troops:
            print("Wait some time")
            pass
    
    def ready_troop(self,troop):
        self.troops.append(troop)
        self.deployed_troops.remove(troop)

    def destroy(self):
        #when outpost break
        pass


    