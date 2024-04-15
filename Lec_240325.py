# 2024/03/25 AI프로그래밍및실습 해양학전공 전상규

# factorial 함수 정의
def factorial(n):
    if n <= 1 :
        return 1
    else :
        return n * factorial(n-1)
    
print(factorial(5))

# factorial for 함수 이용 (시험 출제 가능)
def factorial2(n):
    tmp = 1
    for i in range(n):
        tmp *= i+1
    return tmp

print(factorial2(5))

# 피보나치 수열
def fibonacci(n):
    if n <= 1:
        return n
    else :
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(11))

# map, int, input 함수
a, b, c = map(int, input("세 수를 입력하세요 :").split())
print(a, b, c)

# 입력 변수의 개수를 모를 때 (시험 출제 가능)
a_list = list(map(int, input("여러 수를 입력하세요 :").split()))
print(type(a_list))
print(a_list)

# test1 (결과는 map)
a_list = map(list, input("여러 수를 입력하세요 :").split())
print(type(a_list))
print(a_list)

# test2 (결과는 map)
a_list = map(str, input("여러 수를 입력하세요 :").split())
print(type(a_list))
print(a_list)

# test3 (결과는 list)
a_list = list(map(str, input("여러 수를 입력하세요 :").split()))
print(type(a_list))
print(a_list)

# 질문 : 교수님 map(str, input)을 했을 때와 map(int, input)을 했을 때 type을 확인하면 모두 map인데 이 둘을 다시 list()에 넣으면 어떻게 다시 각각 str와 int로 리스트에 들어가는지 궁금합니다