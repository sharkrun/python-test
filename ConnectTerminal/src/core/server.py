# Copyright (c) 20016-2016 The Cloudsoar.
# See LICENSE for details.

"""
Implement the web server
"""

import os

from twisted.application import service
from twisted.internet.protocol import Factory
from twisted.web import resource
from twisted.web.static import File
from txsockjs.factory import SockJSResource
from frame.configmgr import ConfigMgr
from frame.web import mimesuffix
from frame.logger import PrintStack, Log
from terminal import SSHProtocol
# from frame.web import mimesuffix
from restapi import RestResource


# return html resource
class RootResource(resource.Resource):
    isLeaf = False
    numberRequests = 0

    def __init__(self, service):
        resource.Resource.__init__(self)
        self.service = service
        self.www_root = ConfigMgr.instance().get_www_root_path()

    def render_GET(self, request):
        path = os.path.normcase(request.path)[1:]

        response = None
        try:
            suffix = "html"
            if len(path) == 0:
                path = "index.html"

            fullpath = os.path.join(self.www_root, path)
            suffix = os.path.splitext(os.path.basename(path))[-1][1:]
            if suffix == '':
                suffix = 'html'
                fullpath = os.path.join(fullpath, "index.html")

            if os.path.isfile(fullpath):
                with open(fullpath, "rb") as fp:
                    response = fp.read()

            if suffix in mimesuffix:
                request.setHeader("content-type", mimesuffix[suffix])
        except:
            PrintStack()

        response = response if response else "<body><h1>Error!</h1>Get file [%s] fail</body>" % (path)
        request.setHeader("content-length", str(len(response)))
        return response

    def render_POST(self, request):
        response = '''<body><h1>Error!</h1>
        Method POST is not allowed for root resource
        </body>'''
        request.setHeader("content-type", ["text/html"])
        request.setHeader("content-length", str(len(response)))
        request.write(response)
        request.finish()

    def getChild(self, path, request):
        if path not in ["server"]:
            return self
        else:
            print "error"


class WebService(service.Service):
    def __init__(self, workroot, conf_file=""):
        self.workroot = workroot
        print 'server run...'

    def get_resource(self):
        www = os.path.split(self.workroot)[0]
        www = os.path.join(www, 'www')
        print 'www', www
        r = RootResource(self)
        r.putChild('v1', RestResource())
        r.putChild("chat", SockJSResource(Factory.forProtocol(SSHProtocol)))
        r.putChild("console", File(www))
        r.putChild("socket", File(os.path.join(os.path.split(self.workroot)[0], 'websocket.html')))
        return r

