# -*-coding:utf-8 -*-
print type(int("12121"))
print int('123431313165', base=16)
print int('101010101010010101', base=2)
def int2(x, base=2):
    return int(x, base)
print int("0122")
# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
import functools
int3=functools.partial(int, base=2)
print int3('1000000000000000')
"""
所以，简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。

注意到上面的新的int2函数，仅仅是把base参数重新设定默认值为2，但也可以在函数调用时传入其他值：
"""
print int3("10000000000",base=16)
# 最后，创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数，当传入：
int4= functools.partial(int, base=2)
# 实际上固定了int()函数的关键字参数base，也就是：
int4('10010')
# 相当于：
kw = { 'base': 2 }
print int4('10010', **kw)
# 当传入：
max2 = functools.partial(max, 10)

# 实际上会把10作为*args的一部分自动加到左边，也就是：

print max2(2,3,2,5)
# 相当于：
args = (10, 5, 6, 7)
print max2(*args)
# 结果为10。

import functools

def www(x,r,z):
    y=x+r+z
    return y 

# www1=functools.partial(www)

kw=(5,2,4)
a=www(*kw)
print(a)


