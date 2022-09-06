class Scout():
    
    def __init__(self):
        self.active = []
        self.loc = []
        self.num = 0

    def create(self,number = 1):
        for i in range(number):
            self.active.append(0)
            self.loc.append((0,0)) #Home coords
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
        self.loc[index] = (0,0) # Home coords
        self.active[index] = 0

    def die(self,index):
        self.num-=1
        self.loc.pop(index)
        self.active.pop(index)

l1 = Scout()
l1.create(9)
print(l1.active,l1.loc)
l1.send(3,(5,4))
print(l1.active,l1.loc)
l1.send(8,(2,9))
print(l1.active,l1.loc)
l1.die(10)
print(l1.active,l1.loc)
