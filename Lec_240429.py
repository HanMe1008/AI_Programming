# 2024/04/29 AI프로그래밍및실습 해양학전공

#
def add(a, b):
    return a + b

c = add(2, 3)
print(c)

#
def i_max(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c

print(i_max(5, 5, 3))

#
def i_max(a, b, c):
    max_value = a
    if b > max_value: max_value = b
    if c > max_value: max_value = c
    return max_value

print(i_max(3, 4, 5))

# 
def i_max(*nums):
    max_value = nums[0]
    for num in nums:
        if num > max_value:
            max_value = num
    return max_value

print(i_max(1, 2, 3, 4, 5, 6, 7))

#
class Human:
    def __init__(self, name, age, sex):
        self.__name = name
        self.__age = age
        self.__sex = sex
    
    def __str__(self):
        return "이름은 {}, 나이는 {}, 성별은 {}입니다.".format(self.__name, self.__age, self.__sex)
    
    def setinfo(self, name, age, sex):
        self.__name = name
        self.__age = age
        self.__sex = sex

    def __del__(self):
        print("{}의 죽음을 알리지마라.".format(self.__name))


noah = Human("영호", 28, "남자")
print(noah)

noah.setinfo("상규", 24, "남자")
print(noah)

del(noah)

# 팀프로젝트

# 복소변수
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



