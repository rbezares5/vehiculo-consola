class Light:
    def __init__(self,env):
        self.activated=False
        self.lum=env

    def activate(self):
        self.activated=True
 
    def deactivate(self):
        self.activated=False
 
    def get_activated(self):
        return self.activated

    def update(self):
        if self.lum.get_lum() <= 40:
            self.activated=True
        else:
            self.activated=False

    def __str__(self):
        if self.activated:
            status = 'L'
        else:
            status = ' '
        return status