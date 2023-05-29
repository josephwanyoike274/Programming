#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 06:07:47 2022

@author: wanyoike
"""

#to prevent reassigning

class Hello:
    def __init__(self, name):
        self.a = 10
        self._b = 20
        self.__c = 30

hello = Hello("name")
print(hello.a)
print(hello._b)
print(hello.__c) #use __to make your attribute private