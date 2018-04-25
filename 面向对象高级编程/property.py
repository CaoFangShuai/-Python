# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-04-18 14:26:24
# @Last Modified by:   Administrator
# @Last Modified time: 2018-04-25 13:04:01
# -*- coding: utf-8 -*-

class Screen(object):
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,value):
        self.__width=value
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,value): 
        self.__height=value
    @property
    def resolution(self):
        return self.__height * self.__width
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

'''
class Screen(object):
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def resolution(self):
        return self.__height * self.__width
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
'''

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)




from enum import Enum, unique

@unique
class Gender(Enum):
    Male = 0 # Sun的value被设定为0
    Female = 1
class Student1(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

print(Gender.Male)
bart = Student1('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')

























