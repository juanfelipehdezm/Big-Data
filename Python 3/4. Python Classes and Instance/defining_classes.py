# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 12:24:39 2020

@author: pipem
"""

"""
Create a class called NumberSet that accepts 2 integers as input, and defines two instance 
variables: num1 and num2, which hold each of the input integers. Then, create an instance of NumberSet where 
its num1 is 6 and its num2 is 10. Save this instance to a variable t.
"""

class NumberSet():
    def __init__ (self,num1,num2): 
        self.num1 = num1
        self.num2 = num2
    def __str__(self): #metodo para imprimir el contenido de la Instance
        return "Number set : ({} , {})".format(self.num1,self.num2)
    def get_num1(self):
        return self.num1
    def get_num2(self):
        return self.num2
    def sum_of_nums(self):
        return self.get_num1() + self.get_num2()
    def divded_in(self,newPoint):
        d1 = self.num1 / newPoint.num1
        d2 = self.num2 / newPoint.num2
        return NumberSet(d1,d2)
    
t = NumberSet(6,10)
p = NumberSet(3,20)
#print(t)
#print("Valor de num1 = ",t.get_num1())
#print("Valor de num2 = ",t.get_num2())
print("Suma del punto  = ",t.sum_of_nums())
#print("T divido en P",t.divded_in(p))

"""
sorting lists of instances
"""
class Fruit():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__ (self):
        return "{} at a price of {}".format(self.name,self.price)

    def sort_priority(self):
        return self.price

L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]
#print("---- one more way to do the same thing-----")
#for f in sorted(L, key=lambda x: x.sort_priority()):
    #print(f)
    
    
""" 
-------------------------------ASIGGMENT--------------------------------------
"""

"""
1. Define a class called Bike that accepts a string and a float as input, and assigns those inputs respectively 
to two instance variables, color and price. Assign to the variable testOne an instance of Bike whose color is 
blue and whose price is 89.99. Assign to the variable testTwo an instance of Bike whose color is purple and 
whose price is 25.0.
"""
class Bike():
    def __init__(self,color,price):
        self.color = color
        self.price = float(price)
    
    def __str__(self):
        return "The bike with the color {} cots {}".format(self.color,self.price)
testOne = Bike("blue",89.99)
#print(testOne)
testTwo = Bike("purple",25.0)
#print(testTwo)

"""
2. Create a class called AppleBasket whose constructor accepts two inputs: a string representing a color, 
and a number representing a quantity of apples. The constructor should initialize two instance variables: 
apple_color and apple_quantity. Write a class method called increase that increases the quantity by 1 each 
time it is invoked. You should also write a __str__ method for this class that returns a string of the 
format: "A basket of [quantity goes here] [color goes here] apples." e.g. 
"A basket of 4 red apples." or "A basket of 50 blue apples." 
(Writing some test code that creates instances and assigns values to variables may help you solve this problem!)
"""
class AppleBasket():
    def __init__(self,apple_color,apple_quantity):
        self.apple_color = str(apple_color)
        self.apple_quantity = int(apple_quantity)
    def increase(self):
        self.apple_quantity += 1
        return self.apple_quantity
    def __str__(self):
        return "A basket of {} {} apples.".format(self.apple_quantity,self.apple_color)
    
    
apple = AppleBasket("red",4)
#print(apple)
#print(apple.increase())

"""
3. Define a class called BankAccount that accepts the name you want associated with your bank account in a 
string, and an integer that represents the amount of money in the account. The constructor should initialize 
two instance variables from those inputs: name and amt. Add a string method so that when you print an instance 
of BankAccount, you see "Your account, [name goes here], has [start_amt goes here] dollars.
" Create an instance of this class with "Bob" as the name and 100 as the amount. Save this to the variable t1.
"""
class BankAccount():
    def __init__ (self,name,amt):
        self.name = str(name)
        self.amt = int(amt)
    def __str__(self):
        return "Your account, {}, has {} dollars".format(self.name,self.amt)
t1 = BankAccount("Bob",100)
print(t1)
        