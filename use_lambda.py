#! /usr/bin/env python
# -*- coding:utf-8 -*-

x = [1, 2, 3, 4]
y = [1, 2]
a = lambda m, n: sum([pow(i, 2) for i in m if i in n])
b = a(x, y)
print 'b =', b
