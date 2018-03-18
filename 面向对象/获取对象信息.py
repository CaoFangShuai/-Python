#-*-coding:utf-8-*-
# 当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？
'''
使用type()

首先，我们来判断对象类型，使用type()函数：

基本类型都可以用type()判断：
'''
print type(123)
print type('str')
print type(None)
print type(abs)
'''
但是type()函数返回的是什么类型呢？它返回对应的Class类型。如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同：

>>> type(123)==type(456)
True
>>> type(123)==int
True
>>> type('abc')==type('123')
True
>>> type('abc')==str
True
>>> type('abc')==type(123)
False
判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
'''
import types
def fn():
    pass
print type(fn)==types.FunctionType
print type(abs)==types.BuiltinFunctionType
print type(lambda x:x+1)==types.LambdaType
print type( x for x in range(10))==types.GeneratorType
'''使用isinstance()

对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。

我们回顾上次的例子，如果继承关系是：object -> Animal -> Dog -> Husky'''
class Animal(object):
    pass
class Dog(Animal):
    pass
class Husky(Dog):
    pass

a = Animal()
d = Dog()
h = Husky()
print isinstance(h,Husky)
print isinstance(h, Dog)
print  isinstance(h, Animal)
print isinstance(d, Dog) and isinstance(d, Animal)
print isinstance(d, Husky)
# 能用type()判断的基本类型也可以用isinstance()判断：

print  isinstance([1, 2, 3], (list, tuple))
print  isinstance((1, 2, 3), (list,tuple))
# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。
# 使用dir()

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print dir('ABC')
print dir(h)
print len('ABC')
print 'ABC'.__len__()
class MyDog(object):
    def __len__(self):
        return 100
dog=MyDog()
print len(dog)
# 剩下的都是普通属性或方法，比如lower()返回小写的字符串：
print "ASDSDA".lower()
class MyObject(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x*self.x
obj=MyObject()
print  hasattr(obj, 'x') # 有属性'x'吗？
# True
print obj.x
# 9
print hasattr(obj, 'y') # 有属性'y'吗？
# False
setattr(obj, 'y', 19) # 设置一个属性'y'
print hasattr(obj, 'y') # 有属性'y'吗？
# True
print getattr(obj, 'y') # 获取属性'y'
# 19
print obj.y # 获取属性'y'
# 19
# print getattr(obj, 'z')
print getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404

print hasattr(obj, 'power') # 有属性'power'吗?
print getattr(obj, 'power') # 获取属性'power'
fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
print fn# fn指向obj.power
print fn() # 调用fn()与调用obj.power()是一样的
'''小结

通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写：'''
# print (sum = obj.x + obj.y)
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
'''假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。

请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，
但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。'''


