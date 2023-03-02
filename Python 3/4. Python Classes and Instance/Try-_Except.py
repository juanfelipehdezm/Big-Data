# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 15:34:10 2020

@author: pipem
"""
"""
try:
    items = ['a', 'b']
    third = items[4]   #se provoca este error para que se ejecute la EXCEPTION.
    print("This won't print")
except Exception as e:
    print(e)  #asi imprimimos cualquier posible error y es mas abreviado
"""
"""
______________________________ASSIGMENT --------------------------------------
"""

"""
1.The code below takes the list of country, country, and searches to see if it is in the dictionary gold which 
shows some countries who won gold during the Olympics. However, this code currently does not work. 
Correctly add try/except clause in the code so that it will correctly populate the list, country_gold, 
with either the number of golds won or the string “Did not get gold”.
"""

def add_to_list():
    gold = {"US":46, "Fiji":1, "Great Britain":27, "Cuba":5, "Thailand":2, "China":26, "France":10}
    country = ["Fiji", "Chile", "Mexico", "France", "Norway", "US"]
    country_gold = []

    for x in country:
         try:
             country_gold.append(gold[x])
         except:
             country_gold.append("Did not get gold")
    return country_gold
#print(add_to_list())

"""
2. Provided is a buggy for loop that tries to accumulate some values out of some dictionaries. 
Insert a try/except so that the code passes.
"""
def puppies():
    di = [{"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49}, {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7}, {"Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89}, {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67}]
    total = 0
    for dic in di:
        try: #Como no todos los dic tienen ["Puppies"] se deben saltar
            puppies = dic["Puppies"]
            total  += puppies
        except Exception as e:
            print("this dic has no Puppies value", di[2])
            print(e)
    return total
#print("number of puppies:",puppies())
"""
3.The list, numb, contains integers. Write code that populates the list remainder with the remainder of 36 
divided by each number in numb. For example, the first element should be 0, because 36/6 has no remainder. 
If there is an error, have the string “Error” appear in the remainder.
"""
def remainder():
    numb = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]
    remainder = list()
    for num in numb:
        try:
            remainder.append(36%num)
        except Exception as e:
            remainder.append("Error")
            print(e)
    return remainder
#print(remainder())
"""
4. The buggy code below prints out the value of the sport in the list sport. Use try/except so that the code 
will run properly. If the sport is not in the dictionary, ppl_play, add it in with the value of 1.
"""
def in_a_dic():
    sport = ["hockey", "basketball", "soccer", "tennis", "football", "baseball"]
    ppl_play = {"hockey":4, "soccer": 10, "football": 15, "tennis": 8}

    for x in sport:
        try:
            print(ppl_play[x])
        except:
            ppl_play[x] = 1
    return (ppl_play)
#print(in_a_dic())
