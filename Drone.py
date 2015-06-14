class Drone():
    rotorspeed = 0
    height=0.0
    
    speed = 0.0    
    acc = 0.0
    
    heightPrev=0.0
    speedPrev = 0.0
    
    control = None
    
    def setRotorSpeed(self, value):
        if value > 100:
            self.rotorspeed = 100
        elif value < 0:
            self.rotorspeed = 0
        else:
            self.rotorspeed = value
    
    def setControl(self, control):
        self.control = control

    def refreshHeight(self):
        newheight = self.calc()
        self.heightPrev = self.height
        self.height = newheight
        #not here
        self.speedPrev = self.speed
        self.speed = (self.height - self.heightPrev)/(0.02)
        self.acc = (self.speed - self.speedPrev)/0.02

    def calc(self):
        if self.height == 0 and self.rotorspeed == 0:
            return 0
        else:
            m = 1.0
            g = 10.0
            F = self.rotorspeed
            Fall = F - m*g
            dt = 0.02  #???
            newheight = Fall * dt**2 / m + 2 * self.height - self.heightPrev

            if newheight < 0:
                return 0
            else:
                return newheight