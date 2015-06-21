from Vector import *

class Control():
    drone = None
    
    
    def __init__(self, drone):
        self.drone = drone
        self.error = 0
        self.errorPrev = 0
        
        self.derror = 0        
        self.errorSum = 0
        
        self.program = ""
        self.params = []
        self.switch = 0
        
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
        self.error = 0
        self.errorPrev = 0        
        self.derror = 0        
        self.errorSum = 0
        self.program = None
        
    def goto(self, coordinates):
        if coordinates != []:
            self.stay(coordinates[0])
            
            if abs(self.error) < 2 and abs(self.derror) < 2 and abs(self.drone.speed) < 2:
                self.resetControl()
                coordinates.pop(0)                
                self.load(self.goto, coordinates)
                self.setSwitch(1)
        """        
        else:
            self.load(self.stay, self.drone.height)
            self.setSwitch(1)
        """
    def reset(self):
        self.drone.setRotorSpeed(0)
        self.drone.height = 0.0
        self.drone.speed = 0.0
        
    def stay(self, place):
        #parameters of the controller
        p1 = 0.7
        p2 = 2
        p3 = 0.2
        
        self.errorPrev = self.error
        self.error = place - self.drone.height
        
        # derivator and integrator
        self.errorSum += self.error * 0.02
        self.derror = (self.error - self.errorPrev) / 0.02
        
        # linear controller
        self.drone.setRotorSpeed(p1 * self.error + p2 * self.derror + p3 * self.errorSum)
        
        # minel kozelebb kerulok, annal kevesebbet nyomok ra
    
    def onBtnUp(self):        
        self.drone.setRotorSpeed( Vector(self.drone.rotorspeed.coords[0], self.drone.rotorspeed.coords[1]+1))

    def onBtnDown(self):
        self.drone.setRotorSpeed( Vector(self.drone.rotorspeed.coords[0], self.drone.rotorspeed.coords[1]-1))
        
    def onBtnLeft(self):
        self.drone.setRotorSpeed( Vector(self.drone.rotorspeed.coords[0]-1, self.drone.rotorspeed.coords[1]))
        
    def onBtnRight(self):
        self.drone.setRotorSpeed( Vector(self.drone.rotorspeed.coords[0]+1, self.drone.rotorspeed.coords[1]))