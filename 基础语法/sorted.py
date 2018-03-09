# -*-coding:utf-8 -*-
# Python内置的sorted()函数就可以对list进行排序
print sorted([36, 5, -12, 9, -21])

# 此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
print  sorted([36, 5, -12, 9, -21], key=abs)

# 详解sorted
'''
sorted 语法：

sorted(iterable[, cmp[, key[, reverse]]])
参数说明：

iterable -- 可迭代对象。
cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。
key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。
'''
a = [5,7,6,3,4,1,2]
b = sorted(a)       # 保留原列表
print a 
# [5, 7, 6, 3, 4, 1, 2]
print b
# [1, 2, 3, 4, 5, 6, 7]
 
L=[('b',2),('a',1),('c',3),('d',4)]
print sorted(L, cmp=lambda x,y:cmp(x[1],y[1]))   # 利用cmp函数
# [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
print sorted(L, key=lambda x:x[1])               # 利用key
# [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
 
 
students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
print sorted(students, key=lambda s: s[2])            # 按年龄排序
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
 
print sorted(students, key=lambda s: s[2], reverse=True)       # 按降序
# [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
print sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower,reverse=True)
# 假设我们用一组tuple表示学生名字和成绩：

L1 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序：
print sorted(L1,key=lambda s:s[1],reverse=True) #倒序
print sorted(L1,key=lambda s:s[1]) #正序
