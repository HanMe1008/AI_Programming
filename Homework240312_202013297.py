# 해양학전공 전상규 

# 2.1
print( 100,'+', 200 ,'=', 100 + 200 )
print( 200,'+', 300 ,'+', 400 ,'=', 200 + 300 + 400 )

# 2.2
width = 30
height = 60
print(width)
print(height)

# 2.3
area = str(width * height)
print('사각형의 면적 : ' + area)

# 2.5
length = int(input('정사각형의 밑변을 입력하시오 : '))
area2 = str(length**2)
print('정사각형의 면적 : ' + area2)

# 2.7
x = str(1*2*3*4*5*6*7*8*9*10)
print('10! = '+ x)

# 2.9
celsius = [' 0', 10, 20, 30, 40, 50]
fahrenheit = []

for i in range(6):
    fahrenheit.append(9/5 * float(celsius[i]) + 32)

print('섭씨'+'     '+'화씨')
for i in range(6):
    print(str(celsius[i])+'       '+str(fahrenheit[i]))

# 2.11
fahrenheit = str(input('화씨 온도를 입력하세요 : '))
celsius = str(9/5 * int(fahrenheit) + 32)

print('화씨 '+fahrenheit+' 도는 섭씨 '+celsius+' 도 입니다.')

# 2.13
PI = 3.141592
r = input('원의 반지름을 입력하세요 : ')
원의둘레 = str(2 * PI * float(r))
원의면적 = str(PI * float(r)**2)

print('원의 둘레 = '+원의둘레+', 원의 면적 = '+원의면적)

# 2.14
for i in range(2,11,1):
    print(str(i)+'의 제곱근 = '+str(i**(1/2)))

# 2.15
a = input('밑변의 길이를 입력하세요.')
b = input('높이를 입력하세요.')
c = int(a)**2 + int(b)**2

print('빗변의 길이는 '+str(c**(1/2))+' 입니다.')

# 2.17
print(2 << 0, 2 << 1, 2 << 2, 2 << 3, 2 << 4, 2 << 5, 2 << 6, 2 << 7, 2 << 8, 2 << 9)

# 2.19
정수 = int(input('정수를 입력하세요 : '))

if 정수 % 2 == 1 and 0 <= 정수 <= 100 :
    print('입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요? False')
elif 정수 % 2 ==0 and 0 <= 정수 <= 100 :
    print('입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요? True')
else:
    print('입력된 정수가 0에서 100의 범위 안에 있지 않습니다.')
    
# 2.21
정수 = int(input('정수를 입력하시오 : '))

print(str(정수)+' 의 2진수 값 : '+bin(정수))
print(str(정수)+' 의 2진수 값에 대한 비트단위 부정값 :'+bin(~정수))

# 2.23
n = int(input('세 자리 정수를 입력하시오 : '))

print("백의 자리 : "+ str(n // 100))
print("십의 자리 : "+ str((n // 10)%10))
print("일의 자리 : "+ str(n % 10))

#