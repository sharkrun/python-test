#! /usr/bin/env python
# -*- coding:utf-8 -*-
from twisted.internet import threads
from twisted.web import resource, server
from resthandler import dispatch


class RestResource(resource.Resource):
    def __init__(self, allow_none=True, useDateTime=False, encoding="UTF-8"):
        resource.Resource.__init__(self)
        self.isLeaf = True

    def render_GET(self, request):
        return self.process('GET', request)

    def process(self, http_method, request):
        try:
            responseFailed = []
            request.notifyFinish().addErrback(responseFailed.append)

            d = threads.deferToThread(dispatch, http_method, request)
            d.addErrback(self.error_callback)
            d.addCallback(self.callback, request, responseFailed)
            return server.NOT_DONE_YET
        except Exception as e:
            print e.message

    def callback(self, content, request, responseFailed=None):
        try:
            request.setHeader("content-length", str(len(content)))
            request.setHeader("Access-Control-Allow-Origin", "*")
            request.write(content)
            if not request.finished:
                request.finish()
        except RuntimeError:
            pass
        except Exception as e:
            print e.message

    def error_callback(self, failure):
        try:
            return str(failure)
        except Exception as e:
            print e.message


