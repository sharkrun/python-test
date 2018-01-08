#! /usr/bin/env python
# -*- coding:utf-8 -*-

import gevent
import time


def test1():
    print 11
    gevent.sleep(2)
    print 22
    return 't1'


def test2():
    print 33
    gevent.sleep(3)
    print 44
    return 't2'


def test3():
    print 55
    raise Exception('You failed!')

if __name__ == '__main__':
    t1 = time.time()
    j1 = gevent.spawn(test1)
    j2 = gevent.spawn(test2)
    j3 = gevent.spawn(test3)
    gevent.joinall([j1, j2], timeout=2)
    print 'job1, status:{}, value:{}, exception:{}'.format(j1.successful(), j1.value, j1.exception)
    print 'job2, status:{}, value:{}, exception:{}'.format(j2.successful(), j2.value, j2.exception)
    print 'job3, status:{}, value:{}, exception:{}'.format(j3.successful(), j3.value, j3.exception)
    print 'all cost:', time.time() - t1
