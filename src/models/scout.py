import random

class Scout():
    
    def __init__(self):
        self.active = []
        self.num = 0
        self.timetofind = 60*(5) # frames
        self.death_time = []
        self.time_taken = []

    def create(self,number = 1):
        for i in range(number):
            self.active.append(0)
            self.death_time.append(random.randint(self.timetofind//2,int(self.timetofind*1.5)))
            self.time_taken.append(0)
        self.num+=number

    def send(self, index):
        #TODO: Animate scout moving from one place to another
        if not(self.active[index]):
            self.active[index] = 1

    def reveal(self,index,loc):
        def remove_clouds(loc):
            # TODO: reveal location
            pass
        remove_clouds(loc)
        self.active[index] = 0
        self.death_time[index] = (random.randint(self.timetofind//2,int(self.timetofind*1.5)))
        self.time_taken[index] = 0

    def die(self,index):
        self.num-=1
        self.active[index] = 'X'
        self.death_time[index] = 'X'
        self.time_taken[index] = 'X'


