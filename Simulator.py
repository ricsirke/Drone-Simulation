import Tkinter as tk

from Control import *
from Drone import *
from InfoPanel import *

class Simulator(tk.Tk):
    def __init__(self, dt):
        self.WIDTH = 1000.0
        self.HEIGHT = 500.0
        self.time = 0.0
        self.dt = dt
                
        tk.Tk.__init__( self )
        
        self.drone = Drone(self.dt)
        #self.drone2 = Drone(self.dt)
        self.control = Control(self.drone)
        #self.control2 = Control(self.drone2)
        self.drone.setControl(self.control)
        #self.drone2.setControl(self.control2)     

        screen = tk.Frame(self)
        screen.pack()
        
        self.canvas = tk.Canvas(screen, width=self.WIDTH, height=self.HEIGHT,borderwidth=10)
        self.canvas.grid(column=1, row=1)
        
        self.infos = InfoPanel(screen, self.drone)
        self.infos.panel.grid(column=2, row=1)
        #self.infos2 = InfoPanel(screen, self.drone2)
        #self.infos2.panel.grid(column=3, row=1)
       
        # to receive commands
        screen.focus_set()  
        
        self.drone_ui = self.canvas.create_oval(40, self.HEIGHT, 50, self.HEIGHT-10, fill = "red")
        #self.drone2_ui = self.canvas.create_oval(100, self.HEIGHT, 110, self.HEIGHT-10, fill = "blue")       

        def onBtnUpHand(e):
            self.control.onBtnUp()

        def onBtnDownHand(e):
            self.control.onBtnDown()
            
        def onBtnLeftHand(e):
            self.control.onBtnLeft()
            
        def onBtnRightHand(e):
            self.control.onBtnRight()

        def onBtnAHand(e):          
            if self.control.switch == 0:
                self.control.setSwitch(1)
                self.control.load(self.control.stay, self.drone.pos)
                
        def onBtnRHand(e):
            self.control.reset()
            
        def onBtnGHand(e):                        
            if self.control.switch == 0:
                self.control.setSwitch(1)
                self.control.load(self.control.goto, [Vector(0,50), Vector(30,100)])
                
        def onBtnOHand(e):
            self.control.resetControl()

        screen.bind("<Up>", onBtnUpHand)
        screen.bind("<Down>", onBtnDownHand)
        screen.bind("<Left>", onBtnLeftHand)
        screen.bind("<Right>", onBtnRightHand)
        screen.bind("<a>", onBtnAHand)
        screen.bind("<r>", onBtnRHand)
        screen.bind("<g>", onBtnGHand)
        screen.bind("<o>", onBtnOHand)

    def simLoop(self):        
        self.drone.refreshPos()
        #self.drone2.refreshHeight()
        if self.control.switch == 1:
            self.control.run()
            
        #self.control2.load(self.control2.goto, [self.drone.height])
        #self.control2.run()
            
        self.canvas.coords(self.drone_ui, self.drone.pos.coords[0]+40, self.HEIGHT-self.drone.pos.coords[1], self.drone.pos.coords[0]+50, self.HEIGHT-10-self.drone.pos.coords[1])
        #self.canvas.coords(self.drone2_ui, 100, self.HEIGHT-self.drone2.height, 110, self.HEIGHT-10-self.drone2.height)

        self.infos.texts.setUiTexts()
        #self.infos2.texts.setUiTexts()
        
        self.after(int(1000*self.dt), self.simLoop)