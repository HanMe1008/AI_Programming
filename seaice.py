# 해양학전공 전상규 2024.03.24

# 8월달의 북극 해빙 면적 데이터
import matplotlib.pyplot as plt
import csv

f = open('seaice.csv',"r",encoding='UTF-8-sig')
data = (csv.reader(f))
next(data)
result = []
year = []

for row in data :
    result.append(float(row[1]))
    year.append(row[0].split(" ")[0])
    
plt.rc('font', family='NanumBarunGothic')
plt.figure(figsize = (30,5))
plt.title('북극 해빙 면적 평균(10^6km)')
plt.plot(year, result, linewidth=4)
plt.ylim([4.5, 8.5])     # Y축의 범위: [ymin, ymax]
plt.grid(True, axis='y')        # Y축 그리드 설정

plt.show()


# 8월달의 남극 해빙 면적 데이터

import matplotlib.pyplot as plt
import csv

f = open('seaice.csv',"r",encoding='UTF-8-sig')
data = (csv.reader(f))
next(data)
result = []
year = []

for row in data :
    result.append(float(row[2]))
    year.append(row[0].split(" ")[0])

plt.rc('font', family='NanumBarunGothic')
plt.figure(figsize = (30,5))
plt.plot(year, result, linewidth=4)
plt.title('남극 해빙 면적 평균(10^6km)')
plt.grid(True, axis='y')

plt.show()