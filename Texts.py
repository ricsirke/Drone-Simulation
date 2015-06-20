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
        self.rotorSpeed.config(text=self.format % (self.drone.rotorspeed.x, self.drone.rotorspeed.y))
        self.pos.config(text=self.format % (self.drone.pos.x, self.drone.pos.y))
        self.speed.config(text=self.format % (self.drone.speed.x, self.drone.speed.y))
        self.acc.config(text=self.format % (self.drone.acc.x, self.drone.acc.y))
        
        """
        self.height.config(text="%0.2f" % (self.drone.height))
        
        self.acc.config(text="%0.2f" % self.drone.acc)
        self.error.config(text="%0.2f" % self.drone.control.error)
        self.derror.config(text="%0.2f" % self.drone.control.derror)
        self.errorSum.config(text="%0.2f" % self.drone.control.errorSum)
        
        if self.drone.control.program == self.drone.control.stay:
            self.runProgram = "stay"
        elif self.drone.control.program == self.drone.control.goto:
            self.runProgram = "goto"
        else:
            self.runProgram = ""
        self.switch.config(text=self.runProgram)
        """
    
        