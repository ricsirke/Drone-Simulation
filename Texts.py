import Tkinter as tk
from InfoPanel import *

class Texts():
    def __init__(self,parent):
        self.drone = parent.drone
        
        self.textsFrame = tk.Frame(parent.panel)
        self.textsFrame.pack()
        
        self.rotorSpeedText = tk.StringVar()
        self.rotorSpeed = tk.Label(self.textsFrame, text=self.rotorSpeedText)
        self.rotorSpeed.pack()
        
        self.posText = tk.StringVar()
        self.pos = tk.Label(self.textsFrame, text=self.posText)
        self.pos.pack()
        
        self.speedText = tk.StringVar()
        self.speed = tk.Label(self.textsFrame, text=self.speedText)
        self.speed.pack()
        
        self.accText = tk.StringVar()
        self.acc = tk.Label(self.textsFrame, text=self.accText)
        self.acc.pack()
        
        self.errorText = tk.StringVar()
        self.error = tk.Label(self.textsFrame, text=self.errorText)
        self.error.pack()
        
        self.derrorText = tk.StringVar()
        self.derror = tk.Label(self.textsFrame, text=self.derrorText)
        self.derror.pack()
        
        self.errorSumText = tk.StringVar()
        self.errorSum = tk.Label(self.textsFrame, text=self.errorSumText)
        self.errorSum.pack()
        
        self.switchText = tk.StringVar()
        self.switch = tk.Label(self.textsFrame, text=self.switchText)
        self.switch.pack()
        
        self.runProgram = ""
        
        self.format = "%0.2f , %0.2f"
    
    def setUiTexts(self):
        self.rotorSpeed.config(text=self.format % (self.drone.rotorspeed.coords[0], self.drone.rotorspeed.coords[1]))
        self.pos.config(text=self.format % (self.drone.pos.coords[0], self.drone.pos.coords[1]))
        self.speed.config(text=self.format % (self.drone.speed.coords[0], self.drone.speed.coords[1]))
        self.acc.config(text=self.format % (self.drone.acc.coords[0], self.drone.acc.coords[1]))
        self.error.config(text=self.format % (self.drone.control.error.coords[0], self.drone.control.error.coords[1]))
        self.derror.config(text=self.format % (self.drone.control.derror.coords[0], self.drone.control.derror.coords[1]))
        self.errorSum.config(text=self.format % (self.drone.control.errorSum.coords[0], self.drone.control.errorSum.coords[1]))
             
        if self.drone.control.program == self.drone.control.stay:
            self.runProgram = "stay"
        elif self.drone.control.program == self.drone.control.goto:
            self.runProgram = "goto"
        else:
            self.runProgram = ""
        self.switch.config(text=self.runProgram)
    
        