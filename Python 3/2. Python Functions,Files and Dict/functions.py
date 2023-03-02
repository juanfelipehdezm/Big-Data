# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 11:16:19 2020

@author: pipem
"""

"""
Write a function called int_return that takes an integer as input and returns the same integer.
"""
def int_return(x):
    return x

#print(int_return(34))

"""
Write a function called add that takes any number as its input and returns that sum with 2 added.
"""

def add(x):
    y = x + 2
    return y

#print(add(45))

"""
Write a function called change that takes any string, adds “Nice to meet you!” 
to the end of the argument given, and returns that new string.
"""
def change(string):
    return str(string) + " Nice to meet you!"

#print(change("Felipe"))

"""
Write a function, accum, that takes a list of integers as input and returns the sum 
of those integers.
"""
def accum(lst):
    total = 0
    for num in lst:
        total += int(num)
    return total 

numbers = [4,5,3,"3","2"]
#print (accum(numbers))

"""
Write a function, length, that takes in a list as the input. If the length of the 
list is greater than or equal to 5, return “Longer than 5”. If the length is less than 5,
return “Less than 5”.
"""
def length(lst):
    if len(lst) >= 5:
        return "Longer than 5"
    else:
        return "Less than 5"
lista = ["hola",5,"jeje"]
#print(length(lista))

"""
You will need to write two functions for this problem. 
The first function, divide that takes in any number and returns that same number divided by 2. 
The second function called sum should take any number, divide it by 2, and add 6. 
It should return this new number. You should call the divide function within the sum function. 
Do not worry about decimals.
"""
def divide(x):
    y = x / 2
    return y
def summm(num):
    z = divide(num) + 6
    return z 

#print (summm(2))

