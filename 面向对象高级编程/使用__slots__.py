# -*- coding: utf-8 -*-
'''
使用__slots__

阅读: 225449
正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：
'''
class Student(object):
    pass
s=Student();
s.name="cao"
print(s.name)
def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age, s) #给实例绑定一个方法
s.set_age(25) # 调用实例方法
print(s.age) 
#递归函数
def fetch(n):
    if n==1:
        return 1
    else:
        return n*fetch(n-1)
print(fetch(5))    

print((1,))
s = set([10,1,1, 2,3])
print(s)
a='abc'
b=a.replace('a',"A")
print(a,b)
L=list(range(100))
print(L)
print(L[::2])
s=" a "
print(len(s[1:]))
def trim(str):
    print(str)
    if(str[0]==' '):
        n=str[1:]
        if(n[-1]==' '):
            n=str[-1:]
            return n
str1=trim(" a ")

print(len(str1))    

#请使用迭代查找一个list中最小和最大值，并返回一个tuple：

def findMinAndMax(list):
    if len(list)==0:
        return (None,None)   
    min=list[0]
    max=list[0]
    for v in list:
        if v <min:
            min=v
        elif v>max:
            max=v
    return (min,max)        
print(findMinAndMax([-100,5,857,174,44]))
#列表生成式
A=[m+n+z for m in "ABC" for n in "XYZ" for z in "QWE"]
print(A)
import os # 导入os模块，模块的概念后面讲到
B=[d for d in os.listdir('.')] # os.listdir可以列出文件和目录
print(B)
#L2 = [x.lower() for x in L1 if isinstance(x,str)]
#如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[x.lower() for x in L1 if isinstance(x,str)]
print(L2)
#斐波拉契数列用列表生成式写不出来

def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        
        b=a + b
        a = b
        n = n + 1
    return 'done'
fib1(6)
# =============================================================================
# 要把fib函数变成generator，只需要把print(b)改为yield b就可以了
# =============================================================================

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
for x in fib(10):
    print(x)
'''
杨辉三角定义如下：

          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
'''

def triangles(n):
    L3=[1];
    while len(L3)<n:
        yield L3
        L3=[ L3[x]+L3[x+1] for x in range(len(L3)-1)]
        L3.insert(0,1)
        L3.append(1)
for m in triangles(7):
    print(m)

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    def capital(str):
        return str.capitalize()
    return list(map(capital, name))
print(normalize(['adam', 'LISA', 'barT']))
#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
from functools import reduce
def prod(L4):
    def redu(x,y):
        return x*y
    return reduce(redu,L4)
print(prod([1,5,6]))
#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    a=int(s.split('.')[0])#整数部分
    b=int(s.split('.')[1])*pow(10,-len(s.split('.')[1]))#小数部分
    return a+b
print(list(map(str2float,['124.415','45.25'])))
print(list(map(lambda s : int(s.split('.')[0]) + int(s.split('.')[1]) * pow(10,-len(s.split('.')[1])),['123.456','345.234'])))    
          
#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
    n=str(n)  
    if len(n) % 2==0:
        return False
    else:
        m=1
        while int((len(n)-1)/2)>=m:
            if n[0:m]==n[-1:-(m+1)]:
                m=m+1
                return n

print(list(filter(is_palindrome,[123,5454,45654])))

