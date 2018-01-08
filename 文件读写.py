#! /usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys


class File(object):
    def __init__(self):
        pass

    def read(self):
        """
        使用with方法可以不用手动close文件，同时一行一行的读避免了内存占用过大
        :return:
        """

        pwd = os.getcwd()
        with open(os.path.join(pwd, 'test.yaml')) as f:
            for line in f:
                print line

    def write(self):
        with open(os.path.join(os.getcwd(), 'test.yaml'), 'a') as f:
            for i in range(10000):
                f.writelines('good evening!')
                f.write('bad!')

    def test_line(self):
        """
        统计文件的行数
        :return:
        """
        count = 0
        with open(os.path.join(os.getcwd(), 'test.yaml')) as f:
            for index, line in enumerate(f):
                count += 1
            print count


def read():
    pwd = os.getcwd()
    r = open(os.path.join(pwd, 'policy.yaml'))
    try:
        all_text = r.read()
        return all_text
    finally:
        r.close()


def write(data):
    pwd = os.getcwd()
    w = open(os.path.join(pwd, 'test2.yaml'), 'w')

    try:
        w.write(data)
    finally:
        w.close()


if __name__ == '__main__':
    # a = 'apiVersion: v1\nkind: Secret\nmetadata:  \n  name: mysecret\n  namespace: ws2\ntype: Opaque\ndata:\n  username: YWRtaW4=\n  password: MWYyZDFlMmU2N2Rm'
    # write(a)
    # f = File()
    # f.test_line()
    # r = read()
    # print r
    # print """{}""".format(r)
    ws_name = 'wsaaa1'
    policy_content = """
- apiVersion: v1
  kind: policy
  metadata:
    name: {}
  spec:
    selector: calico/k8s_ns == '{}'
    ingress:
    - action: allow
      source:
        selector: calico/k8s_ns == '{}'
    - action: deny
      source:
        selector: calico/k8s_ns != '{}'
    - action: allow
    egress:
    - action: allow""".format(ws_name, ws_name, ws_name, ws_name)
    with open(os.path.join(os.getcwd(), 'policy1.yaml'), 'w') as f:
        f.write(policy_content)