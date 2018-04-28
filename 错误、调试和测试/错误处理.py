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
import logging
def foo1(s):
    return 10 / int(s)

def bar1(s):
    return foo1(s) * 2

def main1():
    try:
        
        bar1('0')
    except Exception as e:
        logging.exception(e)
        
        

main1()
print('END')

