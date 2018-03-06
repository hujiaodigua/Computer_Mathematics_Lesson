import math

#此处三条边长由三点求得
a_x = float(input('输入a点的x坐标: '))
a_y = float(input('输入a点的y坐标: '))

b_x = float(input('输入b点的x坐标: '))
b_y = float(input('输入b点的y坐标: '))

c_x = float(input('输入c点的x坐标: '))
c_y = float(input('输入c点的y坐标: '))

#计算三条边长
ab = math.sqrt((a_x - b_x)*(a_x - b_x) + (a_y - b_y)*(a_y - b_y))
print("ab边长为 %f"%(ab))
bc = math.sqrt((b_x - c_x)*(b_x - c_x) + (b_y - c_y)*(b_y - c_y))
print("bc边长为 %f"%(bc))
ac = math.sqrt((a_x - c_x)*(a_x - c_x) + (a_y - c_y)*(a_y - c_y))
print("ac边长为 %f"%(ac))

#这里应该判断以下这三条边是否能够组成三角形
#利用两边和大于第三边且两边差小于第三边
if ((ab + bc > ac )& (ab + ac > bc) & (bc + ac > ab)):
	print('满足两边和大于第三边')
	if ((ab - bc < ac) & (ab - ac < bc) & (bc - ac < ab)):
		print('而且满足两边和小于第三边')
		print('可以计算面积')
		
		#ab = float(input('输入三角形第一边长: '))
		#bc = float(input('输入三角形第二边长: '))
		#ac = float(input('输入三角形第三边长: ')) 
		# 计算半周长
		s = (ab + bc + ac) / 2
		# 计算面积
		area = (s*(s-ab)*(s-bc)*(s-ac)) ** 0.5
		print('三角形面积为 %0.2f' %area)