# -*-coding:utf-8 -*-
'''
L=[x*x for x in range(10)] #list
G=(x*x for x in range(10)) #generator
print L
for x in G:
	print x
#斐波拉契数列用列表生成式 
def fib(max):
	n,a,b=0,0,1
	while n<max:
		print b
		a,b=b, a+b
		n=n+1
fib(10)
'''
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
print fib(10)
for x in fib(10):
	print x
def odd():
	print 'step 1'
	yield 1
	print 'step 2'
	yield 3
	print 'step 3'
	yield 5

o=odd()	
o.next()
o.next()
o.next()

