# Copyright (c) 20016-2016 The Cloudsoar.
# See LICENSE for details.

"""
Parse json configure
"""

from common.guard import FileGuard
import copy
import json


class ConfigBase(object):
    conf = {}

    def __init__(self, fullpath=None):
        if fullpath is None:
            return

        self.loadConfig(fullpath)

    def loadConfig(self, fullpath):
        jsStr = "{}"
        try:
            with open(fullpath, "r") as fd:
                jsStr = fd.read()
            self.conf = json.loads(jsStr)
        except Exception, e:
            print e.message

    def save_config(self, fileName):
        '''will compress the config file'''
        text = json.dumps(self.conf, indent=4)
        with FileGuard(fileName, 'w') as fd:
            fd.write(text)

    def get_config(self, key=None):
        if not key:
            return self.conf
        if "." not in key:
            if key in self.conf:
                return self.conf[key]
        else:
            arr = key.split(".")
            config = copy.deepcopy(self.conf)
            for i in range(len(arr)):
                if arr[i] in config:
                    config = config[arr[i]]
                else:
                    config = None
                    break
            return config
        # Log(1,"get_config fail,key:%s"%key)
        return None

    def update_key(self, key, value):
        arr = key.split(".")
        obj = self.parse_str(arr, value)
        self.conf.update(obj)

    def regist_key(self, key, value):
        v = self.get_config(key)
        if v is not None:
            return False
        else:
            self.update_key(key, value)
        return True

    def parse_str(self, arr, value):
        obj = {}
        if len(arr) == 0:
            return {}
        if len(arr) == 1:
            obj[arr[0]] = value
            return obj

        obj[arr[-1]] = value
        return self.parse_str(arr[0:-1], obj)
