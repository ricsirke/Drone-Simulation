# it will provide a tk.Frame -> append it to tk root

import Tkinter as tk
from __builtin__ import str

class InfoPanel():
        
    def __init__(self, parent, drone):
        self.drone = drone
        self.panel = tk.Frame(parent)
        
        self.rotorSpeedText = tk.StringVar()
        self.rotorSpeed = tk.Label(self.panel, text=self.rotorSpeedText)
        self.rotorSpeed.pack()
        
        self.heightText = tk.StringVar()
        self.height = tk.Label(self.panel, text=self.heightText)
        self.height.pack()
        
        self.speedText = tk.StringVar()
        self.speed = tk.Label(self.panel, text=self.speedText)
        self.speed.pack()
        
        self.accText = tk.StringVar()
        self.acc = tk.Label(self.panel, text=self.accText)
        self.acc.pack()
        
        self.timeText = tk.StringVar()
        self.time = tk.Label(self.panel, text=self.timeText)
        self.time.pack()
        
        self.errorText = tk.StringVar()
        self.error = tk.Label(self.panel, text=self.errorText)
        self.error.pack()
        
        self.derrorText = tk.StringVar()
        self.derror = tk.Label(self.panel, text=self.derrorText)
        self.derror.pack()
        
        self.switchText = tk.StringVar()
        self.switch = tk.Label(self.panel, text=self.switchText)
        self.switch.pack()
        
        self.runProgram = ""
    
    def setUiTexts(self):
        self.rotorSpeed.config(text=self.drone.rotorspeed)
        self.height.config(text=self.drone.height/500)
        self.speed.config(text=self.drone.speed/500)
        self.acc.config(text=self.drone.acc)
        self.error.config(text=self.drone.control.error)
        self.derror.config(text=self.drone.control.derror)
        if self.drone.control.program == self.drone.control.stay:
            self.runProgram = "stay"
        elif self.drone.control.program == self.drone.control.goto:
            self.runProgram = "goto"
        else:
            self.runProgram = ""
        self.switch.config(text=self.runProgram)
        
    def pack(self):
        self.panel.pack()
