from random import random
from Vector import *
from Drone import *
from Control import *
from pip.exceptions import BestVersionAlreadyInstalled


"""
max eltereses okossag
eloszor elerem az celt es az utana levo max(cel-pos) ertekre minimalizalok
"""


def gen():
    """generating random vector with coords 0-2"""
    return (Vector(random()*2+0.5, random()*2, random()*0.5)).coords 

TARGET = Vector(0,50)

def loop(best):
    agen = gen()
    control.resetControl()
    control.setP(agen)
    control.load(control.stay, TARGET)
    control.run()
    drone.refreshPos()
    
    
    droneRoute = []
    time = 0
    errorAbs = 111100
    touched = 0
    errorMax = 0
        
    while time < 800:
        if touched == 0:
            if (drone.pos - TARGET).len() < 0.5:
                touched = 1
        if touched == 1:
            if errorMax < control.error.len():
                errorMax = control.error.len()
        droneRoute.append(drone.pos.get())
        control.run()
        drone.refreshPos()
        #errorAbs += control.error.len() * drone.dt
        time += 1

    #if errorAbs < best[0]:
    #    best = [errorAbs, agen]
    #    print best
    #    return best
    #else:
    #    return best
    if errorMax < best[0]:
        best = [errorMax, agen]
        print best
        return best
    else:
        return best


drone = Drone(0.02)
control = Control(drone)

droneRoute = []
best = [1000000000, [0,0,0]]

for a in range(3000):    
    best = loop(best)
