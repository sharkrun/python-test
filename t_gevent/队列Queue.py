#! /usr/bin/env python
# -*- coding:utf-8 -*-

import gevent
from gevent.queue import Queue

products = Queue()


# put和get方法都是阻塞式的，它们都有非阻塞的版本：put_nowait和get_nowait。如果调用get方法时队列为空，则抛出”gevent.queue.Empty”异常


def consumer(name):
    while not products.empty():
        # print '%s got product %s' % (name, products.get())
        print '%s got product %s' % (name, products.get_nowait())
        gevent.sleep(0)

    print '%s Quit'


def producer():
    for i in xrange(1, 100000):
        # products.put(i)
        products.put_nowait(i)


gevent.joinall([
    gevent.spawn(producer),
    gevent.spawn(consumer, 'steve'),
    gevent.spawn(consumer, 'john'),
    gevent.spawn(consumer, 'nancy'),
])
