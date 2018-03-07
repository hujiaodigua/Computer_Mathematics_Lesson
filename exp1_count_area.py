import numpy as np
import math
 
'''
思考matlab绘制函数图像时候，首先会把x坐标离散化，然后求对应的y坐标，
说明计算机并不能绘制连续图像（连续图像的点数是无穷，计算机的寄存器也好存储空间也好都是有限的）;
还说明一点，录入的坐标仍然是离散，那得到的图形自然还是多边形了，毕竟有限个点怎么画都是折线;
那用梯形积分法也好，三点五点积分法也好，或者下面的转换成多个和原点围城的三角形，其实本质差别不是很大
'''
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
