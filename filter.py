# filter.py
# -*-coding:utf-8 -*-
# 
def a(n):
	return n%2==0
print list(filter(a,[1,2,3,4,5,4,8,7,8,9,15]))

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数

def p(s):
	def is_palindrome(n): 
		a = str(n) 
		return a == a[::-1]
	return list(filter(is_palindrome,s))	
print(p([121,15,12321,15651]))	

