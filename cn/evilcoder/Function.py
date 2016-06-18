#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author :evilcoder
date   :2016/6/18 14:22
file   :Function
"""
from App import Base

def testGlobalParam():
    """
    first line

    just for testing global parmas
    :return:
    """
    global x
    print "x in function is:",x
    x = -x
    print "x in function changed to :",x

x = 10
testGlobalParam()
print "final x is :", x





