#! /usr/bin/env python
# -*- coding:utf-8 -*-


def f(x, l=[]):
    for i in range(x):
        l.append(i * i)
    print l


class F(object):
    def __init__(self):
        self.name = 'test'

    @classmethod
    def a(cls):
        print 'aa'

    @property
    def b(self):
        return self.name
if __name__ == '__main__':
    f(1)
    f(2, [1, 2])
    f(3)
    f1 = F()
    b1 = F.b
    print b1
    F.a()
