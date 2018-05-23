# -*- coding: utf-8 -*-
"""
Created on Wed May 23 17:05:20 2018

@author: Administrator
"""

# =============================================================================
#JSON

# =============================================================================
# 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更
#好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，
#也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。
# 
# JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下： 
# =============================================================================
# =============================================================================
'''
JSON类型	      Python类型
{}                  dict
[]	                list
"string"	          str
1234.56	        int或float
true/false        True/False
null	             None
'''
import json
d=dict(name="cao",score=100,age='男')
print(json.dumps(d))

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score




s = Student('Bob', 20, '男')

def student2dict(std):
    return {
            'name':std.name,
            'score':std.score,
            'age':std.age
            }
    
print(json.dumps(s,default=student2dict))


obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)
print(s)