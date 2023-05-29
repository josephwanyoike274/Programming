#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 06:14:08 2022

@author: wanyoike
"""

class Car:
    def __init__(self, speed, color):# used  to initialize some attributes
        print(speed)
        print(color)
        self.__speed = speed
        self.__color = color       
       #print("the__init__ is called")
        
    def set_speed(self, value):
        self.speed = value

    def get_speed(self):
        return self.speed
    
ford =  Car(200, "red")
#honda = Car(300, "blue")
#audi = Car(250, "green")

#ford.speed = 300 #we can change value of an attribute
ford.set_speed(500)


print(ford.get_speed())
#print(honda.color)

#how to make it private to prevent changing the value
