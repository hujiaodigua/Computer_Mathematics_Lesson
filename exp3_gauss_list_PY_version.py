# coding=utf-8
'''
Gauss列主元消去法手工编写求解
说明:
    (1) 脚本程序参考老师 C++代码与CSDN上 WUST_陈迪洋 博客中C语言代码
    (2) 程序与自己动手进行高斯顺去消元并无太大差异

注意:
    (1) 程序最开始的list变量定义不是很规范,不过利用 [None]*3 定义指定维数的list 比用循环中使用
        list.append 塞入一个一个的 None 书写起来简洁很多
    (2) A 矩阵最终会化成一个上三角阵，b 也会在增广矩阵中被化为相应的矩阵

作者：李易
日期：20180406
'''
import os, sys

eps = 0
x = [None]*3 #这里这种变量定义其实非常不规范
a = [None]*3
b = []

with open("gauss_source.txt",'r') as data:
    line = data.readlines()
    line_0st = line[0] #第一行维数
    line_1st = line[1]
    line_2st = line[2]
    line_3st = line[3]
    line_4st = line[4]
    line_5st = line[5]

n   = list(map(int,  line[0].split(' ')))[0] #使用list的split方法以空格划分利用下标读入变量中
a[0]= list(map(float,line[1].split(' ')))    #以空格划分读入list中，a[0]又是一个list，所以a其实是二维list
a[1]= list(map(float,line[2].split(' ')))
a[2]= list(map(float,line[3].split(' ')))
b   = list(map(float,line[4].split(' ')))
eps = list(map(float,line[5].split(' ')))[0]

print("读入变量维数n:%d" % n)
print("读入A矩阵:")
print(a[0])
print(a[1])
print(a[2])
print("读入B矩阵:")
print(b)

'''
a = [[2,  1, 2],
     [4,  5, 4],
     [6, -3, 5]]
b = [6,  18, 5]
n = 3
'''

# GaussList_eiminate
for i in range(0, n - 1): ##########
    #找主元素
    for j in range(i+1, n): ##########
        mi = i
        mx = abs(a[i][i])
        if abs(a[j][i]) > mx :
            mi = j
            mx = abs(a[j][i])
        #交换两行
        if i < mi :
            tmp = b[i]
            b[i] = b[mi]
            b[mi] = tmp
            for j in range(i, n):    ##########
                tmp = a[i][j]
                a[i][j] = a[mi][j]
                a[mi][j] = tmp
    #高斯消元
    for j in range(i+1, n):
        if abs(a[i][i]) < eps:
            print("主元素太小，求解失败")
            os._exit(0)
        tmp = - a[j][i]/a[i][i]
        b[j] += b[i] * tmp
        for k in range(i,n):
            a[j][k] += a[i][k] * tmp
            #print("运行到这里了！！！")

# GaussList_solution
#a[][]到这里被化成上三角矩阵了
#求解方程
x[n - 1] = b[n - 1] / a[n - 1][n - 1]
for i in range(n - 2, -1, -1):
    sum = 0.0
    #print("变量i:%d\n" % i)
    for j in range(i+1, n):
        #print("变量j:%d\n" % j)
        sum += a[i][j] * x[j]
        #print("运行到这里了！！！")
    x[i] = (b[i]- sum) / a[i][i]

# GaussList_output
print("solution is :\n")
for i in range(0, n):
    print("%f\n" % x[i])

x_out = []
for i in range(0,len(x)):
    x_out.append(str(x[i]))

#print(x_out)
s = ' '.join(x_out)  #以空格划分三个输出变量
with open("gauss_result.txt","w") as z:
    z.write(s)
print("已输出到文件中")