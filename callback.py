#! /usr/bin/env python
# -*- coding:utf-8 -*-

import threading


# 可调用的类
class Callable(object):
    def __init__(self, func, args):
        self.func = func
        self.args = args

    def __call__(self):
        apply(self.func, self.args)

        # 用于线程执行的函数


def counter(n):
    cnt = 0
    for i in xrange(n):
        for j in xrange(i):
            cnt += j
    print cnt


if __name__ == '__main__':
    # 初始化一个线程对象，传入可调用的Callable对象，并用函数counter及其参数1000初始化这个对象
    th = threading.Thread(target=Callable(counter, (1000,)))
    # 启动线程
    th.start()
    # 主线程阻塞等待子线程结束
    th.join()