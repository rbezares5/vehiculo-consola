class Fuel:
    def __init__(self,engine):
        self.level = 1000
        self.engine = engine

    def update(self):
        self.level = self.level - abs(self.engine.get_speed()) * 0.01

    def __str__(self):
        status = 'fuel level ' + str(self.level)
        return status 
