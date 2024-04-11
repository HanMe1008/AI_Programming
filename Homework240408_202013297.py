# 해양학전공 전상규

# 9.1
a = 123

print(a.__add__(334))
print(a.__sub__(334))
print(a.__mul__(334))
print(a.__truediv__(3))

# 9.3
s = 'Hello World~'

# 사용 가능한 메소드
s.upper() 

# 사용 불가능한 메소드
# s.pop()
# s.sort()
# s.append()
# s.insert()
# s.remove()

# 9.5
a = 1; b = 1; c = 2; d = 3; e = 3

print("a와 b는 같은 객체인가?", a is b)
print("b와 c는 같은 객체인가?", b is c)
print("c와 d는 같은 객체인가?", c is d)
print("d와 e는 같은 객체인가?", d is e)

# 9.7
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return "이름은 {}이고, 나이는 {}살입니다.".format(self.name, self.age)

my_dog = Dog('Mango', 3)
print(my_dog)

# 9.9
class Counter:
    number = 0

    def __init__(self, number):
        self.__number = number
        if self.__number >= 100:
          self.__number = 0
        elif self.__number <= -1:
          self.__number = 0

    def reset(self):
        self.__number = 0
    
    def inc(self):
        self.__number += 1
        if self.__number >= 100:
            self.__number = 0
    
    def dec(self):
        self.__number -+ 1
        if self.__number <= -1:
            self.__number = 0
    
    def __str__(self):
        return "C({})".format(self.__number)
    
    def __add__(self, other):
        return Counter(self.__number + other.__number)
    def __sub__(self, other):
        return Counter(self.__number - other.__number)

c1 = Counter(10)
c2 = Counter(20)
c3 = c1 + c2
c4 = c1 - c2
print('c3 =', c3)
print('c4 =', c4)

# 9.11
class Student:
    def __init__(self, name, student_id):
        self.__name = name
        self.__student_id = student_id
        self.__korean_quiz = korean_quiz
        self.__math_quiz = math_quiz
        self.__science_quiz = science_quiz

    def __str__(self):
        return "이름 : {}, 학번 : {}\
        국어성적 : {}, 수학성적 : {}, 과학성적 : {}\
        합계 : {}, 평균 : {}".format(self.__name, self.__student_id, self.__korean_quiz, self.__math_quiz, self.__science_quiz, self.get_total_score(), self.get_avg_score())

    # 게터 설정
    def get_name(self):
        return self.__name
    def get_student_id(self):
        return self.__student_id
    def get_korean_quiz(self):
        return self.__korean_quiz
    def get_math_quiz(self):
        return self.__math_quiz
    def get_science_quiz(self):
        return self.__science_quiz
    def get_total_score(self):
        return self.__korean_quiz + self.__math_quiz + self.__science_quiz
    def get_avg_score(self):
        return self.get_total_score() / 3
    
    # 세터 설정
    def set_korean_quiz(self, value):
        self.__korean_quiz = value
    def set_math_quiz(self, value):
        self.__math_quiz = value
    def set_science_quiz(self, value):
        self.__science_quiz = value

name = input('학생의 이름을 입력하세요 : ')
student_id = input('학생의 학번을 입력하세요 : ')

student = Student(name, student_id)

korean_quiz = int(input('학생의 국어 성적을 입력하세요 : '))
math_quiz = int(input('학생의 수학 성적을 입력하세요 : '))
science_quiz = int(input('학생의 과학 성적을 입력하세요 : '))

student.set_korean_quiz(korean_quiz)
student.set_math_quiz(math_quiz)
student.set_science_quiz(science_quiz)

print(student)

