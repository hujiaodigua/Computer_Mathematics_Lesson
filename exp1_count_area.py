import numpy as np
import math

# mat1 = np.array([ [1,2]
#                 , [3,4] ])
#
# mat2 = np.array([ [1,0]
#                 , [0,1] ])
#
# mat3 = np.linalg.det(mat1) + np.linalg.det(mat2)
# print(mat3)

x = [1,1,2,3,4,4,3,2]
y = [2,3,4,4,3,2,1,1]
S = 0

if(len(x)-len(y) == 0):
    n = len(x) - 1 #注意list的下标是从0开始和matlab别搞混
    for i in range(2,n):
        m = np.array([ [x[i -1],y[i - 1]],
                       [x[i]   ,y[i]]     ])
        S = S + np.linalg.det(m)
    S = S + np.linalg.det(np.array([ [x[n],y[n]],
                                     [x[1],y[1]] ]))

S = S / 2
if(S < 0):
    S = -S;

print(S)