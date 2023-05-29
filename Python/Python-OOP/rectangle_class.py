#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 18 05:29:46 2022

@author: wanyoike
"""

class Rectangle:
    pass

rect1 = Rectangle()
rect2 = Rectangle()

rect1.height = 20
rect2.height = 30

rect1.width = 40
rect2.width = 50

print(rect1.height * rect1.width)
print(rect2.height * rect2.width)