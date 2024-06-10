"""
# (1) 손글씨 그림 벡터화 후 그리기
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image_files = ['test_no0.png', 'test_no1.png', 'no2.png', 'no3.png', 'no4.png',
               'no5.png', 'no6.png', 'no7.png', 'no8.png', 'no9.png']

images = []

for file in image_files:
    image = Image.open(file).convert('L')
    # .convert('L') : 이미지를 흑백 (grayscale)로 변환
    image = image.resize((8, 8))
    image = np.array([image]) / 16
    image = image // 1
    image = image.reshape(8, 8)
    plt.imshow(image, cmap='gray')
    plt.show()
"""

# (2) 손글씨 파일 벡터화하여 리스트에 저장(1차원)
from PIL import Image
import numpy as np

image_files = ['test_no0.png', 'test_no1.png', 'no2.png', 'no3.png', 'no4.png',
               'no5.png', 'no6.png', 'no7.png', 'no8.png', 'no9.png']

images = []

for file in image_files:
    image = Image.open(file).convert('L')
    image = image.resize((8, 8))
    image = 16 - (np.array([image]) / 16)
    image = image // 1
    image = image.reshape(64)
    images.append(image)


# (3) 리스트를 모델에 넣어 예측값 확인하기(gamma값 0.1에서 0.001로 수정)
from sklearn import datasets
from sklearn import svm

digit=datasets.load_digits()

s=svm.SVC(gamma=0.001, C=10) 
s.fit(digit.data, digit.target) 

new_d=[images[0], images[1], images[2], images[3], images[4],
       images[5], images[6], images[7], images[8], images[9]]

res = s.predict(new_d)
print("예측값은", res)
print("참값은", "[0 1 2 3 4 5 6 7 8 9]")


# (4) 정확률 계산하기
correct = [i for i in range(len(res)) if res[i]==digit.target[i]]
accuracy=len(correct)/len(res)
print("화소 특징을 사용했을 때 정확률=", accuracy*100, "%")
