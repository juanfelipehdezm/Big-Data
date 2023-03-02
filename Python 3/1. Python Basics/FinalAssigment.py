# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 17:27:13 2020

@author: pipem
"""

"""
Below are a set of scores that students have received in the past semester.
Write code to determine how many are 90 or above and assign that result to the value a_scores.
"""


def countingScores():
    scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
    lst = scores.split()
    print(lst)  # solo para asegurar creacion de la lista
    total_90_or_above = 0
    for num in lst:
        if int(num) >= 90:
            total_90_or_above += 1
    print(total_90_or_above)
# countingScores()


"""
Provided is a list of data about a store’s inventory where each item in the list represents
the name of an item, how much is in stock, and how much it costs. Print out each item in 
the list with the same formatting, using the .format method (not string concatenation). 
For example, the first print statment should read The store has 12 shoes, each for 29.99 USD.
"""


def formatTask():
    inventory = [("shoes", 12, 29.99), ("shirts", 20, 9.99),
                 ("sweatpants", 25, 15.00), ("scarves", 13, 7.75)]
    for item in inventory:
        name = item[0]
        cant = item[1]
        price = item[2]
        print("The store has {} {}, each for {:.2f} USD".format(cant, name, price))


formatTask()

"""
Write code that uses the string stored in org and creates an acronym which is assigned 
to the variable acro. Only the first letter of each word should be used, 
each letter in the acronym should be a capital letter, and there should be nothing to separate 
the letters of the acronym. Words that should not be included in the acronym are stored in the 
list stopwords. For example, if org was assigned the string “hello to world” then 
the resulting acronym should be “HW”.
"""


def acrom():
    stopwords = ['to', 'a', 'for', 'by', 'an',
                 'am', 'the', 'so', 'it', 'and', "The"]
    org = "The organization for health, safety, and education"

    in_org = org.split()
    print(in_org)
    acro = ''
    for letter in in_org:
        if letter not in stopwords:
            acro = acro + letter[0].upper()
    print(acro)
# acrom()


"""
Write code that uses the string stored in sent and creates an acronym which is assigned 
to the variable acro. The first two letters of each word should be used, each letter in 
the acronym should be a capital letter, and each element of the acronym should be separated 
by a “. ” (dot and space). Words that should not be included in the acronym are stored in the
list stopwords. For example, if sent was assigned the string “height and ewok wonder” 
then the resulting acronym should be “HE. EW. WO”.
"""


def acrom2():
    stopwords = ['to', 'a', 'for', 'by', 'an',
                 'am', 'the', 'so', 'it', 'and', "The"]
    sent = "The water earth and air are vital"

    in_org = sent.split()
    print(in_org)
    temp = ""
    for letter in in_org:
        if letter not in stopwords:
            temp = temp + letter[:2].upper() + ". "
    acro = temp[:18]
    print(acro)
# acrom2()


"""
A palindrome is a phrase that, if reversed, would read the exact same.
Write code that checks if p_phrase is a palindrome by reversing it and then 
checking if the reversed version is equal to the original. 
Assign the reversed version of p_phrase to the variable r_phrase so that we can check your work.
"""


def palindrome():
    p_phrase = "was it a car or a cat I saw"
    r_phrase = p_phrase[::-1]  # Asi se voltea el String
    print(r_phrase)
    print(r_phrase == p_phrase)
# palindrome()
