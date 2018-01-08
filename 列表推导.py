#! /usr/bin/env python
# -*- coding:utf-8 -*-


def larger(num1, num2):
    return num1 if num1 > num2 else num2


def lie(x, y):
    return sum([pow(i, 3) for i in x if i in y])


if __name__ == '__main__':
    print lie([1, 2, 3, 4], [1, 2])
