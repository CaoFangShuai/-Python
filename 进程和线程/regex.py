# -*-coding:utf-8-*-
'''
在正则表达式中，如果直接给出字符，就是精确匹配。用\d可以匹配一个数字，\w可以匹配一个字母或数字，所以：

'00\d'可以匹配'007'，但无法匹配'00A'；
'\d\d\d'可以匹配'010'；
'\w\w\d'可以匹配'py3'；
.可以匹配任意字符，所以：
'py.'可以匹配'pyc'、'pyo'、'py!'等等。
要匹配变长的字符，在正则表达式中，用*表示任意个字符（包括0个），用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符：
来看一个复杂的例子：\d{3}\s+\d{3,8}。
我们来从左到右解读一下：
\d{3}表示匹配3个数字，例如'010'；
\s可以匹配一个空格（也包括Tab等空白符），所以\s+表示至少有一个空格，例如匹配' '，' '等；
\d{3,8}表示3-8个数字，例如'1234567'。
综合起来，上面的正则表达式可以匹配以任意个空格隔开的带区号的电话号码。
如果要匹配'010-12345'这样的号码呢？由于'-'是特殊字符，在正则表达式中，要用'\'转义，所以，上面的正则是\d{3}\-\d{3,8}。
但是，仍然无法匹配'010 - 12345'，因为带有空格。所以我们需要更复杂的匹配方式。
进阶
要做更精确地匹配，可以用[]表示范围，比如：
[0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；
[0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；
[a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；
[a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。
A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'。
^表示行的开头，^\d表示必须以数字开头。
$表示行的结束，\d$表示必须以数字结束。
你可能注意到了，py也可以匹配'python'，但是加上^py$就变成了整行匹配，就只能匹配'py'了。
match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。常见的判断方法就是：
test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')
'''
import re
def is_valid_email(addr):
    # '[\w\.]+@\w+.\w+'
    # \w*.\w*@\w*.\w*
    if re.match(r'[\w.]+@\w+.\w+', addr):
        print('ok')
    else:
        print('failed')
is_valid_email("someone@gmail.com")
is_valid_email('bill.gates@microsoft.com')
is_valid_email('bob#example.com')
is_valid_email('mr-bob@example.com')
def name_of_email(addr):
    groups = re.match(r'<?([\w\s]+)>?(.*)@', addr)
    if groups:
        print(groups[1])
    else:
        return None
name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
name_of_email('tom@voyager.org') == 'tom'