# 2024/06/03 AI프로그래밍및실습 해양학전공

"""
## 텐서플로 버전과 동작 확인 ##
import tensorflow as tf

print(tf.__version__)
a=tf.random.uniform([2,3],0,1)
print(a)
print(type(a))


## tensorflow와 numpy의 호환 ##
import tensorflow as tf
import numpy as np

t=tf.random.uniform([2,3],0,1)
n=np.random.uniform(0,1,[2,3])
print("tensorflow로 생성한 텐서:\n",t,"\n")
print("numpy로 생성한 ndarray:\n",n,"\n")

res=t+n     # 텐서 t와 ndarray n의 덧셈
print("덧셈 결과:\n",res)

## 텐서플로가 제공하는 데이터셋의 텐서 구조 확인하기 ##
import tensorflow as tf
import tensorflow.keras.datasets as ds

# MNIST 읽고 텐서 모양 출력
(x_train, y_train), (x_test, y_test) = ds.mnist.load_data()
yy_train = tf.one_hot(y_train, 10, dtype = tf.int8)        #원핫 코드로 변환
print("MNIST: ", x_train.shape, y_train.shape, yy_train.shape)

# CIFAR-10 읽고 텐서 모양 출력
(x_train, y_train), (x_test, y_test) = ds.cifar10.load_data()
yy_train = tf.one_hot(y_train, 10, dtype = tf.int8)        
print("CIFAR-10: ", x_train.shape, y_train.shape, yy_train.shape)

# Boston Housing 읽고 텐서 모양 출력
(x_train, y_train), (x_test, y_test) = ds.boston_housing.load_data()
print("Boston Housing: ", x_train.shape, y_train.shape)

# Reuters 읽고 텐서 모양 출력
(x_train, y_train), (x_test, y_test) = ds.reuters.load_data()
print("Reuters: ", x_train.shape, y_train.shape)

## 텐서플로 프로그래밍: [예제4-1]의 퍼셉트론 동작 ##
import tensorflow as tf

# OR 데이터 구축
x = [[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]]
y = [[-1], [1], [1], [1]]

# [그림 4-3(b)]의 퍼셉트론
w = tf.Variable([[1.0], [1.0]])
b = tf.Variable(-0.5)

# 식 4.3의 퍼셉트론 동작
s = tf.add(tf.matmul(x, w), b)
o = tf.sign(s)

print(o)
"""

## 텐서플로 프로그래밍: 퍼셉트론 학습 ##
import tensorflow as tf

# OR 데이터 구축
x = [[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]]
y = [[-1], [1], [1], [1]]
#print(x, y)

# 가중치 초기화
w = tf.Variable(tf.random.uniform([2, 1], -0.5, 0.5))
b = tf.Variable(tf.zeros([1]))

# 옵티마이저
opt = tf.keras.optimizers.SGD(learning_rate = 0.1)

# 전방 계산(식 (4.3))
def forward():
    s = tf.add(tf.matmul(x, w), b)
    o = tf.tanh(s)
    return o

# 손실 함수 정의
def loss():
    o = forward()
    return tf.reduce_mean((y-o)**2)

# 500세대까지 학습(100세대마다 학습 정보 출력)
for i in range(500):
    opt.minimize(loss, var_list=[w, b])
    if(i%100==0): print('loss at epoch', i, '=', loss().numpy())
    
# 학습된 퍼셉트론으로 OR 데이터를 예측
o = forward()
print(o)

print(w, b)

### 텐서플로를 잘 활용하면 loss 함수만으로 미분 할 필요가없다
