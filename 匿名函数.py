# -*-coding:utf-8 -*-
"""
当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。

在Python中，对匿名函数提供了有限支持。还是以map()函数为例，计算f(x)=x2时，除了定义一个f(x)的函数外，还可以直接传入匿名函数：

"""
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print list(reduce(lambda x, y: x * 10 + y,[1, 2, 3, 4, 5, 6, 7, 8, 9])) 
"""
练习
请用匿名函数改造下面的代码：
"""
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
print(L)
L1 =  list(filter(lambda x: x%2==1, range(1, 20)))

print list(filter(lambda n:n%2==1,range(1,20)))
print L1
