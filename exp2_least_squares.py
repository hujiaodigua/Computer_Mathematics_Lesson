# coding=utf-8
'''
最小二乘手工编写求解
说明：
    （1）脚本程序参考 CSDN上 Jairus Chan 博客
    （2）假设拟合结果为多项式形式

        y = a0+a1x+...ak*x^k 对其ai求编导

        化简后有如下X*A=Y，那么A = (X'*X)-1*X'*Y，便得到了系数矩阵A

        |1 x1 ... x1^k|    |a0|   |y1|
        |1 x2 ... x1^k| *  |a1| = |y2|
        |: :   :     :|    | :|   | :|
        |1 xn ... xn^k|    |ak|   |yn|

        所以最小二乘拟合的过程实际上就是反解系数矩阵的过程

注意：
    （1）数据为老师教案中数据
    （2）代码第31行变量N 为拟合多项式阶数
	
作者：李易
日期：20180326
'''

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)

# 阶数为2阶,多项式最高次项次数为2
N = 2

xi = np.array([32, 40, 48, 56, 64, 72, 81, 89, 97, 105, 113, 121, 129])
yi = np.array([12.5, 17, 22.5, 28, 35.5, 43.5, 53, 64, 76, 89.5, 104.5, 122.5, 141.5])

ax.plot(xi, yi, color='b', linestyle='', marker='.')

# 进行曲线拟合
mat_A = []
for i in range(0, N + 1):
    matA1 = []
    for j in range(0, N + 1):
        tx = 0.0
        for k in range(0, len(xi)):
            dx = 1.0
            for l in range(0, j + i):
                dx = dx * xi[k]
            tx += dx
        matA1.append(tx)
    mat_A.append(matA1)

print("输入xi的长度为：%d" % len(xi))
print("输入yi的长度为：%d" % len(yi))
print("输入xi为：", xi)
print("输入yi为：", yi)

mat_A = np.array(mat_A)   #手动计算出的系数放在数组matA中，这里将其矩阵化，方便后面求解方程组

matB = []
for i in range(0, N + 1):
    ty = 0.0
    for k in range(0, len(xi)):
        dy = 1.0
        for l in range(0, i):
            dy = dy * xi[k]
        ty += yi[k] * dy
    matB.append(ty)

matB = np.array(matB)

mat_a = np.linalg.solve(mat_A, matB)

# 输出拟合后的结果
print("拟合后得到系数矩阵为", mat_a)
print("拟合后得到的表达式为: y=%fx^2+(%f)x+%f" % (mat_a[2], mat_a[1], mat_a[0]))
Xi = np.arange(0, 145, 0.1)
Yi = []
for i in range(0, len(Xi)):
    yy = 0.0
    for j in range(0, N + 1):
        dy = 1.0
        for k in range(0, j):
            dy *= Xi[i]
        dy *= mat_a[j]
        yy += dy
    Yi.append(yy)

# 画出拟合后的曲线
ax.plot(Xi, Yi, color='r', linestyle='-', marker='')
ax.legend()
plt.show()