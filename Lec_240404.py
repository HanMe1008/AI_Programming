# 2024/03/28 AI프로그래밍및실습 해양학전공 전상규


#
class Cat:      # Cat 클래스의 정의
    # 생성자 혹은 초기화 메소드라 한다
    def __init__(self, name, color='흰색'):
        self.name = name        # name이라는 인스턴스 변수를 생성
        self.color = color      # color라는 인스턴스 변수를 생성
    # 고양이의 정보를 출력하는 메소드
    def meow(self):
        print('내이름은 {}, 색깔은 {}. 야옹 야옹~~'.format(self.name, self.color))

nabi = Cat('나비', '검정색')        # nabi 인스턴스 생성
nero = Cat('네로', '흰색')          # nero 인스턴스 생성
mimi = Cat('미미', '갈색')          # mini 인스턴스 생성

nabi.meow()
nero.meow()
mimi.meow()


#
class Cat:      
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return 'Cat(name='+self.name+', color='+self.color+')'
    
nabi = Cat('나비', '검정색')
nero = Cat('네로', '흰색')
print(nabi)
print(nero)


# 캡슐화
class Cat:      
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    # Cat 객체의 문자열 표현방식
    def __str__(self):
        return 'Cat(name='+self.__name+', age='+str(self.__age)+')'
# self.__age를 외부에서 자유롭게 접근하는 것을 제한하고 음수가 되지 않도록 함
    def set_age(self, age):
        if age > 0:
            self.__age = age
    def get_age(self):
        return self.__age
    
nabi = Cat('나비', 3)   # nabi 인스턴스 생성
print(nabi)
nabi.set_age(4)         # set_age() 메소드를 통해서 age에 접근 
nabi.set_age(-5)        # set_age)_ 메소드를 통해서 age가 음수가 되지 않도록 함
nabi.__age = -5         # 동작 안함
print(nabi)


#
list_a = [10, 20, 30]
list_b = [10, 20, 30]

if list_a is list_b:
    print('list_a is list_b')
else:
    print('list_a is not list_b')       # 결과값 


# 특수 메소드
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    def add(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
v1 = Vector2D(30, 40)
v2 = Vector2D(10, 20)
v3 = v1.add(v2)
print('v1.add(v2) =', v3)


# 내적 구하기
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __mul__(self, other):
        return (self.x * other.x + self.y * other.y)
    
v1 = Vector2D(30, 40)
v2 = Vector2D(10, 20)
v3 = v1.__mul__(v2)
print('v1.__mul__(v2) =', v3)


# 내적 구하기 (캡슐화 O)
class Vector2D:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def __mul__(self, other):
        return (self.__x * other.__x + self.__y * other.__y)
    
v1 = Vector2D(30, 40)
v2 = Vector2D(10, 20)
v3 = v1.__mul__(v2)
print('{} * {} = {}'.format(v1, v2, v3))


# 원소끼리의 곱구하기
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    def __mul__(self, other):
        return Vector2D(self.x * other.x, self.y * other.y)
    
v1 = Vector2D(30, 40)
v2 = Vector2D(10, 20)
v3 = v1.add(v2)
print('v1.__mul__(v2) =', v3)


#
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    def __gt__(self, other):
        return self.x**2 + self.y**2 > other.x**2 + other.y**2
          
v1 = Vector2D(30, 40)
v2 = Vector2D(10, 20)

if v1 > v2 :
    print(v1)
else:
    print(v2)


