#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author :evilcoder
date   :2016/6/14 11:19
file   :App
"""

class Base :
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def info(self):
        print "{username = " + self.username + ", password = "+self.password + "]"

base = Base("nn","pp")
base.info()



