#! /usr/bin/env python
# -*- coding:utf-8 -*-

import requests


def http():
    url = 'http://192.168.8.26:8886/clusters/test1-ha'
    r = requests.get(url, timeout=3)
    print r.json()


if __name__ == '__main__':
    http()
