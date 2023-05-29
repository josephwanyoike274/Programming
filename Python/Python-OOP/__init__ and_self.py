#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 18 05:54:39 2022

@author: wanyoike
"""

class Car:
    def __init__(self, speed, color):# used  to initialize some attributes
        print(speed)
        print(color)
        self.speed = speed
        self.color = color       
       #print("the__init__ is called")
        

ford =  Car(200, "red")
honda = Car(300, "blue")
audi = Car(250, "green")

print(ford.color)
print(honda.speed)

# 4:07:03