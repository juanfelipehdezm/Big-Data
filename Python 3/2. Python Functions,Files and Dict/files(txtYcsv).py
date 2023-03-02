# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 16:44:01 2020

@author: pipem
"""

"""
The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary.
Find the total number of characters in the file and save to the variable num.
"""
def numCharInTheFile():
    fhand = open("travel_plans.txt","r")
    cont = fhand.read()
    num = len(cont)
    print(num)
    fhand.close()
#numCharInTheFile() Es un ejemplo, el file en realidad no lo tengo 

"""
We have provided a file called emotion_words.txt that contains lines of words that describe emotions.
Find the total number of words in the file and assign this value to the variable num_words.
"""
def numOfWords():
    fhand = open("emotion_words.txt","r")
    lines = fhand.read().split()
    num_words = len(lines)
    print(num_words)
    fhand.close()
#numOfWords() Es un ejemplo, el file no lo tengo en realidad 

"""
Assign to the variable num_lines the number of lines in the file school_prompt.txt.
"""
def numOfLines():
    fhand = open("school_prompt.txt","r")
    lines = fhand.readlines()
    num_lines = len(lines)
    print(num_lines)
    fhand.close
#numOfLines() Es un ejemplo, el file no lo tengo en realidad 

"""
Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
"""
def first30Chars():
    fhand = open("school_prompt.txt","r")
    content = fhand.read()
    beginning_chars = content[:30]
    print(beginning_chars)
    fhand.close()
#first30Chars() De nuevo es un ejemplo

"""
Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called
three.
"""
def thirdList():
    fhand = open("school_prompt.txt","r")
    three = list()
    for lines in fhand:
        words = lines.split()
        three.append(words[2])
    print(three)
    fhand.close()
# es un ejemplo 

"""
Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, 
then add the word to a list called p_words.
"""
def IfLetterIn():
    
    fhand = open('school_prompt.txt','r')
    p_words = list()
    text = fhand.read()
    content = text.split()
    for word in content:
        if 'p' in word:
            p_words.append(word)
    print(p_words)
    fhand.close()
# EJMPLO 
