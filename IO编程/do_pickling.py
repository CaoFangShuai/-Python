# -*- coding: utf-8 -*-
"""
Created on Wed May 23 16:40:51 2018

@author: Administrator
"""
#  序列化与反序列化
import pickle
d = dict(name='Bob', age=20, score=88)


for key, value in d.items():   # 方法五  
    print(key, '=>', value )
    
print(pickle.dumps(d))
with open("../../-Python/IO编程/dump.txt","wb") as f:
    f.write(pickle.dumps(d))
with open("../../-Python/IO编程/dump.txt",'rb') as f:
    d=pickle.load(f)
print(d)
