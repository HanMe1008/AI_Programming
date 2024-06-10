import numpy as np

def costf(w,x,y):
    yp = w.T@x
    # cost function 안에서는 step_func을 사용하지 않는다.
    #yp = step_func(wi.T@xi) 
    return (yp-y.T)@(yp-y.T).T

def gradJ(w):
    return np.array([8*w[0]+4*w[1]+4*w[2]-4,
                     4*w[0]+4*w[1]+2*w[2]-4,
                     4*w[0]+2*w[1]+4*w[2]-4])

def step_func(x):
    y = x>0
    return 2*y.astype(int)-1

xi = np.array([[1,1,1,1],[0,0,1,1],[0,1,0,1]])
yi = np.array([[-1],[1],[1],[1]])
wi = np.array([[0],[0],[0]])

alpha = 0.01

J = costf(wi,xi,yi)

#w0 = []
#w1 = []
#w2 = []

while(True):
    JP = J
    delw = alpha*gradJ(wi)
    wi = wi - delw
    J = costf(wi,xi,yi)
    #w0.append(wi[0])
    #w1.append(wi[1])
    #w2.append(wi[2])
    #print(J,wi.T,step_func(wi.T@xi))
    if(np.abs((J-JP)/J) < 0.000001): break

print(wi)
print(step_func(wi.T@xi))

"""
# 3차원에 w0, w1, w2 그려보기
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(111, projection='3d')

#ax.plot(w0, w1, w2)
ax.scatter(w0, w1, w2, color = 'r', s=0.5 ,alpha = 0.5)
plt.show()
"""