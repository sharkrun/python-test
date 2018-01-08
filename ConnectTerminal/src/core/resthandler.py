# -*- coding:utf-8 -*-
"""
分发控制台提交的请求
"""

import json
import datetime


def dispatch(http_method, request):
    print 'http_method:', http_method
    print 'request:', request
    print 'dir(request):{}'.format(dir(request))
    t1 = datetime.datetime.now()
    print t1
    print datetime.datetime.now() - t1
    data = {
        'content': 'http://127.0.0.1:9000',
        'error_code': 0,
        'error_msg': 'done'
    }
    return json.dumps(data)

