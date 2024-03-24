# for 문
iend = 20
total = 0

for i in range(iend):
    total = total + i + 1
                         
print(total)

# while 문
i = 0
total = 0

while i < 20 :
    i = i + 1
    total = total + i

print(total)

#
for m in ["사과", "배", "복숭아", "자몽", "캐슈넛"]:
    if "캐슈넛" not in m:
        print("나는 ", m, "을 좋아합니다.")

#
for m in ["사과", "배", "복숭아", "자몽", "캐슈넛"]:
    if m not in "캐슈넛":
        print("나는 ", m, "을 좋아합니다.")

# '_' 로 반복
for _ in range(100) :
    print("I like you")

# 
numbers = [11, 22, 33, 44, 55, 66]

for n in numbers :
    print(n, end = ' ')

#
numbers = [11, 22, 33, 44, 55, 66]

for n in numbers :
    print(n, end = '\n')

#
numbers = [11, 22, 33, 44, 55, 66]

for n in numbers :
    print(n)

#
for ch in 'Hello':
    print(ch, end = ' ')    