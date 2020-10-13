# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as nplin
import time
from scipy.sparse.linalg import gmres, cg

A = np.zeros((100, 100))
np.fill_diagonal(A, 4)
np.fill_diagonal(A[1:],1)
np.fill_diagonal(A[:,1:],1)
np.fill_diagonal(A[4:],1)
np.fill_diagonal(A[:,4:],1)

b = np.matrix(np.ones((100, 1)))
x = np.matrix(np.ones((100, 1)))

cg_times = []
gmres_times = []

#cg
for i in range(100):
    start_time = time.time()
    cg_result = cg(A,b, x0=x)
    elapsed = time.time() - start_time
    cg_times.append(elapsed)
    
#gmres
for i in range(100):
    start_time_ = time.time()
    gmres_result = gmres(A,b, x0=x)
    elapsed_ = time.time() - start_time_
    gmres_times.append(elapsed_)
    
avg_cg_time = np.mean(cg_times)
avg_gmres_time = np.mean(gmres_times)

print('average cg time: {} \n'.format(avg_cg_time))
print('average gmres time: {} \n'.format(avg_gmres_time))