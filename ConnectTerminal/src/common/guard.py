#! /usr/bin/env python
# -*- coding:utf-8 -*-


class LockGuard(object):
    def __init__(self, lock):
        self.lock = lock

    def __enter__(self):
        self.lock.acquire()
        # Log(4, "lock.acquire on [%s] [%s] inspect:[%s]"%(id(self), id(self.lock), inspect.stack()[1]))

    def __exit__(self, _type, value, traceback):
        self.lock.release()
        # Log(4, "lock.release on [%s] [%s] inspect:[%s]"%(id(self), id(self.lock), inspect.stack()[1]))


class FileGuard(object):
    def __init__(self, filename, mode):
        self.mode = mode
        self.filename = filename
        self.f = None

    def __enter__(self):
        try:
            self.f = open(self.filename, self.mode)
            return self.f
        except IOError as e:
            return None

    def __exit__(self, _type, value, traceback):
        if self.f:
            self.f.close()