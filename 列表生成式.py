# -*-coding:utf-8 -*-
print [x*x for x in range(1,11)]
print [m + n for m in 'ABC' for n in 'QWE'] 
print [m + n for m in 'ABC' for n in 'XYZ']
import os # 导入os模块，模块的概念后面讲到
print [d for d in os.listdir('.')] # os.listdir可以列出文件和目录

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print [k+'='+v for k,v in d.iteritems()]