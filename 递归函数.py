# -*-coding:utf-8 -*-
'''
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(n, a, b, c)
        move(n-1, b, a, c)

move(2, 'A', 'B', 'C')	
'''
# 去掉字符串首尾的空格
def trim(str):
	if str[:1]=="":
		str=str[1:]
		
	elif str[-1]=="" :
		str=str[-2:]
	else:
		str=str
	return str	
print(trim("saddasd"))			
