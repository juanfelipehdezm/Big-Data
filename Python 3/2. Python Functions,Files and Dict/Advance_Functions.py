# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 15:26:51 2020

@author: pipem
"""

"""
Create a function called mult that has two parameters, the first is required and should be an 
integer, the second is an optional parameter that can either be a number or a string but whose 
default is 6. The function should return the first parameter multiplied by the second.
"""
def mult(x,y=6):
    return x*y
#print(mult(2,4))

"""
The following function, greeting, does not work. Please fix the code so that it runs without error. 
This only requires one change in the definition of the function.
"""
def greeting( name,greeting="Hello ", excl="!"): #e argumento sin default debe ser el primero
    return greeting + name + excl

#print(greeting("Bob", excl="!!!"))

"""
Write a function, test, that takes in three parameters: a required integer, an optional boolean 
whose default value is True, and an optional dictionary, called dict1, whose default value is 
{2:3, 4:5, 6:8}. If the boolean parameter is True, the function should test to see if the integer 
is a key in the dictionary. The value of that key should then be returned. 
If the boolean parameter is False, return the boolean value “False”.
"""
def test(integer, boolean = True, dict1={2:3, 4:5, 6:8}):
    if boolean is True: 
        for k,v in dict1.items():
            if integer == k:
                return v
            else: 
                return False
    else: 
        return False
#print(test(5, dict1 = {5:4, 2:1}))
"""
Write a function called checkingIfIn that takes three parameters. The first is a required parameter, 
which should be a string. The second is an optional parameter called direction with a default 
value of True. The third is an optional parameter called d that has a default value of 
{'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}. 
Write the function checkingIfIn so that when the second parameter is True, it checks to see if the 
first parameter is a key in the third parameter; if it is, return True, otherwise return False.

But if the second paramter is False, then the function should check to see if the first parameter 
is not a key of the third. If it’s not, the function should return True in this case, and if it is, 
it should return False.
"""

def checkingIfIn(strg, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
     if direction is True:
          keys = list(d.keys())
          if strg in keys:
              return d[strg] #retorna el valor asociado a esa key
          else: 
              return False
     else:
         keys = list(d.keys())
         if strg not in keys:
             return True
         else:
             return d[strg]
# Call the function so that it returns False and assign that function call to the variable c_false
#c_false = checkingIfIn("mango")
#print (c_false)
# Call the fucntion so that it returns True and assign it to the variable c_true
#c_true = checkingIfIn("mango",False)
#print(c_true)
# Call the function so that the value of fruit is assigned to the variable fruit_ans
#fruit_ans = checkingIfIn("fruit")
#print(fruit_ans)
# Call the function using the first and third parameter so that the value 8 is assigned to the variable param_check
#param_check = checkingIfIn("apple",d = {'apple': 8, 'pear': 1, 'fruit': 19})
#print(param_check)