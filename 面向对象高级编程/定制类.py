# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-04-25 09:46:39
# @Last Modified by:   Administrator
# @Last Modified time: 2018-04-25 13:04:44
# -*- coding: utf-8 -*-
class student(object):
    def __init__(self,name):
        self.name=name
        
print(student('cao'))

class student_1(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'student object (name :%s)' % self.name
    __repr__=__str__
print(student_1('cao'))
s=student_1('fang')
print(s)


#如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

#我们以斐波那契数列为例，写一个Fib类，可
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1 #初始化两个变量
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>1000:
            raise StopIteration()
        return self.a
 
#__getitem__
#Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
class Fib1(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a    
f=Fib1 ()
print(f[0])
class Fib2(object):
     def __getitem__(self,n):
         if isinstance(n,int):
             a,b=1,1
             for x in range(n):
                 a,b=b,a+b
             return a
         if isinstance(n,slice):
             start=n.start
             stop=n.stop
             if start is None:
                 start=0
             a,b=1,1
             L=[]
             for x in range(stop):
                 if x>start:
                     L.append(a)
                 a,b=b,a+b
             return L
f2=Fib2()
print(f2[0:10])
#__getattr__
#
#正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。比如定义Student类：
class student2(object):
    def __init__(self,name):
        self.name=name

s2=student2('cao')
print(s2.name)
#print(s2.score)        #'student2' object has no attribute 'score'
#错误信息很清楚地告诉我们，没有找到score这个attribute。
#
#要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。修改如下：
class student3(object):
    def __init__(self,name):
        self.name=name
    def __getattr__(self, attr):
        if attr=='score':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
s3=student3('cao')
print(s3.name)
print(s3.score())  


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__
print(Chain('asds').status)
class chain_1(object):
    
    def __init__(self,path=''):
        
        self._path=path
        
    def __call__(self,path):
        
        return chain_1('%s/%s' % (self._path,path))
    
    def __getattr__(self,item):
        
        return chain_1('%s/%s' % (self._path,item))
    
    def __str__(self):
        
        return self._path
    
    __repr__ = __str__

print(chain_1().users('michael').repos)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    