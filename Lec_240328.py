# 2024/03/28 AI프로그래밍및실습 해양학전공 전상규

# 
score_list = [87, 84, 95, 67, 88, 94, 63]
for i in score_list:
    print(i)
print("---------------------------")

# range() 함수를 리스트에 넣기
a = list(range(0, 9))
print(a)
print("---------------------------")

# 
n_list = [11, 22, 33, 44, 55, 66]
print(n_list[-2:])
print("---------------------------")

# append() 함수
a_list = ['a', 'b', 'c', 'd', 'e']
a_list.append('f')
print(a_list)
print("---------------------------")

n_list = [10, 20, 30, 40]
n_list.append(50)
print(n_list)
print("---------------------------")

# del() 함수
n_list = [11, 22, 33, 44, 55, 66]
print(n_list)

del n_list[3]
print(n_list)
print("---------------------------")

# remove() 함수
n_list = [11, 22, 33, 44, 55, 66]
print(n_list)

n_list.remove(44)
print(n_list)
print("---------------------------")

# pop() 메소드
n_list = [11, 22, 33, 44, 55, 66]
print(n_list)

print(n_list.pop(5))
print(n_list)
print("---------------------------")

# sort() 메소드
list1 = [20, 10, 40, 50, 30]
list1.sort()
print(list1)
print("---------------------------")

# sort 함수는 리스트 자체를 반환하기 때문에 반환값이 None
list2 = [20, 10, 40, 50, 30]
list2.sort(reverse = True)
print(list2)
print("---------------------------")

list3 = [20, 10, 40, 50, 30]
list4 = sorted(list3)
print(list4)
print("---------------------------")

# extend() 메소드
list1 = ['a', 'b']
list2 = [10, 20]
list3 = list1 + list2
print(list3)
print("---------------------------")

list1.extend(list2)
print(list1)
# extend 함수는 리스트 자체를 반환하기 때문에 반환값이 None
print(list1.extend(list2))
print("---------------------------")

# 모든 원소에 10을 곱하여 보기
list1 = [10, 20, 30, 40, 50]
list1 = [n * 10 for n in list1]
print(list1)
print("---------------------------")

# 딕셔너리
person = {'이름' : '홍길동', '나이' : 26, '몸무게' : 82}
print(person['나이']) 
print("---------------------------")

# 딕셔너리 항목 삽입
person['번호'] = '010-6365-6161'
print(person['번호'])

# 딕셔너리 항목 수정
person['나이'] = 27
print(person['나이'])

# 딕셔너리 항목 삭제
del person['나이']
print(person)