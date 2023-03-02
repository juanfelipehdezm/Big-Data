# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 18:03:59 2020

@author: pipem
"""

"""
Create a tuple called olympics with four elements: “Beijing”, “London”, “Rio”, “Tokyo”.
"""

def crateTuple():
    olympics = ("Beijing", "London", "Rio", "Tokyo")
    
"""
The list below, tuples_lst, is a list of tuples. Create a list of the second elements of 
each tuple and assign this list to the variable country.
"""
def fromtuple():
    tuples_lst = [('Beijing', 'China', 2008), ('London', 'England', 2012), ('Rio', 'Brazil', 2016, 'Current'), ('Tokyo', 'Japan', 2020, 'Future')]
    country = list()
    for lst in tuples_lst:
        country.append(lst[1])
    return country
#print(fromtuple())

"""
With only one line of code, assign the variables city, country, and year to the values of the 
tuple olymp.
"""

def unpacking():
    olymp = ('Rio', 'Brazil', 2016)
    city, country, year = olymp
    
"""
Define a function called info with five parameters: name, gender, age, bday_month, and hometown. 
The function should then return a tuple with all five parameters in that order.
"""
def info(name, gender, age, bday_month, hometown):
    return (name, gender, age, bday_month,hometown)
#tup = ('Sue', 'Female', 20, 'March', 'Ann Arbor')
#print (info(*tup))

"""
Given is the dictionary, gold, which shows the country and the number of gold medals they have 
earned so far in the 2016 Olympics. Create a list, num_medals, that contains only the number of 
medals for each country. You must use the .items() method. 
Note: The .items() method provides a list of tuples. Do not use .keys() method.
"""

def listOfKeys():
    gold = {'USA':31, 'Great Britain':19, 'China':19, 'Germany':13, 'Russia':12, 'Japan':10, 'France':8, 'Italy':8}
    num_medals = list()
    for k,v in gold.items():
        num_medals.append(v)
    return num_medals
#print(listOfKeys())