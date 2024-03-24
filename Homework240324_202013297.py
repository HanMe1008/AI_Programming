# 해양학전공 전상규

#4.1
def my_greet():
    print("환영합니다")

my_greet()
my_greet()

#4.3
def max2(m, n):
    if m > n:
        return m
    else:
        return n

def min2(m, n):
    if m > n:
        return n
    else:
        return m
    
print('100과 200중 큰 수는 :', max2(100, 200))
print('100과 200중 작은 수는 :', min2(100, 200))

#4.5
def inch2cm(inch):
    cm = inch * 2.54
    print(inch, '인치 =', cm, '센티미터')
    
inch2cm(1)
inch2cm(2)
inch2cm(3)
inch2cm(4)
inch2cm(5)

#4.7
def mean3(a, b, c):
    mean = (a+b+c)/3
    print('{}, {}, {}의 평균값은'.format(a,b,c), mean)
    
def max3(a, b, c):
    print('{}, {}, {}의 최댓값은'.format(a,b,c), max(a,b,c))
    
def min3(a, b, c):
    print('{}, {}, {}의 최솟값은'.format(a,b,c), min(a,b,c))


a,b,c = map(int,input("세 수를 입력하시오 : ").split())

mean3(a,b,c)
max3(a,b,c)
min3(a,b,c)

#4.9
nums = list(map(int, input("정수를 여러 개 입력하시오 :").split()))

def mean_of_n(nums):
    mean_of_n = sum(nums) / len(nums)
    return mean_of_n
    
def max_of_n(nums):
    max_of_n = max(nums)
    return max_of_n

def min_of_n(nums):
    min_of_n = min(nums)
    return min_of_n

print('평균값은','{:.1f}'.format(mean_of_n(nums)))
print('최댓값은','{}'.format(max_of_n(nums)))
print('최솟값은','{}'.format(min_of_n(nums)))

#4.11
x1 = int(input("x1 좌표를 입력하시오 : "))
y1 = int(input("y1 좌표를 입력하시오 : "))
x2 = int(input("x2 좌표를 입력하시오 : "))
y2 = int(input("y2 좌표를 입력하시오 : "))

def area(x1, y1, x2, y2):
    area = (x2-x1)*(y2-y1)/2
    return area

print('직각삼각형의 면적은 : {}'.format(area(x1, y1, x2, y2)))

#4.13
def cube(s):
    volume = s**3
    return volume

print("모서리의 길이가 12인 정육면체 :", cube(12))
print("모서리의 길이가 20인 정육면체 :", cube(20))

def cuboid(w, h, l):
    volume = w*h*l
    return volume

print("가로, 세로, 길이가 각각 3, 5, 6인 직육면체", cuboid(3,5,6))

pi = 3.14
def cone(r, h):
    volume = (1/3)*pi*(r**2)*h
    return volume

print("반지름과 높이가 각각 20, 10인 원뿔", cone(20,10))

def sphere(r):
    volume = (4/3)*pi*(r**3)
    return volume

print("반지름이 15인 구", sphere(15))

def cylinder(r, h):
    volume = pi*(r**2)*h
    return volume

print("반지름과 높이가 각각 20, 10인 원기둥", cylinder(20, 10))

#4.15
def my_sort(*nums):
    a = list(nums)
    a.sort()
    return a

print(my_sort(45, 3, 4, 56, 5))
print(my_sort(9, 8, 7, 6, 5, 4, 3))

#4.17
def sum_range(n1, n2):
    sum = 0
    for i in range(n1, n2+1, 1):
        sum += i
    return sum

print("10에서 20까지의 정수의 합 :",sum_range(10, 20))
print("40에서 100까지의 정수의 합 :",sum_range(40, 100))

#4.19
def fibo(n):
    if n <= 1:
        return 1
    return fibo(n-1) + fibo(n-2)
n = int(input("fibo(n)의 n을 입력하세요 : "))
print('fibo({}) = {}'.format(n, fibo(n)))

#4.21
birth = input("주민등록번호 첫 6숫자 형식 입력: ")

if int(birth[0:2]) <= 49:
    print('20'+birth[0:2]+'년',birth[2:4]+'월',birth[4:]+'일')
else:
    print('19'+birth[0:2]+'년',birth[2:4]+'월',birth[4:6]+'일')

#4.23
import numpy as np 

def area_and_circumference(r):
    area = np.pi*r**2
    circumference = 2*np.pi*r
    return area, circumference

while True:
    r = int(input("반지름을 입력하시오: "))
    if r < 0:
        print("프로그램을 종료합니다")
        break
    area,circumference = area_and_circumference(r)
    print("넓이 : {:7.3f}, 둘레 : {:7.3f}".format(area,circumference))

#4.25
s1 = 'Kang Young Min'
s2 = ' Kang Young-Min'
s3 = 'Park Dong Min'
s4 = ' Park Dong-Yun'

print(s1+'(은)는', s1.replace(' ', '').replace('-', '').upper()+'(으)로 수정됨')
print(s2+'(은)는', s2.replace(' ', '').replace('-', '').upper()+'(으)로 수정됨')
print(s3+'(은)는', s3.replace(' ', '').replace('-', '').upper()+'(으)로 수정됨')
print(s4+'(은)는', s4.replace(' ', '').replace('-', '').upper()+'(으)로 수정됨')

print(s1.replace(' ', '').replace('-', '').upper(), ': {} 개의 N이 나타남'.format(s1.upper().count('N')))
print(s2.replace(' ', '').replace('-', '').upper(), ': {} 개의 N이 나타남'.format(s2.upper().count('N')))
print(s3.replace(' ', '').replace('-', '').upper(), ': {} 개의 N이 나타남'.format(s3.upper().count('N')))
print(s4.replace(' ', '').replace('-', '').upper(), ': {} 개의 N이 나타남'.format(s4.upper().count('N')))

#4.27
def unit_fraction(frac):
    i = int(1/frac)
    if (1/i - frac) < (1/(i+1) - frac):
        return i
    else:
        return i+1

frac = float(input("1보다 작고 0보다 큰 소수를 입력하세요: "))
i = unit_fraction(frac)
print("가장 가까운 단위 분수는 1/{}이며, 이 값은 {}입니다.".format(i, 1/i))