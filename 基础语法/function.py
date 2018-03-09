# -*- coding:utf-8 -*-
# help(abs)
a=-10
print(abs(a))
# 练习
'''
请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
n1 = 255
n2 = 1000
'''
n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))

#定义函数
def my_abs(x):
	if x>=0:
		return x
	else:
		return -x
print(my_abs(-10))		

# 返回多个值
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
# print(move(1,1,1))
# print('%2d-%02d' % (3, 1))
# print('%.2f' % 3.1415926)

"""
练习
请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：

ax2 + bx + c = 0

的两个解。

提示：计算平方根可以调用math.sqrt()函数：
>>> import math
>>> math.sqrt(2)
1.4142135623730951

"""

# print("100的16进制是"+hex(100))

def quad(a,b,c):
	if a ==0:
		# print("无解")
		return "无解"	
	else:
		n=b**2-4*a*c
		if n==0:
			x= -b/2*a
			return "有且只有一个根x=%2f" %x
		elif n<0:
			return "无解"	
		else:
			
			return 	"有两个根x1= %f,x2= %f" %((-b+math.sqrt(n))/2*a, (-b-math.sqrt(n))/2*a)
		# print()		
			
x=quad(1,2,1)		
print(x)

# quad(0,2,1)