#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 18 05:29:46 2022

@author: wanyoike
"""


class Cars:
    pass      # pass means its empty class or attribute


ford = Cars()
honda = Cars()
audi = Cars()


ford.speed = 200
honda.speed = 250
audi.speed = 300

ford.color = "black"
honda.color = "red"
audi.color = "green"

print(ford.speed)
print(audi.color)

ford.speed = 400
audi.color = "blue"

print(ford.speed)
print(audi.color)