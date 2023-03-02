# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 16:08:31 2020

@author: pipem
"""

"""
Write code to assign to the variable compri all the values of the key name in any of the sub-dictionaries 
in the dictionary tester. Do this using a list comprehension.
"""
import json
def comprehension_in_dic():
    tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
    info = tester["info"]
    #info = json.dumps(info, indent = 2) just to check
    #print (info)
    compri = [d["name"] for d in info]
    return compri

#print(comprehension_in_dic())
"""
Below we have provided two lists of numbers, L1 and L2. Using zip and list comprehension, create a new list, 
L3, that sums the two numbers if the number from L1 is greater than 10 and the number from L2 is less than 5.
This can be accomplished in one line of code.
"""
def zipping():
    L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
    L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]

    L3 = [x1+x2 for(x1,x2) in list(zip(L1,L2)) if x1>10 and x2<5]
    return L3
#print(zipping())

"""
Write code to assign to the variable map_testing all the elements in lst_check while adding the string 
“Fruit: ” to the beginning of each element using mapping.
"""
def if_string(lst):
    map_testing = map(lambda fruit : "Fruit: " + fruit, lst)
    return map_testing
lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
#print(if_string(lst_check))
    
"""
Below, we have provided a list of strings called countries. Use filter to produce a list called b_countries 
that only contains the strings from countries that begin with B.
"""
def bCountries(countries):
    #countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']
    b_countries = filter(lambda countrie: countrie.startswith("B"),countries)
    return b_countries

countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']
#print(bCountries(countries))

"""
Below, we have provided a list of tuples that contain the names of Game of Thrones characters. 
Using list comprehension, create a list of strings called first_names that contains only the first names of 
everyone in the original list.
"""
def comprehension(): 
    people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]
    first_name = [ name for last_name,name in people ]
    return first_name
#print(comprehension())

"""
Below, we have provided a list of tuples that contain students’ names and their final grades in PYTHON 101. 
Using list comprehension, create a new list passed that contains the names of students who passed the class 
(had a final grade of 70 or greater).
"""
def who_pass(): 
    students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]
    passed = [name for name,note in students if note>=70]
    return passed
#print(who_pass())

"""
Write code using zip and filter so that these lists (l1 and l2) are combined into one big list and assigned to 
the variable opposites if they are both longer than 3 characters each.
"""
def zip_and_filter():
    l1 = ['left', 'up', 'front']
    l2 = ['right', 'down', 'back']
    opposites = [ (x,y) for (x,y) in list(zip(l1, l2)) if len(x) and len(y) < 3]
    return opposites
#print(zip_and_filter())

"""
Below, we have provided a species list and a population list. Use zip to combine these lists into one list of 
tuples called pop_info. From this list, create a new list called endangered that contains the names of 
species whose populations are below 2500.
"""
def tuples(): 
    species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']
    population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]
    pop_info = list(zip(species,population))
    endangered = [pet for pet,pop in pop_info if pop < 2500]
    return endangered
#print(tuples())
