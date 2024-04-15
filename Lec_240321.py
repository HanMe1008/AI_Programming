# 2024/03/21 AI프로그래밍및실습 해양학전공 전상규
#
#
def plus(a, b) :
    c = a + b
    return c

d = plus(3, 4)
print(d)

# 약수의 개수 함수 정의
def hyacsu(a) :
    total = 0
    for i in range(1,a):
        if a % i == 0:
            total += 1
    return total

print(hyacsu(18))

# 약수의 합 함수 정의
def hyacsu(a) :
    total = 0
    for i in range(1,a):
        if a % i == 0:
            total += i
    return total

print(hyacsu(18))

# 반지름을 입력받아서 원의 멵적과 둘레 구하는 함수 정의
import numpy as np 

def circle_area_circum(radius):
    area = radius**2 * np.pi
    circum = 2 * radius * np.pi
    return area, circum

radius = int(input('반지름을 입력하세요 : '))
area, circum = circle_area_circum(radius)

print('반지름이 {} 인 원의 면적은 {}, 원의 둘레는 {} 입니다.'.format(radius, area, circum))

# 간단한 버전
def circle(radius):
    return np.pi*radius**2, 2*np.pi*radius

print(circle(10))

# 전역변수 global

# 가변적인 인자전달
def greet(*names):
    for name in names:
        print('안녕하세요', name, '씨')

greet('홍길동', '양만춘', '이순신')
greet('James', 'Thomas')
 
# 
def sum_nums(*numbers):
    sum = 0
    total = 0
    for i in numbers:
        sum += i
        total += 1
    mean = sum / total
    print(len(numbers), '개의 인자', numbers)
    print('합계 :', sum , ', 평균 :', mean)
    return sum, mean

sum_nums(10, 20, 30, 40, 50)
    