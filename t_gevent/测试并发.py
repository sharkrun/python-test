#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
>> pip install grequests

使用grequests创建异步HTTP请求。
"""
# from gevent import monkey
# monkey.patch_all()
import requests
import grequests
import gevent
import time

num = 20000


def syn_req1():
    headers = {'token': '1234567890987654321'}
    rs = (grequests.get('http://192.168.8.26:8885/v1/cluster/list', headers=headers, timeout=5) for i in range(num))
    a = grequests.map(rs)
    return a


def myrequests():
    headers = {'token': '1234567890987654321'}
    try:
        r = requests.get('http://192.168.8.26:8885/v1/cluster/list', headers=headers)
    except requests.RequestException:
        return False, None
    if r.status_code == 200:
        return True, r.json()
    return False, None


def sleep_s():
    time.sleep(1)


def main0():
    s_d = {}
    for i in range(num):
        # s_d[i] = gevent.spawn(sleep_s)
        s_d[i] = gevent.spawn(myrequests)
    gevent.joinall(s_d.values(), timeout=30)
    succs_num = 0
    for v in s_d.values():
        if v.successful():
            succs_num += 1
            # print v.successful(), v.value
    print succs_num


def main1():
    r = syn_req1()
    # print r


def main2():
    for i in range(num):
        _, r = myrequests()
        # print _
        # sleep_s()


if __name__ == '__main__':
    # t0 = time.time()
    # main0()
    # print 'main0 cost:', time.time() - t0

    t1 = time.time()
    main1()
    print 'main1 cost:', time.time() - t1

    # t2 = time.time()
    # main2()
    # print 'main2 cost:', time.time() - t2

    """
    1000
        main0 cost: 16.6759572029
        main1 cost: 5.87984490395
        main2 cost: 7.31206393242

    1500
        main0 cost: 30.0331029892
        main1 cost: 6.57398104668
        main2 cost: 11.0852408409

    2000
        main1 cost: 7.119
        main2 cost: 14.79

    5000
        main1 cost: 15.32
        main2 cost: 37.02

    10000
        main1 cost: 20.75
        main2 cost: 72.61

    20000
        main1 cost: 33.49
    """
