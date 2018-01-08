#! /usr/bin/env python
# -*- coding:utf-8 -*-
import copy

# 浅拷贝
will = ["Will", 28, ["Python", "C#", "JavaScript"]]
wilber = copy.copy(will)

print id(will)
print will
print [id(ele) for ele in will]
print id(wilber)
print wilber
print [id(ele) for ele in wilber]

will[0] = "Wilber"
will[2].append("CSS")
print id(will)
print will
print [id(ele) for ele in will]
print id(wilber)
print wilber
print [id(ele) for ele in wilber]


# 深拷贝
will = ["Will", 28, ["Python", "C#", "JavaScript"]]
wilber = copy.deepcopy(will)

print id(will)
print will
print [id(ele) for ele in will]
print id(wilber)
print wilber
print [id(ele) for ele in wilber]

will[0] = "Wilber"
will[2].append("CSS")
print id(will)
print will
print [id(ele) for ele in will]
print id(wilber)
print wilber
print [id(ele) for ele in wilber]


books = ('python', 'java', 'C++')
copys = copy.deepcopy(books)
print books is copys

books = ('python', 'java', 'C++', [])
copys = copy.deepcopy(books)
print books is copys

# 拷贝的特殊情况
#
# 其实，对于拷贝有一些特殊情况：
#
# 对于非容器类型（如数字、字符串、和其他’原子’类型的对象）没有拷贝这一说
# 也就是说，对于这些类型，”obj is copy.copy(obj)” 、”obj is copy.deepcopy(obj)”
#
# 如果元祖变量只包含原子类型对象，则不能深拷贝，看下面的例子