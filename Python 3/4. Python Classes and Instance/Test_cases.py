# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 12:10:20 2020

@author: pipem
"""


def mySum(list_numbers):
    suma = 0
    if len(list_numbers) == 0:
        suma = 0
    else:
        for num in list_numbers:
             suma += num
    return suma
assert mySum([]) == 0 #no retorna nada por que esta bien
# SE DEBEN HACER VARIOS assert PARA PROBAR QUE FUNCIONE EN TODOS LOS CASOS
#print(mySum([4,5,6,3,34343,0]))
"""
------------------------------------TESTING CLASES-----------------------------
"""
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy


#testing class constructor (__init__ method)
p = Point(3, 4)
assert p.y == 4
assert p.x == 3

#testing the distance method
p = Point(3, 4)
assert p.distanceFromOrigin() == 5.0

#testing the move method
p = Point(3, 4)
p.move(-2, 3)
assert p.x == 1
assert p.y == 7