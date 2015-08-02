# coding:utf-8
import pdb

'''namedtuple'''
if __name__=="__main__":
    from collections import namedtuple

    Point = namedtuple("Point",["x","y"])

    p = Point(1,3)
    print p.x,p.y

    print type(p)
    print isinstance(p,Point)
    print isinstance(p,tuple)
    print "-------------------------------------"


if __name__=="__main__":
    from collections import deque
    q = deque([1,2,3])
    q.append("tail")
    q.appendleft("head")
    print q
    print type(q)
    print isinstance(q,deque)
    print "-------------------------------------"


if __name__=="__main__":
    from collections import defaultdict
    dd = defaultdict()
    dd['a'] = "aa"
    print dd
    print dd["a"]
    # print dd["b"],"|",type(dd["b"])

    print "-------------------------------------"

if __name__=="__main__":
    from collections import OrderedDict
    d = dict([('a', 1), ('b', 2), ('c', 3)])
    print d
    od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    print od
    print "-------------------------------------"

if __name__=="__main__":
    from collections import Counter
    c = Counter()
    for ch in 'programming':
        c[ch] = c[ch]+1

    print c
    print "-------------------------------------"


