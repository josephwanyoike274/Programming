#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 20 05:58:14 2022

@author: wanyoike
"""

#class Hello:
   # def __init__(self): pass
   # def __init__(self, name): pass
    
#hello =Hello("name")

# 2 __init__ methods are not valid

class Hello2:
    def __init__(self, *args): pass
hello = Hello2()
hello = Hello2("name", "jose", "wanyoike", "njoroge")
#4:16:43

class Hello2:
    def __init__(self, name2):
        self.name = name2
        self.age = 28

hello = Hello2("name")