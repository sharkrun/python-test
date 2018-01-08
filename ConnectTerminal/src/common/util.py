#! /usr/bin/env python
# -*- coding:utf-8 -*-


class LawResult(object):
    def __init__(self):
        super(LawResult, self).__init__()


class Result(LawResult):
    def __init__(self, data, result=0, msg="done", code=200):
        super(Result, self).__init__()
        self.content = data
        self.result = result
        self.message = msg
        self.code = code

    @property
    def success(self):
        if not self.result == 0:
            return False
        return True

    @property
    def code_info(self):
        return self.code == 200

    def __str__(self):
        return "Result<'result':%d,'message':'%s','return':%s>" % (
            self.result, self.message, str(self.content))

    def to_ext_result(self):
        return {
            "success": self.result == 0,
            "KernelMessage": self.content,
            "message": self.message
        }

    def to_json(self):
        return {
            'error_code': self.result,
            'error_msg': self.message,
            'content': self.content
        }
