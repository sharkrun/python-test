#! /usr/bin/env python
# -*- coding:utf-8 -*-

from gevent.server import StreamServer


def connection_handler(socket, address):
    for l in socket.makefile('r'):
        socket.sendall(l)


if __name__ == '__main__':
    server = StreamServer(('0.0.0.0', 8001), connection_handler)
    server.serve_forever()
