from Simulator import *

dt = 0.02
app = Simulator(dt)
app.after( int(1000*dt), app.simLoop )
app.mainloop()