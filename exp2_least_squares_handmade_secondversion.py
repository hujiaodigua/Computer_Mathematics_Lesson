# coding=utf-8

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
matA = []
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
    matA.append(matA1)

print("输入xi的长度为：%d" % len(xi))
print("输入yi的长度为：%d" % len(yi))
print("输入xi为：", xi)
print("输入yi为：", yi)

matA = np.array(matA)   #手动计算出的系数放在数组matA中，这里将其矩阵化，方便后面求解方程组

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

matAA = np.linalg.solve(matA, matB)

# 画出拟合后的曲线
# print(matAA)
print("拟合后得到系数矩阵为", matAA)
Xi = np.arange(0, 145, 0.1)
Yi = []
for i in range(0, len(Xi)):
    yy = 0.0
    for j in range(0, N + 1):
        dy = 1.0
        for k in range(0, j):
            dy *= Xi[i]
        dy *= matAA[j]
        yy += dy
    Yi.append(yy)
ax.plot(Xi, Yi, color='r', linestyle='-', marker='')
ax.legend()
plt.show()  