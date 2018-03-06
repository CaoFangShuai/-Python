# -*- coding:utf-8 -*-
"""
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
"""
age=20
if age<3:
	print("big")
elif 3<age<=20:
	print("keyi")
else:
	print("very good")	
s=input("你的出生年份:")
s=int(s)
if s>2000:
	print("00后")
else:
	print("00前")	



#练习
'''
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
用if-elif判断并打印结果：
'''
h=1.75
w=80.5
r=w/(h*100)
print(r)
r=r**2
print(r)
if r<18.5:
	print("过轻")
elif 18.5 <=r<25:
	print("正常")
elif 25<= r<32:
	print("肥胖")
else:
	print("严重肥胖")			
