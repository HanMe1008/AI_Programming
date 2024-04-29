# 최대공약수

a, b = map(int, input("최대공약수를 구하고싶은 수를 입력하세요 :").split())
a_lst = []
b_lst = []
eq_lst = []

for n in range(1, a + 1):
    if a % n == 0:
        a_lst.append(n)

for m in range(1, b + 1):
    if b % m == 0:
        b_lst.append(m)

for i in b_lst:
    if i in a_lst:
        eq_lst.append(i)

print(max(eq_lst))



  