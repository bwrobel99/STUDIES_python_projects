# -*- coding: utf-8 -*-

import numpy as np
import scipy.optimize as so
import matplotlib.pyplot as plt
import numpy.linalg as nplin
import time

#1
def function1(x):
    return 2*np.exp(-x) - np.sin(x)

plt.figure()
X=np.linspace(1e-3,50,int(1e3))
plt.plot(X, function1(X))
plt.grid()
plt.show()

def find_bisect_root(f,a,b):    
    if (f(a)*f(b))>0:
        print('no root between {} and {}'.format(a, b))
        find_root(f, a+1, b+1)
    else:
        print('root between {} and {} exists'.format(a, b))
    root = so.bisect(f, a, b)
    return root

bisect_root = find_bisect_root(function1,0,1)
root_root = so.root(function1, 0.5)
fsolve_root = so.fsolve(function1, 0.5)
print('bisect root : {}'.format(bisect_root))
print('root root : {}'.format(root_root.x))
print('fsolve root : {}'.format(fsolve_root))

#2
def fcn2(x):
    return 1/((x - 0.3)**2 + 0.01) - 1/((x-0.8)**2 +0.04)

plt.figure()
X = np.linspace(1e-3,2,int(1e3))
plt.plot(X,fcn2(X))
plt.grid()
plt.show()

newton = so.newton(fcn2,0.5)
print("x0 = 0.5, newton:")
print(newton)

rootroot = so.root(fcn2,0.31) 
print("root: ")
print(rootroot.x)

fsolve = so.fsolve(fcn2,0.4)
print("fsolve: ")
print((fsolve[0]))

#3
from numpy.polynomial import polynomial as poly
polynomial_roots = np.linspace(1,20,20)
wsp = poly.polyfromroots(polynomial_roots)
N = 20

for i in range(1,N+1):
    rand_vec = 10**(-10)*np.random.random_sample((21,))
    new_wsp = wsp + rand_vec
    new_poly_roots = poly.polyroots(new_wsp)
    plt.plot(new_poly_roots.real,'o')
    
plt.show()