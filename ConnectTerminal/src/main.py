#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from twisted.internet import reactor
from twisted.web import server

from core.server import WebService


# from twisted.python import threadable
# threadable.init(1)


def main():
    print __file__
    workroot = os.path.dirname(os.path.abspath(__file__))
    reactor.suggestThreadPoolSize(20)

    webserver = WebService(workroot)
    reactor.listenTCP(9001, server.Site(webserver.get_resource(), timeout=10))
    reactor.run()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print e