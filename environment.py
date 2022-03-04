class Environment:
    def __init__(self):
        self.lum=50

    def modify_lum(self, value):
        self.lum += value
        
        if self.lum < 0:
            self.lum = 0
        if self.lum > 100:
            self.lum = 100

    def set_lum(self, value):
        self.lum = value

        if self.lum < 0:
            self.lum = 0
        if self.lum > 100:
            self.lum = 100

    def get_lum(self):
        return self.lum