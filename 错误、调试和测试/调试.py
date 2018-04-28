# -*- coding: utf-8 -*-
#import logging
import json
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)
print(type(s))






#j b  son.dumps()接受一个必须参数（如dict），结果是str
#json.dump()接受两个必须参数，第一个如dict，第二个是类文件名
#json.dumps()和dump序列化对象时用 default=lambda obj: obj.dict
#json.loads()接受一个必需参数，把json变为如dict，
#json.load()接受一个必需参数（类文件名），把类文件中的json变为如dict
#json.loads()和load反序列化json（对象）时需要object_hook=参数