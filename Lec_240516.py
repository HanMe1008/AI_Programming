# 2024/05/16 AI프로그래밍및실습 해양학전공

# 축을 비트는 것이 PCA
# 클래스는 프로퍼티와 비헤이브를 가지고있다(?)


#
from sklearn import datasets
from sklearn import svm

digit=datasets.load_digits()

# svm의 분류기 모델 SC를 학습
s=svm.SVC(gamma=0.1, C=10) # C=10 이면 완전히 맞다(?)
s.fit(digit.data, digit.target) # digit 데이터로 모델링

# 훈련 집합의 앞에 있는 샘플 3개를 새로운 샘플로 간주하고 인식해봄
new_d=[digit.data[0], digit.data[1], digit.data[2]]
print(new_d)
res = s.predict(new_d)
print("예측값은", res)
print("참값은", digit.target[0], digit.target[1], digit.target[2])

# 훈련 집합을 테스트 집합으로 간주하여 인식해보고 정확률을 측정
res = s.predict(digit.data)
correct = [i for i in range(len(res)) if res[i]==digit.target[i]]
accuracy=len(correct)/len(res)
#print(correct)
print("화소 특징을 사용했을 때 정확률=", accuracy*100, "%")

#print(len(res))

# 그림 그리기

import matplotlib.pyplot as plt

plt.figure(figsize=(5,5))
plt.imshow(digit.images[0], cmap=plt.cm.gray_r, interpolation='nearest')

plt.show()
print(digit.data[0])
print("이 숫자는 ", digit.target[0], "입니다.")


# 인공신경망에선 검증 집합이 중요하다 overfit(오버피팅)하지 않기 위해

"""
#
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split
import numpy as np

# 데이터셋을 읽고 훈련 집합과 테스트 집합으로 분할
digit = datasets.load_digits()
x_train, x_test, y_train, y_test = train_test_split(digit.data, digit.target, train_size=0.6)

# svm의 분류 모델 SVC를 학습
s = svm.SVC(gamma=0.001)
s.fit(x_train, y_train)

res = s.predict(x_test)

# 혼돈 행렬 구함
conf = np.zeros((10,10))
for i in range(len(res)):
    conf[res[i]][y_test[i]] += 1
print(conf)

# 정확률 측정하고 출력
no_correct=0
for i in range(10):
    no_correct += conf[i][i]
accuracy = no_correct / len(res)
print("테스트 집합에 대한 정확률은", accuracy*100, "%입니다")

# 보통 사용하는 모델들의 정확률은 80%
"""

"""
#
from sklearn import datasets
from sklearn import svm
import numpy as np

digit=datasets.load_digits()

# svm의 분류기 모델 SC를 학습
s=svm.SVC(gamma=0.1, C=10) # C=10 이면 완전히 맞다(?)
s.fit(digit.data, digit.target) # digit 데이터로 모델링

# 훈련 집합의 앞에 있는 샘플 3개를 새로운 샘플로 간주하고 인식해봄
new_d1=[digit.data[0], digit.data[1], digit.data[2]]
print(new_d1)
new_d=[np.flip(digit.data[0]), np.flip(digit.data[1]), np.flip(digit.data[2])]
res = s.predict(new_d)
print(new_d)
print("예측값은", res)
print("참값은", digit.target[0], digit.target[1], digit.target[2])

# 훈련 집합을 테스트 집합으로 간주하여 인식해보고 정확률을 측정
res = s.predict(digit.data)
correct = [i for i in range(len(res)) if res[i]==digit.target[i]]
accuracy=len(correct)/len(res)
print("화소 특징을 사용했을 때 정확률=", accuracy*100, "%")
"""

import cv2
import numpy as np
import subprocess

# Step 1: 이미지 읽기 및 이진화
def preprocess_image(image_path):
    # 이미지 읽기
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # 이진화
    _, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY_INV)
    # 이진화된 이미지 저장
    cv2.imwrite('binary_image.pbm', binary_image)

# Step 2: Potrace를 사용하여 벡터화
def convert_to_vector():
    # Potrace 명령어 실행
    subprocess.run(['potrace', 'binary_image.pbm', '--svg', '-o', 'output.svg'])

# 실행
image_path = 'no1.png'  # 손글씨 이미지 경로
preprocess_image(image_path)
convert_to_vector()
