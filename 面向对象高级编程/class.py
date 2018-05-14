# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender
    def get_name(self):
        return self.__name
    def get_gender(self):
        return self.__gender
    def set_name(self,name):
        self.__name=name
    def set_gender(self,gender):
         if gender>0:
             self.__gender=gender

S=Student("cao",10)
print(S._Student__name)
S.set_name('fan')
S.set_gender(-41)

print(S.get_gender())


#继承和多态
class Animal(object):
    def run(self):
        print('Animal is running...')
    
A=Animal()
A.run()

#多态
class Student1():
    def grade(self):
        print('哇要考试啦！')


class goodStudent(Student1):
    def grade(self):
        print('哇满分！')


class badStudent(Student1):
    def grade(self):
        print('哇零分')


class Pig(Student1):
    def grade(self):
        print('精品猪肉！')


def kind(student):
    student.grade()
student1 = Student1()
good = goodStudent()
bad = badStudent()
pig = Pig()

kind(student1)
kind(good)
kind(bad)
kind(pig)


#为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
class Student2(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student2.count=Student2.count+1
if Student2.count != 0:
    print('测试失败!')
else:
    bart = Student2('Bart')
    if Student2.count != 1:
        print('测试失败!')
    else:
        lisa = Student2('Bart')
        if Student2.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student2.count)
            print('测试通过!')
class A(object):
    def set_age(self,age):
        self.age=age
        return age
S=A()
print(S.set_age(20))