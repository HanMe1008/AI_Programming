# 해양학전공 전상규

# 3.1
100 > 200   #False
100 >= 200  #False
100 < 200   #True
100 <= 200  #True
100 == 200  #False
100 != 200  #True
200 == 200  #True
200 != 200  #False
True or True    #True
True or False   #True
True and False  #False
True and True   #True
True or True and False  #True
True and True or False  #True
'Morning' < 'morning'   #True
'A' > 'B'   #False

# 3.3
age = int(input("나이를 입력하시오 : "))
height = int(input("키를 입력하시오(단위 cm) : "))

if age >= 19 and height >= 150 :
    print("입장할 수 있습니다")
else :
    print("입장할 수 없습니다.")

# 3.5
a,b = map(int,input("두 정수를 입력하시오 : ").split())

if a > b :
    print("{0} {1}".format(b,a))
else :
    print("{0} {1}".format(a,b))

# 3.7
score = int(input("게임점수를 입력하시오 : "))

if score >= 1000 :
    print('고수입니다.')
else :
    print('입문자입니다.')

# 3.9
num = int(input("정수를 입력하시오 : "))

if num % 2 == 0 :
    print("{0}는(은) 2(으)로 나누어집니다.".format(num))
else :
    print("{0}는(은) 2(으)로 나누어지지 않습니다.".format(num))

if num % 3 == 0 :
    print("{0}는(은) 3(으)로 나누어집니다.".format(num))
else :
    print("{0}는(은) 3(으)로 나누어지지 않습니다.".format(num))

if num % 2 == 0 and num % 3 == 0
    print("{0}는(은) 2와(과) 3 모두로 나누어집니다.".format(num))
else :
    print("{0}는(은) 2와(과) 3 모두로 나누어지지 않습니다.".format(num))

# 3.11 (map함수 활용)
a,b,c = map(int,input("세 복권번호를 입력하시오 : ").split())

if (a==2 and b==3 and c==9) :
    print("상금 1억 원") 
elif (a!=2 and b==3 and c==9) :
    print("상금 1천만 원")
elif (a==2 and b!=3 and c==9) :
    print("상금 1천만 원")
elif (a==2 and b==3 and c!=9) :
    print("상금 1천만 원")
elif (a!=2 and b!=3 and c==9) :
    print("상금 1만 원")
elif (a==2 and b!=3 and c!=9) :
    print("상금 1만 원")
elif (a!=2 and b==3 and c!=9) :
    print("상금 1만 원")
else :
    print("다음 기회에...")

# 3.11 (리스트 활용)
a = input("세 복권번호를 입력하시오 : ").split()

if "2" in a and "3" in a and "9" in a :
    print("상금 1억 원")
elif "2" not in a and "3" in a and "9" in a :
    print("상금 1천만 원")
elif "2" in a and "3" not in a and "9" in a :
    print("상금 1천만 원")
elif "2" in a and "3" in a and "9" not in a :
    print("상금 1천만 원")
elif "2" not in a and "3" not in a and "9" in a :
    print("상금 1만 원")
elif "2" in a and "3" not in a and "9" not in a :
    print("상금 1만 원")
elif "2" not in a and "3" in a and "9" not in a :
    print("상금 1만 원")
else :
    print("다음 기회에...")

# 3.13
x,y = map(int,input("점의 좌표 x, y를 입력하시오 : ").split())

if (x - 3)**2 + (y - 4)**2 > 100 :
    print("원의 외부에 있음")
else :
    print("원의 내부에 있음")

# 3.15 (for 문)
for i in range(1,10,1):
    print("2 * " + str(i) + " = " + str(2 * i))

# 3.15 (while 문)
i = 0

while i < 9:
    i += 1
    print("2 * " + str(i) + " = " + str(2 * i))

# 3.17
for i in range(3):
    print('Python ')
    print('is ')
    print('Fun! ')

for i in range(3):
    print('Python ')
    print('is ')
print('Fun! ')

# 3.19
print("맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.\n- 햄버거(입력 b)\n- 치킨(입력 c)\n- 피자(입력 p)")

menu = input("메뉴를 선택하세요(알파벳 b, c, p 입력) : ")

while menu not in ['b', 'c', 'p'] :
     menu = input("메뉴를 다시 입력하세요(알파벳 b, c, p 입력) : ")
     continue
if menu == 'c' :
    print("치킨을 선택하였습니다.")
elif menu == 'b' :
    print("햄버거를 선택하였습니다.")
else :
    print("피자를 선택하였습니다.")

# 3.21
n = int(input("숫자를 입력하세요 : "))

if n == 2:
    print('{}는 소수입니다'.format(n))
elif n % 2 == 0:
    print('{}는 소수가 아닙니다.'.format(n))
else:
    for i in range(3, n-1, 2):
        if n % i != 0:
            m = 'Y'
        else:
            m = 'N'
            break
                                                                             
    if m == 'N':
        print('{}는 소수가 아닙니다'.format(n))
    else:
        print('{}는 소수입니다'.format(n))

# 3.23
n = int(input('숫자를 입력하세요 : '))
result = 0 

for i in range(1, n+1):
    result += i**2
    
print(result)

# 3.25
day = 0
location = 0

while True :
    day += 1
    location += 7
    if location >= 30:
        print("day : {} \t 달팽이의 위치 : {} 미터".format(day,location))
        print("\n우물을 탈출하는 데 걸린 날은 {}일 입니다.".format(day))
        break
    print("day : {} \t 달팽이의 위치 : {} 미터".format(day,location))
    location -= 5
    
# 3.27
num=[]

for i in range(100,1000):
    a = i // 100
    b = (i // 10) % 10
    c = i % 10
    if i == a**3 + b**3 + c**3:
        num.append(i)
        
print("세 자리의 암스트롱 수 : {}".format(num))

# 3.29
a = 500

while True:
    a += int(input("충전 또는 사용한 연료를 +/- 기호와 함께 입력하시오: "))
    print("현재 탱크양은 {} 입니다.".format(a))
    if a < 50:
        print("경고 : 연료가 10% 미만이니 충전하세요!".format(a))
        break
# 3.31