# 9.13 (문제에선 x, y가 좌측 상단 기준인데 실수로 좌측 하단으로 코드 작성함)
class Rectangle:
    def __init__(self, x, y, width, height):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    def __str__(self):
        return "(x = {}, y = {}, w = {}, h = {}), 면적 : {}".format(self.__x, self.__y, self.__width, self.__height, self.area())

    # 게터/세터 설정
    def set_x(self, value):
        self.__x = value
    def get_x(self):
        return self.__x
    def set_y(self, value):
        self.__y = value
    def get_y(self):
        return self.__y
    def set_width(self, value):
        self.__width = value
    def get_width(self):
        return self.__width
    
    def area(self):
        return self.__width * self.__height
    
    def overlaps(self, other):
        for i in range(self.__x, self.__x + self.__width + 1):
            for j in range(other.__x, other.__x + other.__width + 1):
                if i == j:
                    return True
        for n in range(self.__y, self.__y + self.__height + 1):
            for m in range(other.__y, other.__y + other.__height + 1):
                if n == m:
                    return True
        return False
    
    def contains(self, other):
        for j in range(other.__x, other.__x + other.__width + 1):
            for m in range(other.__y, other.__y + other.__height + 1):
                if j >= self.__x and j <= self.__x + self.__width and m >= self.__y and m <= self.__y + self.__height:
                    pass
                else:
                    return False
        return True
    
r1 = Rectangle(0, 0, 100, 100)
r2 = Rectangle(0, -10, 10, 10)
r3 = Rectangle(-100, 0, 120, 100)

print('r1 =', r1)
print('r2 =', r2)
print('r3 =', r3)

print('r1 contains r2 :', r1.contains(r2))
print('r1 contains r3 :', r1.contains(r3))
print('r1 overlaps r2 :', r1.overlaps(r2))
print('r1 overlaps r3 :', r1.overlaps(r3))


# 9.13 (기준을 좌측 상단으로 수정하여 코드 작성해보자)
class Rectangle:
    def __init__(self, x, y, width, height):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    def __str__(self):
        return "(x = {}, y = {}, w = {}, h = {}), 면적 : {}".format(self.__x, self.__y, self.__width, self.__height, self.area())

    # 게터/세터 설정
    def set_x(self, value):
        self.__x = value
    def get_x(self):
        return self.__x
    def set_y(self, value):
        self.__y = value
    def get_y(self):
        return self.__y
    def set_width(self, value):
        self.__width = value
    def get_width(self):
        return self.__width
    
    def area(self):
        return self.__width * self.__height
    
    def overlaps(self, other):
        for i in range(self.__x, self.__x + self.__width + 1):
            for j in range(other.__x, other.__x + other.__width + 1):
                if i == j:
                    return True
        for n in range(self.__height, self.__y + self.__height + 1):
            for m in range(other.__y, other.__y + other.__height + 1):
                if n == m:
                    return True
        return False
    
    def contains(self, other):
        for j in range(other.__x, other.__x + other.__width + 1):
            for m in range(other.__height, other.__y + other.__height + 1):
                if ( j >= self.__x and j <= self.__x + self.__width ) and ( m >= self.__height and m <= self.__y + self.__height ):
                    pass
                else:
                    return False 
        return True

r1 = Rectangle(0, 0, 100, 100)
r2 = Rectangle(0, -10, 10, 10)
r3 = Rectangle(-100, 0, 120, 100)

print('r1 =', r1)
print('r2 =', r2)
print('r3 =', r3)

print('r1 contains r2 :', r1.contains(r2))
print('r1 contains r3 :', r1.contains(r3))
print('r1 overlaps r2 :', r1.overlaps(r2))
print('r1 overlaps r3 :', r1.overlaps(r3))

# 추가문제 6번 (정답 3번)
class Car:
    def method(self):
        print("슈퍼 클래스")

class Sedan(Car):
    def method(self):
        print("서브 클래스")

myCar = Car()
mySedan = Sedan()
myCar.method()
mySedan.method()

# 추가문제 7번
class Car:
    speed = 0

    def upSpeed(self, value):
        self.speed = self.speed + value

class RVCar(Car):
    seatNum = 0

    def getSeatNum(self):
        return self.seatNum