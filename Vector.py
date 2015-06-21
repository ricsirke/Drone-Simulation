class Vector():
    def __init__(self, *args):
        # Vector(2,3,4,3,2)
        self.coords = []
        
        for arg in args:
            self.coords.append(arg)      
        
    def set(self, *args):
        if len(self.coords) != len(args):
            print 'Error in Vector: set method, different dimensions'
        else:
            self.coords = args
        
    def get(self):
        return self.coords
    
    def __add__(self, b):
        return Vector(*[self.coords[i]  +b.coords[i] for i in range(len(self.coords))])
        
    def __sub__(self, b):
        return Vector(*[self.coords[i] - b.coords[i] for i in range(len(self.coords))])
    
    def __div__ (self, c):
        if isinstance(c, (long, int, float)):
            return Vector(*[self.coords[i] / c for i in range(len(self.coords))])
        else:
            print "Error in Vector - div: second arg is not i can div with"
        
    def __mul__ (self, c):
        if isinstance(c, (long, int, float)):
            return Vector(*[self.coords[i] * c for i in range(len(self.coords))])
        else:
            print "Error in Vector - div: second arg is not i can multiply with"
        