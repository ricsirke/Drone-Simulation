# it will provide a tk.Frame -> append it to tk root

import Tkinter as tk
from Texts import *
from Plots import *

class InfoPanel():        
    def __init__(self, parent, drone):        
        self.drone = drone
        self.panel = tk.Frame(parent, width=300) 
        
        self.texts = Texts(self)
        self.plots = Plots()       
        
    def pack(self):
        self.panel.pack(side=tk.LEFT)
