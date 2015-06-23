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
        if value.coords[0] < -30:
            self.rotorspeed.coords[0] = -30
        elif value.coords[0] > 30:
            self.rotorspeed.coords[0] = 30
        else:
            self.rotorspeed.coords[0] = value.coords[0]
            
        if value.coords[1] < 0:
            self.rotorspeed.coords[1] = 0
        elif value.coords[1] > 30:
            self.rotorspeed.coords[1] = 30
        else:
            self.rotorspeed.coords[1] = value.coords[1]
            
    
    def setControl(self, control):
        self.control = control

    def refreshPos(self):
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
            """
             m*ddx = F
            """            
            Fall = self.rotorspeed + Vector(0, -m*g)
            
            newpos = Fall * dt**2 / m + self.pos * 2 - self.posPrev
            
            if newpos.coords[1] < 0:
                self.speed.set(0,0)
                return Vector(newpos.coords[0], 0)
            elif newpos.coords[0] < 0:
                self.speed.set(0,0)
                return Vector(0, newpos.coords[1])
            elif newpos.coords[1] > 500:
                self.speed.set(0,0)
                return Vector(newpos.coords[0], 500)
            elif newpos.coords[0] > 1000:
                self.speed.set(0,0)
                return Vector(1000, newpos.coords[1])
            else:
                return newpos
