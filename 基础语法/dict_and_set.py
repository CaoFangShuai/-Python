# -*-coding:utf-8 -*-
d={"cao":95,"guo":50,"li":50}
d["ca"]=100
print("cao" in d) #检测这个dict中是否有这个key
print(d["ca"])
print(d.get("ca"))#get()方法，如果key不存在，可以返回None，或者自己指定的value
d.pop("ca")
print(d)
#set
# 创建
l=[1,2,4,1]#重复元素在set中自动被过滤：
s=set(l)
s.add(10)#add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s.remove(10)#通过remove(key)方法可以删除元素：
print(s)
#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1=set([1,2,2,3])
s2=set([1,4,0.5])
print(s1&s2)
print(s1|s2)
# 再议不可变对象
a=['a','c','d','b']
a.sort()#通过sort()函数进行排序
print(a)
b="ABC"
c=b.replace("A","a")
print(c) #aBC
print(b) #ABC 虽然通过replace()方法，也确实变出了'Abc'，但变量a最后仍是'abc'
mm={"a":("aa",2,1),"b":(1,[2,3])}
# mm["a"][1]=3
print(mm)
nn=set([("aa",2,1)])
print(nn)