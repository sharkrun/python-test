#! /usr/bin/env python
# -*- coding:utf-8 -*-

# 使用闭包注意事项
# 1.闭包中是不能修改外部作用域的局部变量的


def foo():
    m = 0

    def foo1():
        m = 1
        print id(m)
        print m
    print id(m)
    print m
    foo1()
    print m

if __name__ == '__main__':
    foo()