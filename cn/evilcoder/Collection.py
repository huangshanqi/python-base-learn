#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author :evilcoder
date   :2016/6/18 17:03
file   :Collection
"""

list = []
list.append("a")
list.append("b")
list.append(10)
list.append(True)
for i in list:
    print i

list.__delitem__(0)
for i in list:
    print i

letters = ("a","b","c")
digits = (1,2,3)
tables = (letters, digits)
for i in tables:
    print i


single = (1,)
print single

param = (1)
print param

dict = {"key1":"value1","key2":"value2"}
print dict
dict["key3"] = "value3"
print dict
dict["key3"] = "value3_new"
print dict

# seq
seq = ["a","b","c","d"]
print seq[0]
print seq[1:3]
print seq[:]
print seq[1:-1]


