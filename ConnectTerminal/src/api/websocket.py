#! /usr/bin/env python
# -*-coding:utf-8-*-

from common.util import Result


class Websocket(object):
    def __init__(self):
        pass

    def websocket(self, **kwargs):
        url = 'http://127.0.0.1:9000/chat'
        return Result(url)
