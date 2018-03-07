# -*-coding:utf-8 -*-
"""
函数作为返回值
高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

我们来实现一个可变参数的求和。通常情况下，求和的函数是这样定义的：
"""
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
L=(12412,1354,4563)
print calc_sum(*L)
# 函数作为返回值
def lazy_sum(*args):
	def calc_sum():
	    ax = 0
	    for n in args:
	        ax = ax + n
	    return ax
	return calc_sum
print lazy_sum(*L)()	    
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print f1==f2
# 请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
# f1()和f2()的调用结果互不影响。
# False
'''
注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，
其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。
另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。我们来看一个例子：
'''
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
f1,f2,f3=count()
"""
在上面的例子中，每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了。
你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际结果是：
>>> f1()
9
>>> f2()
9
>>> f3()
9
全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
"""

print f1(),f2() ,f3()
def a():
	l=[]
	a=1
	for i in range(1,4):
		a=a*i
		l.append(a)
	return l 
print a()		
def a():
	def b(i):
		def c():
			return i*i
		return c
	# a=lambda i:i*i
	d=[]
	for i in xrange(1,4):
		d.append(b(i))
	return d		
a1,a2,a3=a()
print a1(),a2(),a3()	
# 练习
# 利用闭包返回一个计数器函数，每次调用它返回递增整数：

def counting():
	num=[0]
	def num_f():
		num[0]=num[0]+1
		return num[0]
	return 	num_f
g2=counting()	


print g2(), g2()
# print counting()

# num=[0]
# def num_f():
# 	num[0]=num[0]+1
# 	return num
# print num_f()	