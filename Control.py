from Vector import *

class Control():
    drone = None
    
    
    def __init__(self, drone):
        self.drone = drone
        self.error = Vector(0,0)
        self.errorPrev = Vector(0,0)
        
        self.derror = Vector(0,0)
        self.errorSum = Vector(0,0)
        
        self.program = ""
        self.params = []
        self.switch = 0
        
        self.p = [1.920992106546498, 1.4674037935865036, 1.2306011558472907]
        
        drone.setControl(self)
        
    def setP(self, newP):
        self.p = newP
        
    def run(self):
        self.program(self.params)
    
    def load(self, program, params):
        self.program = program
        self.params = params
        
    def setSwitch(self, state):
        if state == 0:
            self.switch = 0
        elif state == 1:
            self.switch = 1
        else:
            print "invalid switch state"
            
    def resetControl(self):
        self.switch = 0
        self.error = Vector(0,0)
        self.errorPrev = Vector(0,0)        
        self.derror = Vector(0,0)        
        self.errorSum = Vector(0,0)
        self.program = None
        
    def goto(self, coordinates):
        if coordinates != []:
            self.stay(coordinates[0])
            
            if abs(self.error.len()) < 2 and abs(self.derror.len()) < 2 and abs(self.drone.speed.len()) < 2:
                self.resetControl()
                coordinates.pop(0)                
                self.load(self.goto, coordinates)
                self.setSwitch(1)
      
        else:
            self.resetControl()
            self.load(self.stay, self.drone.pos)
            self.setSwitch(1)

    def reset(self):
        self.drone.rotorspeed.set(0,0)
        self.drone.height.set(0,0)
        self.drone.speed.set(0,0)
        
    def stay(self, place):        
        self.errorPrev = self.error
        self.error = place - self.drone.pos        
        # derivator and integrator
        self.errorSum += self.error * self.drone.dt
        self.derror = (self.error - self.errorPrev) / self.drone.dt        
        # linear controller
        self.drone.setRotorSpeed(self.error * self.p[0] + self.derror * self.p[1] + self.errorSum * self.p[2])
        
        # minel kozelebb kerulok, annal kevesebbet nyomok ra
    
    def onBtnUp(self):        
        self.drone.setRotorSpeed( Vector(self.drone.rotorspeed.coords[0], self.drone.rotorspeed.coords[1]+1))

    def onBtnDown(self):
        self.drone.setRotorSpeed( Vector(self.drone.rotorspeed.coords[0], self.drone.rotorspeed.coords[1]-1))
        
    def onBtnLeft(self):
        self.drone.setRotorSpeed( Vector(self.drone.rotorspeed.coords[0]-1, self.drone.rotorspeed.coords[1]))
        
    def onBtnRight(self):
        self.drone.setRotorSpeed( Vector(self.drone.rotorspeed.coords[0]+1, self.drone.rotorspeed.coords[1]))