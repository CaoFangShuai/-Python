# -*- coding:utf-8 -*-
# 循环
#for...in
names=["cao","guo","zhang"]
for name in names:
	print(name)
# for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句。
sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
	sum=sum+x
print(sum)
# range() 可以生成一个整数序列，再通过list()函数可以转换为list。list(range(101))产生1到100的列表
# print(list(range(101)))
list=list(range(101))
sum1=0
for x in list:
	sum1=sum1+x
print(sum1)

# while 循环
sum2=0
n=100
while n>0:
	sum2=sum2+n
	n=n-1
print(sum2)	
"""
练习
请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Bart', 'Lisa', 'Adam']
"""
L = ['Bart', 'Lisa', 'Adam']
n=0
while n<len(L):
	print("hello,%s" % L[n])
	print("hello,"+L[n])
	n=n+1
# break 跳出循环
n=0
while n<100:
	n=n+1
	print(n)
	if n>20:
		print("end")
		break

# continue 跳出档次循环 执行下次循环
a=0
while a<100:
	a=a+1
	if(a%2==0):
		print("这是偶数%s"% a)
	else:
		print("这是奇数%s"% a )

#死循环
i=0
while i>0:
	i=i+1
print(i)		
	
	