# 2024/03/28 AI프로그래밍및실습 해양학전공 전상규

# 2000년 1월 1일부터 날짜수 세기(전상규의 레전드 코드)
def julian(year, month, day):
    count_day = 0
    if year >= 2000 and year < 2024:
        # 윤년 생각
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            count_day += (year - 2000) * 366
        else:
            count_day += (year - 2000) * 365
        # 달마다 다른 일수 생각 
        for i in range(1, month):
            if month == 2:
                if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
                    count_day += 29
                else:
                    count_day += 28
            elif month == 4 or month == 6 or month == 9 or month == 11:
                count_day += 30
            else:
                count_day += 31
        # 일수 더하기
        count_day += day
    return count_day

days = julian(2001, 12, 15)  # 내 생일 입력
print("{}번째 날입니다".format(days))

#
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def mult(self, other):
        return Vector2D(self.x * other.x, self.y * other.y)
    
    def __str__(self):
        return "({}, {})".format(self.x, self.y)

def vect_mul(v1, v2):
    v3 = v1.mul(v2)
    return v3

a = Vector2D(10, 20)
b = Vector2D(2, 3)

print(vect_mul(a, b))

# 과제
# Vector2D 한줄 한줄 코드 파헤치기
