# -*-coding:utf-8-*-
print range(1,11)
print [x*x for x in range(1,11) if x % 2==0]
print [m+n for m in "ABC" for n in 'QWE' ]


# 练习
L = ['Hello', 'World', "18", 'Apple',"None"]
print  [s.lower() for s in L]
# a=[]
# for s in L:
# 	if isinstance(s,str):
# 		a=a.append([s.lower()])	
# print(a)		
# print [s.lower() for s in L if ]
