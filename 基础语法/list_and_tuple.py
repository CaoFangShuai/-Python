# -*- coding: utf-8 -*-
#list -列表
classmates = ['Michael', 'Bob', 'Tracy']
# 在list最后添加一个元素
classmates.append("cao")  
# 在list指定位置添加一个元素
classmates.insert(1,"cao") 
# 删除最后一个元素
classmates.pop()
# 删除指定未知的元素
classmates.pop(1)
# 替换某个位置的元素
classmates[1] = 'Sarah'
classmates.append(123)
# 在最后添加一个对象
classmates1=["jone","yoouh"]
classmates.append(classmates1)
print(classmates)
print(len(classmates))
# tuple - 元组
#创建一个元组
#一旦定义里边的内容不变
t=("cao","guo","li")
#定义一个元素时候后后边得带,
t1=(1,)
#最后来看一个“可变的”tuple：
"""
表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list，
所以，tuple所谓的“不变”是说，tuple的每个元素，
指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
"""
t2=("cao","guo",["a","b"])
t2[2][0]="c"
t2[2].append("d")
print(t2)

# 作业
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])
