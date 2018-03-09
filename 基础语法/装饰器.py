# -*-coding:utf-8 -*-
# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
def now():
	print('2015-3-25')
f=now
f()	
# 函数对象有一个__name__属性，可以拿到函数的名字：
print f.__name__
print now.__name__
# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
# 但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
	print(2)
print now()	   
print ("asd",log(now))
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log('execute')
def now():
    print('2015-3-25')    

"""
我们来剖析上面的语句，首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。

以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，它有__name__等属性，
但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：
"""
print now()    
now = log('execute')(now)
print  now.__name__
# wrapper
"""
因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。

不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：
"""
import functools

def log1(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log1
def now():
    print('2015-3-25')      
print now()    
print now.__name__

# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import time, functools
# time.struct_time(tm_year=2018, tm_mon=3, tm_mday=7, tm_hour=15, tm_min=50, tm_sec=24, tm_wday=2, tm_yday=66, tm_isdst=0)

# print (time.tm_year,time.tm_mon,time.tm_mday,time.tm_hour,time.tm_min,time.tm_sec)

'''
def metric(fn):
#    @functools.wraps(fn)
    def wrapper(*args, **kw):
        t0 = time.time()
        y = fn(*args, **kw)
        print('%s executed in %s ms' % (fn.__name__, time.time()-t0))
        return y
    return wrapper
'''


'''
def time(func):
	# @functools.wraps(func)
	def wrapper(*args, **kw):
 		t2=time.localtime()
		t=t2.tm_year%s t2.tm_mon %s t2.tm_mday %s t2.tm_hour %s t2.tm_min %s t2.tm_sec %s %("年","月","日","时","分","秒")
		print('%s executed in %s ms' % (func.__name__, t))
		return func(*args,**kw)
	return wrapper	
'''
def metric(fn):
   # @functools.wraps(fn)
    def wrapper(*args, **kw):
        t0 = time.time()
        y = fn(*args, **kw)
        print('%s executed in %s ms' % (fn.__name__, time.time()-t0))
        return y
    return wrapper
	
@metric	
def now():
    # print('2015-3-25') 
    l=[]
    for x in xrange(1,1000):
    	l.append(x)
    return l	
print(now())    