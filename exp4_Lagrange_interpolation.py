# coding=utf-8
'''
拉格朗日插值函数
'''
k = 3

x_list = [None] * k
y_list = [None] * k

l_list = [None] * k 
L = 0

x = 10 #所求y值对应的x值

x_list = [3,  6, 9]
y_list = [10, 8, 4]

l_list = [1] * k

for j in range(0,k):
	for i in range(0,k):
		if (i < j) or (i > j) :
			l_list[j] *= (x - x_list[i]) / (x_list[j] - x_list[i])
			
for j in range(0,k):
	L +=  y_list[j] * l_list[j]

print(L)
