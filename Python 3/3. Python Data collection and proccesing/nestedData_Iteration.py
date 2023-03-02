# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 16:23:35 2020

@author: pipem
"""

"""
2. Below, we have provided a list of lists that contain information about people. 
Write code to create a new list that contains every person’s last name, and save that list as last_names.
"""
import copy

def nest(): 
    info = [['Tina', 'Turner', 1939, 'singer'], ['Matt', 'Damon', 1970, 'actor'], ['Kristen', 'Wiig', 1973, 'comedian'], ['Michael', 'Phelps', 1985, 'swimmer'], ['Barack', 'Obama', 1961, 'president']]
    last_names = list()
    for person in info: 
        last_names.append(person[1])
    return last_names

#print(nest())

"""
3. Below, we have provided a list of lists named L. Use nested iteration to save every 
string containing “b” into a new list named b_strings
"""

def nest2(lst):
    
    b_strings = list()
    for lst in L: 
        for strg in lst: 
            if "b" in strg:
                b_strings.append(strg)
    return b_strings
L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas', 'cucumbers', 'green beans'], ['root beer', 'smoothies', 'cranberry juice']]
#print(nest2(L))


""" 
when something if no iterable
"""
def with_not_iterable(lst):
    for x in lst:
        print("level1: ")
        if type(x) is list: # si el type no es iterable else:
            for y in x:
                print("     level2: {}".format(y))
        else:
            print(x) #salta aca e imprime ese no iterable: 
lst = [1, 2, ['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
#print(with_not_iterable(lst))

"""
SHADOW AND DEEP  copy 
"""
def shadow_deep():
    original = [['canines', ['dogs', 'puppies']], ['felines', ['cats', 'kittens']]]
    shallow_copy_version = original[:]
    deeply_copied_version = copy.deepcopy(original)
    original.append("Hi there")
    original[0].append(["marsupials"])
    print("-------- Original -----------")
    print(original)
    print("-------- deep copy -----------")
    print(deeply_copied_version)
    print("-------- shallow copy -----------") 
    print(shallow_copy_version)
#shadow_deep()


"""
---------------------------ASSIGMENTE-------------------------------------------------
"""


"""
1. The variable nested contains a nested list. Assign ‘snake’ to the variable output using indexing.
"""

def snake(): 
    nested = [['dog', 'cat', 'horse'], ['frog', 'turtle', 'snake', 'gecko'], ['hamster', 'gerbil', 'rat', 'ferret']]
    for lst in nested: 
        if "snake" in lst:
            output = "snake"
    return output
#print(snake())

"""
2. Below, a list of lists is provided. Use in and not in tests to create variables with Boolean values. 
See comments for further instructions.
"""

def in_notin_test(): 
    lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]
    
    yellow = "yellow" in lst[2]
    four = 4 in lst[1]
    orange = "orange" in lst[0]
    return yellow,four,orange
#print(in_notin_test())

""" 
3. Provided is a nested data structure. Follow the instructions in the comments below. Do not hard code.
"""

def in_with_dic(): 
    nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}
    # Check to see if the string data is a key in nested, if it is, assign True to the variable data, 
    # otherwise assign False.
    lst_keys = list(nested.keys())
    if "data" in lst_keys:
        data = True
    else: 
        data = False
    # Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable 
    # twentyfour the value of True, otherwise False.
    if 24 in nested["data"]:
        twentyfour = True
    else: 
        twentyfour = False
    # Check to see that the string 'whole' is not in the value of the key window. If it's not, 
    # then assign to the variable whole the value of True, otherwise False.
    if "whole" not in nested["window"]:
        whole = True
    else: 
        whole = False
    return data,twentyfour,whole

#print(in_with_dic())

"""
The variable nested_d contains a nested dictionary with the gold medal counts for the top four 
countries in the past three Olympics. Assign the value of Great Britain’s gold medal count from 
the London Olympics to the variable london_gold. Use indexing. Do not hardcode
"""

def simple_dic():
    nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}
    london_gold = nested_d["London"]["Great Britain"]
    return london_gold
#print(simple_dic())
"""
Below, we have provided a nested dictionary. Index into the dictionary to create variables that we have 
listed in the ActiveCode window.
"""
def complex_dic():
    sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'], 'diving': ['springboard', 'platform', 'synchronized'], 'track': ['sprint', 'distance', 'jumps', 'throws'], 'gymnastics': {'women':['vault', 'floor', 'uneven bars', 'balance beam'], 'men': ['vault', 'parallel bars', 'floor', 'rings']}}
    # Assign the string 'backstroke' to the name v1
    v1 = sports["swimming"][2]
    # Assign the string 'platform' to the name v2
    v2 = sports["diving"][1]
    # Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the name v3
    v3 = sports["gymnastics"]["women"]

    # Assign the string 'rings' to the name v4
    v4 = sports["gymnastics"]["men"][3]
        
    return v1,v2,v3,v4
#print(complex_dic())
 
"""
Given the dictionary, nested_d, save the medal count for the USA from all three Olympics in the dictionary 
to the list US_count.  
""" 
def count():
    nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}
    US_count = list()
    US_count.append(nested_d["Beijing"]["USA"])
    US_count.append(nested_d["London"]["USA"])
    US_count.append(nested_d["Rio"]["USA"])
    
    return US_count
#print(count())

"""
Given below is a list of lists of athletes. Create a list, t, that saves only the athlete’s name if it 
contains the letter “t”. If it does not contain the letter “t”, save the athlete name into list other.
"""
def list_of_list():
    athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt', 'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]
    t = list()
    other = list()
    for lista in athletes:
        for name in lista:
            if "t" in name:
                t.append(name)
            else:
                other.append(name)
    return t,other
print(list_of_list())