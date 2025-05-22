class Vector:
    """a vector class"""
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        if self.z == 0: 
            return f"Vector({self.x}, {self.y})"
        else:
            return f"Vector({self.x}, {self.y}, {self.z})"
    def __add__(self, other): 
        return f"Vector({self.x + other.x}, {self.y + other.y}, {self.z + other.z})"
    def dot(self, other): 
        if self.z or other.z == 0: 
            return f"Vector({self.x * other.x}, {self.y * other.y})"
        else:
            return f"Vector({self.x * other.x}, {self.y * other.y}, {self.z * other.z})"
    def vector_form(self): 
        return f"{self.x}i+{self.y}j+{self.z}k"
    def value(self): 
        return ((self.x ** 2) + (self.y ** 2) + (self.z ** 2)) ** 0.5
    def scaler_mult(self, scaler): 
        if self.z == 0: 
            return f"Vector({self.x * scaler}, {self.y * scaler})"
        else:
            return f"Vector({self.x * scaler}, {self.y * scaler}, {self.z * scaler})"
    def x(self): 
        return self.x
    def y(self): 
        return self.y
    def z(self): 
        return self.z