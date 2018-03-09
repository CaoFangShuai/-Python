# -*- coding-utf-8 -*-
def power(x,n=2):
	s=1
	if n==2:
		return x*x
	else:
		while n>0:
			n=n-1
			s=s*x
		return s
print(power(5))	
def add_end(l=[]):
	l.append('end')
	return l
print(add_end())
print(add_end())	
def add_end1(l=None):
	if l ==None:
		return
	else:
		l=[]
		l.append("end")
print(add_end1())	
print(add_end1())	
print(add_end1())



def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
nums=[1,2,3]   
print(calc(*nums))    



def person(name,age,**kw):
	print('name:', name, 'age:', age, 'other:', kw)
print(person("Michael",30))
print(person('Bob', 35, city='Beijing'))
# name: Bob age: 35 other: {'city': 'Beijing'}
print(person('Adam', 45, gender='M', job='Engineer'))
# name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person("Jack",200,**extra))

def product(*list):
	s=1
	for n in list:
		s=s * n
	return s	
a=[1,2,.1,2,5,5,5,5,5,5,5,5,5,5,5]	
print(product(*a))	    





















