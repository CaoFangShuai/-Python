# -*- coding: utf-8 -*-
'''
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')
try:
    print('try...')
    r = 10 / 2
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')
'''
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 100

def main():
    try:
        bar('1')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')
main()
