# 2024/03/14 AI프로그래밍및실습 해양학전공 전상규 

a = 100
print(type(a))

# 공백으로 문자열을 분리
print(input('문자열을 입력해주세요').split())

# 입력받은 숫자 2개의 배수 관계를 알아보기
a,b = map(int,input('정수를 입력하세요 : ').split())

if a % b == 0 :
    print("{0}은(는) {1}의 배수입니다.".format(a,b))
else :
    print("{0:d}은(는) {1:d}의 배수가 아닙니다.".format(a,b))   # {0:d} 에서 :d는 정수를 의미하기 ㄸ문에 문자열을 입력받으면 오류발생


# 윤년 구하기
a = int(input("연도를 입력하세요 : "))
        
if a % 400 == 0 or (a % 4 == 0 and a % 100 != 0):
    print("해당 연도는 윤년입니다")
else:
    print("해당 연도는 평년입니다")

# for 반복문을 이용하여 리스트 요소 합 구하기
numbers = [10, 20, 30, 40, 50]
total = 0

for m in numbers:
    total += m
    
print(total)

# while 문 사용
total = 0
i = 0

while i < 10:
    i += 1
    total += i
    
print(total)

# break
total = 0
i = 0

while True:
    i += 1
    total += i
    if i >= 10 :
        break
    
print(total)

# continue
total = 0
i = 0

while i < 9 :
    i += 1
    if i % 3 == 0: continue
    total += i
    
print(total)


