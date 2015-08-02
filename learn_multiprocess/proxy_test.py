# coding:utf-8
__author__ = 'Solomn'



from multiprocessing import Manager,freeze_support

if __name__=="__main__":
    freeze_support()
    manager = Manager()
    l = manager.list([i*i for i in range(10)])
    print str(l)
    print l
    print repr(l)
    print l[4]
    print l[2:5]


    a = manager.list()
    b = manager.list()
    a.append(b)         # referent of a now contains referent of b
    print a, b

    b.append('hello')
    print a, b
