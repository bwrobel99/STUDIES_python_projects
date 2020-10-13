# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 16:46:43 2019

@author: bart
"""

from numpy import *
import numpy as np  
import math
import matplotlib.pyplot as plt

#1
v = linspace(-1.0,1.0,num=1000)

def czybyszew(n:int):
   
    return cos((linspace(1,n,n)*pi)/n)
    
        
#2
def not_differentiable(x:int):
    return sign(x)*x+x**2
def differentiable_onetime(x:int):
    return sign(x)*x**2
def differentiable_threetimes(x:int):
    return (abs(sign(5*x)))**3

def analitic(x:int, a:int):
    if a == 1 or a==25 or a==100:
        return 1/(1+a*x**2)
    else:
        return False
    def discontinuous(x:int):
        return sign(x)

#3
    
from scipy.interpolate import barycentric_interpolate
import timeit
def make_plot(arg: int):
    xch = czybyszew(arg)
    yimp = barycentric_interpolate(xch,not_differentiable(xch),v)
    plt.figure()
    plt.plot(xch,not_differentiable(xch),'go',label = 'wezly interpolacji')
    plt.plot(v,not_differentiable(v),'b',label = 'sign(x)*x+x^2')
    plt.plot(v,yimp,'r',label = 'interpolacja {}'.format(arg))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend(loc = 0)
    plt.grid()
    plt.show()

make_plot(10)
#make_plot(100)

N = 1000
x_i=czybyszew(N)
bar_w= lambda i : 1/np.prod(x_i[i]-np.delete(x_i,i))
w_i=np.array([bar_w(0),bar_w(1),bar_w(2),bar_w(3),bar_w(4)])
X=np.linspace(-1+1e-5,1-1e-5,101)
y_i=differentiable_onetime(x_i)
w_i=[np.power(-1,i) for i in range(N)]
w_i[0]=0.5
w_i[-1]=0.5*(-1)**N

def barycentric_interpolate(x_i,y_i,w_i,X):
    Y=[]
    for x in np.nditer(X):
        if x in x_i:
            #omijamy dzielenie przez 0
            Y.append(y_i[np.where(x_i==x)[0]])
        else:
            #wzór w drugiej formie
            L=w_i/(x-x_i)
            Y.append(y_i@L/sum(L)) 
    return np.array(Y)

Y=barycentric_interpolate(x_i,y_i,w_i,X)

plt.plot(X,differentiable_onetime(X))
plt.plot(X,Y)
plt.scatter(x_i,y_i)



#4
def norm(x1,x2):
    
    return max(abs(x1-x2))

#5
    
wynik = []
wynik2 = []
I = []
Y_org = differentiable_onetime(X)
for k in range(2, 1000, 10):
    x_i = np.array([np.cos(i*np.pi/k) for i in range(0, k+1)])
    y_i = differentiable_onetime(x_i)
    w_i = [np.power(-1,i) for i in range(k+1)]
    w_i[0] = 0.5
    w_i[k] = 0.5*(-1)**k
    Y = barycentric_interpolate(x_i, y_i,w_i,X)
    wynik.append(np.abs(np.max((Y-Y_org))))
    I.append(k)
    wynik2.append(k**(-1))
plt.figure()
ax = plt.gca()
ax.loglog(I, wynik,label='blad')
ax.loglog(I, wynik2, label='$n^{-3}$')
ax.legend()

wynik1 = []
I = []
Y_org = differentiable_threetimes(X)
wynik3 = []
for k in range(2, 1000, 10):
    x_i = np.array([np.cos(i*np.pi/k) for i in range(0, k+1)])
    y_i = differentiable_threetimes(x_i)
    w_i = [np.power(-1,i) for i in range(k+1)]
    w_i[0] = 0.5
    w_i[k] = 0.5*(-1)**k
    Y = barycentric_interpolate(x_i, y_i,w_i,X)
    wynik1.append(norm(Y, Y_org))
    wynik3.append(k**(-3))
    I.append(k)
plt.figure()
ax1 = plt.gca()
ax1.loglog(I, wynik, label='blad')
ax1.loglog(I, wynik2, label='$n^{-3}$')
ax1.legend()