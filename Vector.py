class Vector():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def set(self,x,y):
        self.x = x
        self.y = y
        
    def get(self):
        return (self.x,self.y)
    
    def __add__(self, b):
        return Vector(self.x+b.x, self.y+b.y)
        
    def __sub__(self, b):
        return Vector(self.x - b.x, self.y - b.y)
    
    def __div__ (self, c):
        if isinstance(c, (long, int, float)):
            return Vector(self.x / c, self.y / c)
        
    def __mul__ (self, c):
        if isinstance(c, (long, int, float)):
            return Vector(self.x * c, self.y * c)
        
        