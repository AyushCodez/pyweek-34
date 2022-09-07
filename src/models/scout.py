class Scout():
    
    def __init__(self,home_coords):
        self.home_coords = home_coords
        self.active = []
        self.loc = []
        self.num = 0

    def create(self,number = 1):
        for i in range(number):
            self.active.append(0)
            self.loc.append(self.home_coords) #Home coords
        self.num+=number

    def send(self, index, coords: tuple):
        #TODO: Animate scout moving from one place to another
        if not(self.active[index]):
            self.loc[index] = coords[:]
            self.active[index] = 1

    def reveal(self,index):
        def remove_clouds(x,y):
            # TODO: reveal location
            pass
        remove_clouds(self.loc[index][0],self.loc[index][1])
        self.loc[index] = self.home_coords # Home coords
        self.active[index] = 0

    def die(self,index):
        self.num-=1
        self.loc.pop(index)
        self.active.pop(index)


