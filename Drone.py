from Vector import *

class Drone():

    def __init__(self, dt):
        self.dt = dt
        self.rotorspeed = Vector(0.0, 0.0)
        self.pos = Vector(0,0)
        self.speed = Vector(0.0,0.0)
        self.acc = Vector(0.0, 0.0)
        
        self.posPrev = Vector(0.0, 0.0)
        self.speedPrev = Vector(0.0, 0.0)
        
        self.control = None
    
    def setRotorSpeed(self, value):
        if value.x < 0:
            self.rotorspeed.x = 0
        elif value.x > 50:
            self.rotorspeed.x = 50
        else:
            self.rotorspeed.x = value.x
            
        if value.y < -50:
            self.rotorspeed.y = -50
        elif value.y > 50:
            self.rotorspeed.y = 50
        else:
            self.rotorspeed.y = value.y
            
    
    def setControl(self, control):
        self.control = control

    def refreshHeight(self):
        newpos = self.calc()
        self.posPrev = self.pos
        self.pos = newpos
        #not here
        self.speedPrev = self.speed
        self.speed = (self.pos - self.posPrev)/self.dt
        self.acc = (self.speed - self.speedPrev) / self.dt

    def calc(self):
        if self.pos.get() == (0,0) and self.rotorspeed.get() == (0,0):
            return self.pos
        else:
            m = 1.0
            g = 10.0
            dt = self.dt  #???
            newy = (self.rotorspeed.get()[1]-m*g) * dt**2 / m + 2 * self.pos.get()[1] - self.posPrev.get()[1]
            newx = (self.rotorspeed.get()[0]) * dt**2 / m + 2 * self.pos.get()[0] - self.posPrev.get()[0]

            if newy < 0:
                return Vector(self.rotorspeed.x, 0)
            elif newx < 0:
                return Vector(0, self.rotorspeed.y)
            elif newy > 500:
                return Vector(self.rotorspeed.x, 500)
            elif newx > 1000:
                return Vector(1000, self.rotorspeed.y)
            else:
                return Vector(newx,newy)
