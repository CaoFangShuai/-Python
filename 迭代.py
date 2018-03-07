# -*-coding:utf-8-*-
d={'a':1,'b':2,'c':3}
for value in d.itervalues():
	print(value)
for v,k in d.iteritems():
	print k,v
	# print(v)
from collections import Iterable
b1=isinstance('abc', Iterable) # str是否可迭代	
b2=isinstance([1,2,3], Iterable) # list是否可迭代
b3=isinstance(123,Iterable)#整数是否可迭代
print(b1)
print(b2)
print(b3)

for i, value in enumerate(['A', 'B', 'C']):
	print i, value
for x, y,z in [(1, 1,1), (2, 4,2), (3, 9,1)]:
    print x, y,z
	