# coding:utf-8

# import itertools
# natuals = itertools.count(10)
# for n in natuals:
#     print n

# import itertools
#
# l = itertools.repeat({},10)
# for i in l:
#     print i

# import itertools
# l = itertools.chain("aaa","bbb")
# for i in l:
#     print i

# import itertools
# for key, group in itertools.groupby('AAABBBCACAAA'):
#     print key,group, list(group) # 为什么这里要用list()函数呢？

# import itertools
# r = itertools.imap(lambda x: x*x, [1, 2, 3])
# print r,list(r)

# import itertools
# print
# r = map(lambda x: x*x, list(itertools.count(1))) # 会不断申请内存，可能会死机
