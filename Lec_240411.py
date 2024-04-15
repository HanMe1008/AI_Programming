# 2024/04/11 AI프로그래밍및실습 해양학전공

# 클래스 선언 부분 #
class Car :
    speed = 0
    def upSpeed(self, value):
        self.speed += value

        print("현재 속도(슈퍼 클래스) : %d" % self.speed)

class Sedan(Car):
    def upSpeed(self, value):
        self.speed += value
        
        if self.speed > 150:
            self.speed = 150


#
class Car:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.speed = 0

    def upSpeed(self, value):
        self.speed += value

    def reset(self):
        self.speed = 0

class Sedan(Car):
    # 있던 함수지만 조건 추가
    def upSpeed(self, value):
        self.speed += value

        if self.speed > 150:
            self.speed = 150

    # 없던 함수
    def downSpeed(self, value):
        self.speed -= value
        
        if self.speed < 0:
            self.speed = 0

myCar = Sedan('Volvo', 2023)

myCar.upSpeed(50)
print(myCar.speed)

myCar.downSpeed(20)
print(myCar.speed)

myCar.reset()
print(myCar.speed)


#
class Television:
    serialNumber = 0       # 이것이 정적 변수이다.
    def __init__(self):
        Television.serialNumber += 1
        self.number = Television.serialNumber
    
tv1 = Television()
print(tv1.number)

tv2 = Television()
print(tv2.number)

tv3 = Television()
print(tv3.number)

print(tv1.number)
print(tv2.number)
print(tv3.number)
print(Television.serialNumber)


#
a, b = input('두 수를 입력하시오: ').split()
result = int(a) / int(b)        # 0으로 나누는 오류

# 
try:
    a, b = input('두 수를 입력하시오: ').split()
    result = int(a) / int(b)
    print('{}/{} = {}'.format(a, b, result))
except:
    print('수가 정확한지 확인하세요.')

#
try:
    b = 2 / 0
    a = 1 + 'hundred'
except Exception as e:
    print('error :', e)

#
try:
    b = 2 / 0
    a = 1 + 'hundred'
except ZeroDivisionError:
    print('0으로 나누는 오류')
except TypeError:
    print('지원되지 않는 연산자를 사용하는 오류')

# 이런식으로 시험문제
while True:
  try:
    a, b = map(int, input('두 수를 입력하세요 :').split())
    result = a/b
    print('{} / {} = {}'.format(a, b, result))
    break
  except ZeroDivisionError:
    print('입력 숫자를 확인해 주세요.')
 
 # try-except-(else)-finally 문
 def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('0으로 나누는 오류발생')
    else:
        print('결과 :', result)
    finally:
        print('수행완료')

# raise 문 (사용자가 지정한 오류를 띄움)
def get_ans(ans):
    if ans in ['예', '아니오']:
        print('정상적인 입력입니다.')
    else:
        raise ValueError('입력을 확인하세요.')
while True:
    try:
        ans = input('예/아니오 중 하나를 입력하세요 :')
        get_ans(ans)
        break
    except Exception as e:
        print('error :', e)