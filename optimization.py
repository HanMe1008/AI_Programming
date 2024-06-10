import numpy as np

def costf(w,x,y):
    yp = w.T@x
    return (yp-y.T)@(yp-y.T).T

def gradJ(w):
    return np.array([8*w[0]+4*w[1]+4*w[2]-4,4*w[0]+4*w[1]+2*w[2]-4,4*w[0]+2*w[1]+4*w[2]-4])

def step_func(yvalue):
    y = yvalue>0
    return 2*y.astype(int)-1

xi = np.array([[1,1,1,1],[0,0,1,1],[0,1,0,1]])
yi = np.array([[-1],[1],[1],[1]])
wi = np.array([[1],[2],[3]])

rho = 0.01
J = costf(wi,xi,yi)
delW = gradJ(wi)
#count = 0

while(True):
    JP = J
    #print(JP)
    #count += 1
    delW = gradJ(wi)
    wi = wi - rho*delW
    J = costf(wi,xi,yi)
    if(np.abs((J-JP)/J) < 0.000001):
        #print("반복횟수 :", count)
        break

print(wi)
print("비용함수 =", JP)
print(step_func(wi.T@xi))
