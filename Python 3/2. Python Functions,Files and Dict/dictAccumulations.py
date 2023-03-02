# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 15:10:57 2020

@author: pipem
"""

"""
1. The dictionary travel contains the number of countries within each continent that Jackie
has traveled to. Find the total number of countries that Jackie has been to, 
nd save this number to the variable name total. Do not hard code this!
"""

def sumOfValues():
    travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa":1, "Antarctica": 0, "Australia": 1}
    values = list(travel.values())
    total = 0 
    for v in values: 
        total += v 
    print("Jacke has been in",total,"countries")
#sumOfValues()
"""
Create a dictionary called d that keeps track of all the characters in the string placement 
and notes how many times each character was seen. Then, find the key with the lowest value in 
this dictionary and assign that key to min_value.
"""

def lessFrecuent():
    placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
    char_dic = dict()
    for char in placement:
        if char not in char_dic:
            char_dic[char] = 0
        char_dic[char] += 1
    #print (char_dic)
    
    keys = list(char_dic.keys())
    print(keys)
    min_value = keys[0]
    for key in keys:
        if char_dic[key] < char_dic[min_value]:
            min_value = key 
    print ( min_value,":", char_dic[min_value])
#lessFrecuent()

"""
Create a dictionary, freq, that displays each character in string str1 as the key and its 
frequency as the value.
"""
def newDic():
    str1 = "peter piper picked a peck of pickled peppers"
    freq = dict()
    for char in str1:
        if char not in freq:
            freq[char]= 0
        freq[char] += 1
    print(freq)
#newDic()
"""
Create a dictionary, freq_words, that contains each word in string str1 as the key and its 
frequency as the value.
"""
def newDic2():
    str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
    freq_words = dict()
    words = str1.split()
    for wrd in words: 
        if wrd not in freq_words:
            freq_words[wrd] = 0 
        freq_words[wrd] += 1
    print(freq_words)
#newDic2()

"""
Create the dictionary characters that shows each character from the string sally and its frequency. 
Then, find the most frequent letter based on the dictionary. Assign this letter to the variable 
best_char.
"""
def moreFrecuent():
    sally = "sally sells sea shells by the sea shore"
    characters = dict()
    for char in sally:
        if char not in characters:
            characters[char]=0
        characters[char]+=1
    print(characters)
    
    keys = list(characters.keys()) # se crea lista de keys
    best_char = keys[0]
    for key in keys:
        if characters[key] > characters[best_char]:
            best_char = key
    print("The more frequent word is:",best_char,"=",characters[best_char])
#moreFrecuent()
"""
Create a dictionary named letter_counts that contains each letter and the number of times it 
occurs in string1. Challenge: Letters should not be counted separately as upper-case and lower-case.
Instead, all of them should be counted as lower-case.
"""
def notUpperCase():
    string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
    lower_case = string1.lower() #pasamos todas a minustulas
    #print(lower_case) para comprobar
    letter_counts = dict()
    for char in lower_case:
        if char not in letter_counts:
            letter_counts[char] = 0
        letter_counts[char] += 1
    print(letter_counts)
#notUpperCase()

"""
Create a dictionary called low_d that keeps track of all the characters in the string p and notes 
how many times each character was seen. Make sure that there are no repeats of characters as keys, 
such that “T” and “t” are both seen as a “t” for example.
"""
def notRepeatChar():
    p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
    char_count = dict()
    for char in p:
        if char in char_count:
            continue
        elif char not in char_count:
            char_count[char] = 0
        char_count[char] =+ 1
    print(char_count)
#notRepeatChar() JAJAJ no se pa que sirve pero solo cuenta una vez cada char 