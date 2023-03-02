# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 12:21:00 2020

@author: pipem
"""

"""
1. You will be sorting the following list by each element’s second letter, a to z. 
Create a function to use when sorting, called second_let. It will take a string as input and 
return the second letter of that string. Then sort the list, create a variable called 
sorted_by_second_let and assign the sorted list to it. Do not use lambda.
"""
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
def second_let(strg):
    return strg[1]

sorted_by_second_let = sorted(ex_lst,key= second_let)
#print(sorted_by_second_let)

"""
2. Below, we have provided a list of strings called nums. Write a function called last_char 
that takes a string as input, and returns only its last character. Use this function to sort the 
list nums by the last digit of each number, from highest to lowest, and save this as a new list 
called nums_sorted.
"""
nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

def last_char(strg):
    return strg[-1]

nums_sorted = sorted(nums,key=last_char,reverse = True)
#print(nums_sorted)

"""
Sort the following dictionary based on the keys so that they are sorted a to z. 
Assign the resulting value to the variable sorted_keys.
"""
def sortdicKeys():
    dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}
    sorted_keys = sorted(dictionary.keys())
    return sorted_keys
#print(sortdicKeys())

"""
Sort the following dictionary’s keys based on the value from highest to lowest. 
Assign the resulting value to the variable sorted_values.
"""
def sortdicValues():
    dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}
    sorted_values = sorted(dictionary.keys(), key = lambda k: dictionary[k], reverse = True)
    return sorted_values #Ojo no retorna los valores, sino las keys 
#print(sortdicValues())


"""
What will the sorted function sort by?
"""
def sortDicInDic():
    weather = {'Reykjavik': {'temp':60, 'condition': 'rainy'},
           'Buenos Aires': {'temp': 55, 'condition': 'cloudy'},
           'Cairo': {'temp': 96, 'condition': 'sunny'},
           'Berlin': {'temp': 89, 'condition': 'sunny'},
           'Caloocan': {'temp': 78, 'condition': 'sunny'}}

    sorted_weather = sorted(weather, key=lambda w: (w, weather[w]['temp']))
    #primero ordena por albafeticamente por nombre de ciudad y si inicnan por misma letra 
    #oderdn por temperatura, de menor a mayor
    return sorted_weather
#print(sortDicInDic())

"""
Juntar lambda con funtions
"""
def s_cities_count(city_list): 
    """ Cuenta toda las ciudades de una lista que inian con S """
    ct = 0
    for city in city_list:
        if city[0] == "S":
            ct += 1
    return ct

states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
          "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
          "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}

#print(sorted(states, key=lambda state: s_cities_count(states[state])))
#                   lambda retorna en este caso la funcion que toma como input una lista

"""
-------------------ASSIGMENT--------------------------------------------------
"""

"""
1) Sort the following string alphabetically, from z to a, and assign it to the variable sorted_letters.
"""
def sortStrg():
    letters = "alwnfiwaksuezlaeiajsdl"
    sorted_letters = sorted(letters, reverse = True) 
    return sorted_letters
#print(sortStrg())

"""
2) Given the same dictionary, medals, now sort by the medal count. Save the three countries with 
the highest medal count to the list, top_three.
"""
def topThree():
    medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
    sorted_medals = sorted(medals.keys(), key = lambda k: medals[k], reverse = True)
    top_three = sorted_medals[:3]
    return top_three
#print(topThree())

"""
3) Create a function called last_four that takes in an ID number and returns the last four digits. 
For example, the number 17573005 should return 3005. Then, use this function to sort the list of 
ids stored in the variable, ids, from lowest to highest. Save this sorted list in the variable, 
sorted_ids. Hint: Remember that only strings can be indexed, so conversions may be needed.
"""
def last_four(x):
    to = str(x)
    return to[-4:]
#print(last_four(123453543543))

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_ids = sorted(ids,key = last_four)
#print(sorted_ids)

"""
4) Sort the following list by each element’s second letter a to z. Do so by using lambda. 
    Assign the resulting value to the variable lambda_sort.
"""
def sortwithLambda():
    ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
    lambda_sort = sorted(ex_lst, key = lambda strg: strg[1])
    return lambda_sort
#print(sortwithLambda())