# -*- coding:utf-8 -*-
# print("草发明和所爱")
def qur(a,b,c):
	if a==0:
		return"无解"
	else:
		n=b**2-4*a*c
		if(n==0):
			x=-b/2*a
			return x
		elif n>0:
			x1=(-b-n)/2*a
			x2=(-b+n)/2*a
			return x1, x2
		else:
				return "无解"
print(qur(1,2,1))