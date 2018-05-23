# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 09:59:27 2018

@author: Administrator
"""

from io import StringIO
from io import BytesIO
# StringIO

# 写入
f=StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())
# 读取
s=StringIO("Hello!\nHi!\nGoodbye!")
while True:
    a=s.readline()
    if a=='':
        break
    print(a.strip())


# BytesIO
#  读取
g=BytesIO()
g.write('中文'.encode('utf-8'))
print(g.getvalue())


# 写入
h=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(h.read())
