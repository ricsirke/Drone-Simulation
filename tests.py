"""from Tkinter import Tk, Button
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

# plotting function: clear current, plot & redraw
def plot(x, y):
    plt.clf()    
    plt.plot(x,y)    
    # just plt.draw() won't do it here, strangely
    plt.gcf().canvas.draw()

# just to see the plot change
plotShift = 0
def main():
    global plotShift

    x = np.arange(0.0,3.0,0.01)
    y = np.sin(2*np.pi*x + plotShift)
    plot(x, y)

    plotShift += 1

# GUI
root = Tk()

draw_button = Button(root, text="Plot!", command = main)
draw_button.grid(row=0, column=0)

# init figure
fig = plt.figure()
canvas = Tk.Canvas(fig, master=root)
canvas.get_tk_widget().grid(row=0,column=1)

root.mainloop()"""





from Vector import *
a = Vector(2,1,2)
b = Vector(3,2,3)

c = a + b

print a.get()
print "b"
print b.get()
print "c"
print  c.get()