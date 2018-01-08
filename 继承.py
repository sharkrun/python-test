#! /usr/bin/env python
# -*- coding:utf-8 -*-


class A(object):
    a_in = 10

    def __init__(self):
        print 'A...'

    def play(self):
        print 'ball'


class B(A):
    def __init__(self):
        print 'B....'
        super(B, self).__init__()
        super(B, self).play()

    def play(self):
        super(B, self).play()


class C(A):
    def __init__(self):
        print 'C....'
        super(C, self).__init__()
        super(C, self).play()

    def play(self):
        super(C, self).play()


class D(B, C):
    def __init__(self):
        print 'D....'
        super(D, self).__init__()
        super(D, self).play()

    def play(self):
        super(D, self).play()


if __name__ == '__main__':
    d = D()
    print '-------'
    print D.a_in

    d.play()
