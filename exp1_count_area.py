# -*- coding: UTF-8 -*-

import numpy as np
import math

'''
思考matlab绘制函数图像时候，首先会把x坐标离散化，然后求对应的y坐标，
说明:
	(1)计算机并不能绘制连续图像（连续图像的点数是无穷，计算机的寄存器也好存储空间也好都是有限的）;
	(2)还说明一点，录入的坐标仍然是离散，那得到的图形自然还是多边形了，毕竟有限个点怎么画都是折线;
	(3)用梯形积分法也好，三点五点积分法也好，或者下面的转换成多个和原点围城的三角形，其实本质差别不是很大
	(4)我不会写C++,只会写嵌入式C，C++ 程序请参考守枫竹清博客http://blog.csdn.net/ycl295644/article/details/48368639
	
注意:
	(1)为了能够验证程序准确性除去简单不规则区域外，使用matlab生成一组在0到pi范围内由sin(x)与0.5*sin(x)围成
	   图形所得数据保存在.txt文件内
	(2)matlab下生成数据代码如下: 
	   x1 = 0:0.001*pi:1*pi; 
	   y1 = sin(x1);
       x2 = 0:0.001*pi:1*pi; 
	   y2 = 0.5*sin(x2);
		
作者:李易 
日期:20180312
'''
 
# mat1 = np.array([ [1,2]
#                 , [3,4] ])
#
# mat2 = np.array([ [1,0]
#                 , [0,1] ])
#
# mat3 = np.linalg.det(mat1) + np.linalg.det(mat2)
# print(mat3)

#x = [1,1,2,3,4,4,3,2]
#y = [2,3,4,4,3,2,1,1]

#读入x坐标
result = []
with open('yueya_x.txt','r') as f:
    for line in f:
        result.append(list(map(float,line.split(','))))

#读入y坐标
x = []		
for k in range(0, len(result) - 1):
	x.append(result[k][0])


result.clear()	
with open('yueya_y.txt','r') as f:
    for line in f:
        result.append(list(map(float,line.split(','))))
		
y = []		
for k in range(0, len(result) - 1):
	y.append(result[k][0])



print("x坐标个数为：%d" % len(x))
print("y坐标个数为：%d" % len(y))
	
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

print("计算结果保留6位有效数字为：%f" % S)