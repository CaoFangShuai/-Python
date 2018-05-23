# -*- coding: utf-8 -*-

# 如果我们要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。比如dir、cp等命令。
# 如果要在Python程序中执行这些目录和文件的操作怎么办？其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数，
# Python内置的os模块也可以直接调用操作系统提供的接口函数。
# 打开Python交互式命令行，我们来看看如何使用os模块的基本功能：


import os
print(os.name)
import json

'''
如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。

要获取详细的系统信息，可以调用uname()函数：

# print(os.uname())
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。

# 要获取详细的系统信息，可以调用uname()函数：
'''
print(os.environ)
print(os.environ.get('PATH'))
'''
操作文件和目录

操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：
'''
#print( os.path.abspath('.'))
#print(os.path.join(os.path.abspath('.'), 'testdir'))
#os.mkdir(os.path.join(os.path.abspath('.'),'testdir'))
#os.rmdir(os.path.join(os.path.abspath('.')))


obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)
print(s)