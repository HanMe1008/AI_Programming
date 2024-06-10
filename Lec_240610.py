# 2024/06/10 AI프로그래밍및실습 해양학전공

"""
## 케라스 프로그래밍: 퍼셉트론 학습 ##
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD

# OR 데이터 구축
x = np.array([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]])
y = np.array([[-1], [1], [1], [1]])

n_input = 2
n_output = 1

perceptron = Sequential()
perceptron.add(Dense(units=n_output, activation='tanh',
                     input_shape=(n_input,),kernel_initializer='random_uniform',
                     bias_initializer='zeros'))

perceptron.compile(loss='mse', optimizer=SGD
                   (learning_rate=0.1), metrics=['mse'])
perceptron.fit(x, y, epochs=500, verbose=2)

res = perceptron.predict(x)
print(res)

# Sequential()은 층을 하나만 두겠다 (hidden layer 없이)
# bias는 편차
# compile 은 모델을 학습하는것
# fit는 최적화시키는 것
# loss='mse' : 손실함수를 mean square(?)로
# learning.rate : 얼마나 빠르게 접근할 것이냐
# metrics : 평가기준, 어떻게 평가할 것이냐? mse 그래도 사용
# epochs : 몇 번 반복할 것이냐
# verbose : fitting 하는 과정을 화면에 보여줘라
"""

## 텐서플로 프로그래밍: 다중 퍼셉트론으로 MNIST 인식 ##
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# MNIST 읽어 와서 신경망에 입력할 형태로 변환
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(60000, 784) # 784 = 28^2      # 텐서 모양 변환
x_test  = x_test.reshape(10000, 784)
x_train = x_train.astype(np.float32) / 255.0            # ndarray로 변환
x_test  = x_test.astype(np.float32) / 255.0
y_train = tf.keras.utils.to_categorical(y_train, 10)    # 원핫 코드로 변환
y_test  = tf.keras.utils.to_categorical(y_test, 10)

n_input = 784
n_hidden = 1024
n_output = 10

mlp=Sequential()
# units는 output의 개수를 의미
mlp.add(Dense(units=n_hidden,       
              activation='tanh',
              input_shape=(n_input,),
              kernel_initializer='random_uniform',
              bias_initializer='zeros'))
mlp.add(Dense(units=n_output,
              activation='tanh',
              kernel_initializer='random_uniform',
              bias_initializer='zeros'))
mlp.compile(loss='mean_squared_error',
            optimizer=Adam(learning_rate=0.001),
            metrics=['accuracy'])
hist = mlp.fit(x_train, y_train, batch_size=128, epochs=30,
               validation_data=(x_test, y_test), verbose=2)

res = mlp.evaluate(x_test, y_test, verbose=0)
print("정확률은", res[1]*100)
print(res)
# res[0] : loss(오차값으로 0에 가까우면 정확함)
# res[1] : 정확도(1에 가까울수록 정확함)












