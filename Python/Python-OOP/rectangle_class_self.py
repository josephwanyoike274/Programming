#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 20 05:54:45 2022

@author: wanyoike
"""


class Rectangle:
    def __init__(self, height,width):
        self.height = height
        self.width = width

rect1 = Rectangle(20, 60)
rect2 = Rectangle(50, 40)



print(rect1.height * rect1.width)
print(rect2.height * rect2.width)