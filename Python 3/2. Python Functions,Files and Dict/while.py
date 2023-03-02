# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 09:53:48 2020

@author: pipem
"""

"""
Write a while loop that is initialized at 0 and stops at 15. If the counter is an even number,
append the counter to a list called eve_nums.
"""
def eve():
    count = 0 
    eve_nums = list()
    while count <= 15:
        if count %2 == 0:
            eve_nums.append(count)
        count += 1
    return eve_nums
#print (eve())
"""
Below, we’ve provided a for loop that sums all the elements of list1. 
Write code that accomplishes the same task, but instead uses a while loop. 
Assign the accumulator variable to the name accum.
"""

def summOfList ():
    list1 = [8, 3, 4, 5, 6, 7, 9]
    idx = 0  # para secuencias como listas y string se inicia en 0 
    accum = 0 
    while idx < len(list1):
        accum += list1[idx]
        idx += 1
    return accum
#print (summOfList())
    

"""
Write a function, sublist, that takes in a list of numbers as the parameter. 
In the function, use a while loop to return a sublist of the input list. 
The sublist should contain the same values of the original list up until it reaches the number 5 
(it should not contain the number 5).
"""

def sublist(alst): 
    idx = 0 
    lst = list()
    while idx < len(alst) and alst[idx] != 5: #recorre la lista y un elemento diferente de 5
        lst.append(alst[idx])
        idx += 1
    return lst
#print (sublist([1, 2, 3, 4, 5, 6, 7, 8]))
"""
Write a function called check_nums that takes a list as its parameter, and contains a while loop 
that only stops once the element of the list is the number 7. What is returned is a list of all of 
the numbers up until it reaches 7.
"""
def check_nums(alst):
    idx = 0 
    lst = list()
    while idx < len(alst) and alst[idx] != 7: 
        lst.append(alst[idx])
        idx += 1
    return lst
#print (check_nums([1, 2, 3, 4, 5, 6, 7, 8]))

"""
Write a function, sublist, that takes in a list of strings as the parameter. 
In the function, use a while loop to return a sublist of the input list. 
he sublist should contain the same values of the original list up until it reaches the string 
“STOP” (it should not contain the string “STOP”).
"""
def sublist2(alist):
    idx = 0
    lst = list()
    while idx < len(alist) and alist[idx] != "STOP":
        lst.append(alist[idx])
        idx += 1
    return lst
print(sublist2(['bob', 'joe', 'lucy', 'STOP', 'carol', 'james']))

"""
Write a function called stop_at_z that iterates through a list of strings. 
Using a while loop, append each string to a new list until the string that appears is “z”. 
The function should return the new list.
"""
def stop_at_z(alist):
    idx = 0
    lst = list()
    while idx < len(alist) and alist[idx] != "z": 
        lst.append(alist[idx])
        idx += 1
    return lst
#print(stop_at_z(['c', 'b', 'd', 'zebra', 'h', 'r', 'z', 'm', 'a', 'k']))

"""
Below is a for loop that works. Underneath the for loop, rewrite the problem so that it does 
the same thing, but using a while loop instead of a for loop. Assign the accumulated total in 
the while loop code to the variable sum2. Once complete, sum2 should equal sum1.
"""
def whileAndFor(lista):
    sum1 = 0 
    lst = list()
    sum2 = 0 
    idx = 0 
    for x in lst:
        sum1 = sum1 + x
    while idx < len(lst):
        sum2 += lst[idx]
        idx += 1
    if sum1 == sum2:
        return True
    else :
        return False
#print(whileAndFor([65, 78, 21, 33]))

"""
Challenge: Write a function called beginning that takes a list as input and contains a while loop 
that only stops once the element of the list is the string ‘bye’. What is returned is a list that 
contains up to the first 10 strings, regardless of where the loop stops. 
(i.e., if it stops on the 32nd element, the first 10 are returned. If “bye” is the 5th element, 
the first 4 are returned.) If you want to make this even more of a challenge, 
do this without slicing
"""
def beginning(alist):
    idx = 0
    lst = list()
    while idx < len(alist) and alist[idx] != "bye": 
        lst.append(alist[idx])
        idx += 1
    if len(lst) > 10: 
        return lst[:11]
    else:
        return lst
#print (beginning(['hello', 'hi', 'hiyah', 'howdy', 'what up', 'whats good', 'holla', 'good afternoon', 'good morning', 'sup', 'see yah', 'toodel loo', 'night', 'until later', 'peace', 'bye', 'good-bye', 'g night']))
