# -*- coding: utf-8 -*-
#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：


def is_palindrome1(n):
    return    str(n) == str(n)[::-1]
print(list(filter(is_palindrome1,[123,5454,45654])))
#sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数。
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    print(t)
    return str.lower(t[0])
L2 = sorted(L, key=by_name)

print(L2)
def by_score(t):
    return t[1]

L3 = sorted(L, key=by_score)

print(L3)


#利用闭包返回一个计数器函数，每次调用它返回递增整数：

def createCounter():
    n=0
    def counter():
        nonlocal n
        n=n+1
        return n
    return counter
#print(createCounter()()())
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())
''' 
nonlocal与global区别：
nonlocal 用于调用函数或者作用域【外层】变量
global 用于调用【全局】变量，在函数调用变量后，若变量值改变则全局的变量值也会改变。
'''
#请用匿名函数(lambda )改造下面的代码：

def is_odd(n):
    return n % 2 == 1

L3 = list(filter(is_odd, range(1, 20)))
print(L3)

L4=list(filter(lambda x:x % 2==1,range(1,20)))
print(L4)


class Student(object):
    def __init__(self,name):
        self.name = name
    def set_score(self,score):
        self.score=score

s1=Student('曹芳帅')
print(s1.set_score(10))

class Student1(object):
    """docstring for Student"""
    def __init__(self, name, score):
        # super(Student, self).__init__()
        self.name = name
        self.score = score
    def print_score(self):
        return('%s: %s' % (self.name, self.score))
        
s2=Student1("曹芳帅",100)
print(s2.print_score())








