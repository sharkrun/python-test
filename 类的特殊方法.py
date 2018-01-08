#! /usr/bin/env python
# -*- coding:utf-8 -*-
import math


class MyFunc(object):
    count = 0

    def __init__(self, name):
        MyFunc.count += 1
        self.count += 1
        self._name = name
        self.age = 18

    @classmethod
    def test(cls, a, b):
        print 'count:', cls.count
        return a+b

    @staticmethod
    def test1(a, b):
        return math.pow(a, b)

    @property
    def name(self):
        self.count += 10
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def __getitem__(self, n):
        """
        类的切片
        :param n:
        :return:
        """
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

if __name__ == "__main__":
    f = MyFunc('lear')
    f1 = MyFunc('lear2')
    print f[:5]
    print f.name
    f.name = 'lear1'
    print f.name
    print MyFunc.test(10, 11)
    print MyFunc.test1(2, 3)
    f.test(12, 34)
    print 'self.count:', f.count

