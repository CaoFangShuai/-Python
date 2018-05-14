# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 09:59:27 2018

@author: Administrator
"""

from io import StringIO


f=StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())

