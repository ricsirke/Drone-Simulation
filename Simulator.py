import Tkinter as tk

from Control import *
from Drone import *
from InfoPanel import *

class Simulator(tk.Tk):
    def __init__(self):
        self.WIDTH = 500.0
        self.HEIGHT = 500.0
        self.time = 0.0
                
        tk.Tk.__init__( self )
        
        self.drone = Drone()
        self.control = Control(self.drone)
        self.drone.setControl(self.control)     

        self.infos = InfoPanel(self, self.drone)
        self.infos.setUiTexts()
        self.infos.pack()

        screen = tk.Frame(self)
        screen.pack()
        
        screen.focus_set()  
                
        self.canvas = tk.Canvas(screen, width=self.WIDTH, height=self.HEIGHT)
        self.canvas.pack()       
                
        self.rotorspeed_ui = self.canvas.create_rectangle(25, self.HEIGHT-25, 50, self.HEIGHT-25, fill="blue")
             
        self.drone_ui = self.canvas.create_oval(150, self.HEIGHT, 160, self.HEIGHT-10, fill = "red")
               

        def onBtnUpHand(e):
            self.control.onBtnUp()

        def onBtnDownHand(e):
            self.control.onBtnDown()

        def onBtnAHand(e):          
            if self.control.switch == 0:
                self.control.setSwitch(1)
                self.control.load(self.control.stay, [self.drone.height])
                
        def onBtnRHand(e):
            self.control.reset()
            
        def onBtnGHand(e):                        
            if self.control.switch == 0:
                self.control.setSwitch(1)
                self.control.load(self.control.goto, [100, 50, 200])
                
        def onBtnOHand(e):
            self.control.resetControl()

        screen.bind("<Up>", onBtnUpHand)
        screen.bind("<Down>", onBtnDownHand)
        screen.bind("<a>", onBtnAHand)
        screen.bind("<r>", onBtnRHand)
        screen.bind("<g>", onBtnGHand)
        screen.bind("<o>", onBtnOHand)

    def simLoop(self):
        self.canvas.coords(self.rotorspeed_ui, 25, 175, 50, 175-self.drone.rotorspeed)
        self.drone.refreshHeight()
        if self.control.switch == 1:
            self.control.run()
            
        self.canvas.coords(self.drone_ui, 150, self.HEIGHT-self.drone.height, 160, self.HEIGHT-10-self.drone.height)

        self.infos.setUiTexts()
        
        self.time += 0.02
        
        self.after(20, self.simLoop)