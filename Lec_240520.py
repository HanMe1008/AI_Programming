# 2024/05/20 AI프로그래밍및실습 해양학전공

"""
#
import numpy as np
X = np.array([   1, 0, 1]).reshape(3, 1)
w = np.array([-0.5, 1, 1]).reshape(3, 1)

s = sum(X*w)    # 또는 s = X.T @ w
print(s)

print((X.T@w).shape)
print(sum(X*w).shape)

#
import numpy as np
x2 = np.array([1, 0, 1])
w = np.array([-0.5, 1.0, 1.0])
s = sum(x2*w)
print(s)

#
import numpy as np
x = np.array([[1,0,0], [1,0,1], [1,1,0], [1,1,1]])
w = np.array([-0.5, 1.0, 1.0])
s = np.sum(x*w, axis=1)
print(s)
"""

## OR 데이터에 퍼셉트론 적용 ##
from sklearn.linear_model import Perceptron

# 훈련 집합 구축
X = [[0,0], [0,1], [1,0], [1,1]]
y = [-1, 1, 1, 1]

# fit 함수로 Perceptron 학습
p = Perceptron()
p.fit(X, y)

# p.intercept_ 가 w0를 의미
print("학습된 퍼셉트론의 매개변수: ", p.coef_, p.intercept_)
print("훈련집합에 대한 예측: ", p.predict(X))
print("정확률 측정: ", p.score(X, y)*100, "%")

 