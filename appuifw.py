#! /usr/bin/env python
# -*- coding:utf-8 -*-

import appuifw


def get_data_from_file():
    fp = open('c:\\names.txt', 'r')
    li = fp.readlines()
    fp.close()
    compList = []
    for item in li:
        item = item.decode("utf-8")
        compList.append(item)
    return compList

L = get_data_from_file()
index = appuifw.selection_list(choices=L , search_field=1)