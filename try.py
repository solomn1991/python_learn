__author__ = 'Solomn'

# #function1

# import logging
#
# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     try:
#         bar('0')
#     except StandardError, e:
#         logging.exception(e)
#
# main()
# print 'END'
#
# print 123

# #function2

# err.py
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')
main()