# 해양학전공 전상규

class Comx:                  
    def __init__(self, x, y):
        self.real = x
        self.imag = y
    
    def __add__(self, other):
        return Comx(self.real + other.real , self.imag + other.real)

    def __sub__(self, other):
        return Comx(self.real - other.real , self.imag - other.real)
    
    def __mul__(self, other):
        return Comx(self.real * other.real - self.imag * other.imag,
                    self.real * other.imag + self.imag * other.real)
    
    def __truediv__(self, other):
        return Comx((self.real * other.real + self.imag * other.imag) / (other.real**2 + other.imag**2),
                    (self.imag * other.real - self.real * other.imag) / (other.real**2 + other.imag**2))
    def __str__(self):
        return "{} + {}i".format(self.real, self.imag)
    
a = Comx(1, 2)
b = Comx(2, 3)

c = a + b
print(c)
d = a - b
print(d)
e = a * b
print(e)
f = a / b
print(f)