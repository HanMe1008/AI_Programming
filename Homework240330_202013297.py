# 해양학전공 전상규

# 5.1
list_ex = [10, 20, 30, 40, 50, 60, 70]
high = 5
low = 3

print(list_ex[low])
print(list_ex[low + 2])
print(list_ex[high - low])
print(list_ex[low - high])
print(list_ex[-1])
print(list_ex[-low])
print(list_ex[2 * 3])
print(list_ex[2] * 3)
print(list_ex[5 % 4])
print(len(list_ex))

# 5.3
list1 = [3, 5, 7]
list2 = [2, 3, 4, 5, 6]

for m in list1:
    for n in list2:
        print(m, "*", n, "=", m * n)

# 5.5
list1 = ['I like', 'I love']
list2 = ['pancakes.', 'liwi juice.', 'espresso.']

for m in list1:
    for n in list2:
        print(m, n)
        
# 5.7
n_list = [10, 20, 30, 50, 60]
sum = 0

for n in n_list:
    sum += n

print("리스트의 원소들 :", n_list)
print("리스트 원소들의 합 :", sum)
        
# 5.9
n_list = [10, 20, 30, 40, 50, 60]
max = 0

for n in n_list:
    if max < n:
        max = n

print("리스트의 원소들 :", n_list)
print("리스트 원소들 중 최대값 :", max)

# 5.11
n_list = list(map(int, input("5개의 수를 입력하세요:").split()))

# 오류 - TypeError: 'int' object is not callable
# 앞선 문제에서 sum과 max를 변수로 사용하여 오류가 발생했음
# 앞으로는 sum 대신 total, max 대신 max_num을 쓰자 !
# 변수를 제거함으로써 오류 해결
del sum
del max

print('합 :',sum(n_list))
print('평균 :', sum(n_list)/len(n_list))
print('최댓값 :', max(n_list))
print('최솟값 :', min(n_list))

# 5.13
n_list = list(map(int, input("10개의 수를 입력하세요 :").split()))

sigma = 0

for i in n_list:
    sigma += ( ( sum(n_list)/len(n_list) ) - i )**2

standard_deviation = ( sigma / len(n_list) )**(1/2)

print('합 :', sum(n_list))
print('평균 :', sum(n_list)/len(n_list))
print('표준편차 :', round(standard_deviation, 2))

# 5.15
greet = 'Have a beautiful day.'

print(greet[0:4])
print(greet[7:16])
print(greet[-4:-1])

# 5.17
animals = ['dog', 'cat', 'tiger', 'lion']
print("animals =", animals)

animals = ['dog', 'cat', 'tiger', 'lion']
animals.append(animals[0])
animals[0] = animals[1]
animals[1] = animals[2]
animals[2] = animals[3]
del(animals[3])
print(animals)

animals = ['dog', 'cat', 'tiger', 'lion']
for i in animals:
    print('I love {}.'.format(i))

# 5.19
s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
new_s_list = []

for s in s_list:
    if s not in new_s_list:
        new_s_list.append(s)

print('s_list =', s_list)
print('new_s_list =', new_s_list)

# aabbbccccccaacccfg 출력
src = 'a2b3c6a2c3f1g1'

for ch in src:
  if ch.isnumeric():
    for i in range(int(ch)):
      print(ch_old, end='')
  else:
    ch_old = ch

# 5.23(1)
# [이름, 나이, 성별(남자=1), 키, 몸무게]
person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]

def how_many_persons(person_list):
    return int((len(person_list) / 5))

# 5.23(2)
person_list = person1 + person3 + person4
n_persons = how_many_persons(person_list)
print(str(n_persons) + '명의 정보가 담겨 있습니다.')

def compute_average_age(person_list):
    return sum( person_list[1:2]+person_list[6:7]+person_list[11:12]+person_list[16:17] ) / ( len(person_list) / 5 )

person_list = person1 + person2 + person3 + person4
average_age = compute_average_age(person_list)
print('평균 나이는 '+ str(average_age) +'세입니다.')

# 5.23(3)
person_list = person1 + person2 + person3 + person4

def count_males_females(person_list):
    n_male = 0
    n_female = 0
    for i in range(2, 19, 5):
        if person_list[i] == 1:
            n_male += 1
        else:
            n_female += 1
    return n_male, n_female

n_male, n_female = count_males_females(person_list)
print('리스트에는 남자가', n_male, '명, 여자가', n_female, '명입니다.')

# 5.23(4)
person_list = person1 + person2 + person3 + person4

def display_persons(person_list):
    print(person_list[0:5])
    print(person_list[5:10])
    print(person_list[10:15])
    print(person_list[15:20])

display_persons(person_list)9