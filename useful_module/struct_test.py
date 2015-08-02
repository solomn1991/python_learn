# coding:utf-8

import struct
a = 1111111
b=struct.pack(">I",a)
print b
c = struct.unpack(">I",b)
print c


