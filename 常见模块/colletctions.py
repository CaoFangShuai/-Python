#-*-coding:utf-8-*-
# print("曹芳帅")
from collections import namedtuple,deque,defaultdict
Point=namedtuple('Piont',['X','Y'])
P=Point(1,2)
print(P)
print(P.X)
print(isinstance(P,Point))#P是Point的子类
Circle=namedtuple("circle",['x','y','r'])
s=('cao',[1,13,3])
print(s)


q=deque(['a','b','c'])
q.append('x')
print(q)
dd=defaultdict(lambda:'N/A')
dd['key']='abc'
print(dd['key2'])
