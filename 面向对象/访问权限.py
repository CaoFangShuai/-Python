# -*-coding:utf-8-*-
'''
在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。

但是，从前面Student类的定义来看，外部代码还是可以自由地修改一个实例的name、score属性：
'''
class Student1(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def print_score(self):
        print("%s :%s"% (self.name,self.score))
bart1=Student1("cao","100")
bart1.name="fang"
bart1.print_score()#fang :100
'''
如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，
就变成了一个私有变量（private），只有内部可以访问，外部不能访问，所以，我们把Student类改一改：
'''

class Student2(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def print_score(self):
        print("%s :%s"% (self.__name,self.__score))
bart2=Student2("%s cao"%("私有变量在外部没有被改变"),"100")
# print bart2.__name#不可被访问
'''
这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。

但是如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法'''
class Student3(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self,score):
        if 0<= score <=100:
            self.__score=score
        else:
            raise ValueError("b0ad score")
bart3=Student3("cao",100)
print bart3.get_name()
print bart3._Student3__name
print bart3.set_score(20)
class gread(object):
    def __init__(self,name,gread):
        self.name=name
        self.__gread=gread
    def get_gread(self):
        return  self.__gread
    def set_gread(self,gread):
        if gread=="female" or gread=="male":
           self.__gread=gread
           return self.__gread
        else:
            return  "请正确输入性别"
gender=gread('cao','male')
print gender.get_gread()
print gender.set_gread('female')
print gender.get_gread()







