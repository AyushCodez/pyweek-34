import random

class Scout():
    
    def __init__(self):
        self.active = []
        self.num = 0
        self.timetofind = 30*(2) # frames
        self.death_time = []
        self.time_taken = []
        self.loc = []

    def create(self,number = 1):
        for i in range(number):
            self.active.append(0)
            self.death_time.append(random.randint(self.timetofind,int(self.timetofind*1.5)))#TODO lower beggining int when finalise
            self.time_taken.append(0)
            self.loc.append((0,0))
        self.num+=number

    def send(self,loc):
        ind = self.active.index(0)
        if not(self.active[ind]):
            self.active[ind] = 1
            self.loc[ind] = loc

    def reveal(self,index):
        self.active[index] = 0
        self.death_time[index] = (random.randint(self.timetofind//2,int(self.timetofind*1.5)))
        self.time_taken[index] = 0

    def die(self,index):
        self.num-=1
        self.active[index] = 'X'
        self.death_time[index] = 'X'
        self.time_taken[index] = 'X'


