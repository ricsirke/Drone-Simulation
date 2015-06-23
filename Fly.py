"""
[0.715036894231266, 0.4584803275416627, 0.03]
[0.6436009871488448, 0.6872072721886775, 0.05761033562424367]
[1.2061366432908034, 1.9170533843531075, 0.3607981810620108]

[2.2757878997777423, 1.7802098502025374, 0.15680047465820263]
[1.341896591615919, 1.7278910600594943, 0.41981330345561163]

[1.4911202040685452, 1.8362011995517473, 0.47215317780529964]


max norma
[0.6453539547210074, 1.3817991909818224, 0.03797045123404019]
[0.6453539547210074, 1.3817991909818224, 0.08597045123404019]  <- eddigi legjobb
[1.2265485343557876, 1.9855714793925145, 0.120788504112233]
#################################


[16.095992229752056, [1.9969525844055631, 1.8381537599239324, 0.14317915448451723]]
[4.381782581030109, [2.007821556163127, 0.27615086577017367, 0.44609716664311955]]
[0, [1.2265485343557876, 1.9855714793925145, 0.033788504112233]]

"""

from Vector import *
from Drone import *
from Control import *

drone = Drone(0.05)
control = Control(drone)
control.load(control.stay, Vector( 0,50))
control.run()
drone.refreshPos()
control.setP([1.2265485343557876, 1.9855714793925145, 0.120788504112233])

droneRoute = []
time = 0

while (abs(control.error.len()) > 1 or abs(control.derror.len()) > 1 or abs(drone.speed.len()) > 1) and time < 2000:
    """while program is not empty -> convergence"""
    droneRoute.append(drone.pos.get())
    control.run()
    drone.refreshPos()
    time += 1
    
import matplotlib.pyplot as plt
x_ax = []
y_ax = []

for i in range(len(droneRoute)):
    x_ax.append(i)
    y_ax.append(droneRoute[i][1])
    
plt.plot(x_ax, y_ax)
plt.show()