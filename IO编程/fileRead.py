# -*- coding: utf-8 -*-
with open('../../-Python/test.txt','r',encoding='utf-8') as f:
    for line in f.readline():
        print(line)
with open('../../-Python/test.txt','a',encoding='utf-8') as f:
        f.write('张珊')
with open('../../-Python/my.ini','r') as f:
    print(f.read())
