class Scout():

    def __init__(self):
        self.active = False

    def send(self, to_x, to_y):
        if not(self.active):
            self.to_x = to_x
            self.to_y = to_y
            self.active = True

    def reveal(self):
        def remove_clouds(x,y):
            # TODO: reveal location
            pass
        remove_clouds(self.to_x,self.to_y)


