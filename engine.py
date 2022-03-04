class Engine:
    def __init__(self):
        self.gear=0
        self.rpm=0

    def modify_rpm(self, value):
        self.rpm += value

    def modify_gear(self, value):
        self.gear += value

        if self.gear > 5:
            self.gear=5

        if self.gear < -1:
            self.gear=-1

    def get_speed(self):
        if self.gear >= 0:
            speed = (self.rpm*self.gear/5)/10

        elif self.rpm > 0:
            speed = -10

        else:
            speed=0
        
        return speed

    def __str__(self):
        speed=self.get_speed()

        status=str(self.rpm) + ' rpm ' + str(self.gear) + ' gear ' + str(speed) + ' km/h'

        return status 