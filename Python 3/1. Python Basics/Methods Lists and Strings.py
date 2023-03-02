# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 16:01:01 2020

@author: pipem
"""
"""
Write code to add ‘horseback riding’ to the second position
(i.e., right before volleyball) in the list sports
"""

def addSecondPos():
    sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
    sports.insert(2,"horseback riding")
    print(sports)
#addSecondPos()

"""
Write code to take ‘London’ out of the list trav_dest.
"""
def takeOut():
    trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'London', 'Melbourne']
    trav_dest.remove("London")
    print(trav_dest)
#takeOut()

"""
Write code to add ‘Guadalajara’ to the end of the list trav_dest using a list method.
"""

def addToTheEnd():
    trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'Melbourne']
    trav_dest.append("Guadalajara")
    print(trav_dest)
#addToTheEnd()

"""
Write code to rearrange the strings in the list winners so that they are in
alphabetical order from A to Z.
"""
def alphabetical():
    winners = ['Kazuo Ishiguro', 'Rainer Weiss', 'Youyou Tu', 'Malala Yousafzai', 'Alice Munro', 'Alvin E. Roth']
    winners.sort()
    print(winners)
#alphabetical()
"""
Write code to rearrange the strings in the list winners so that they are in
alphabetical order from Z to A.
"""
def fromZtoA():
    winners = ['Kazuo Ishiguro', 'Rainer Weiss', 'Youyou Tu', 'Malala Yousafzai', 'Alice Munro', 'Alvin E. Roth']
    winners.sort(reverse=True)
    print(winners)
#fromZtoA()

"""
Currently there is a string called str1. Write code to create a list called chars 
which should contain the characters from str1. Each character in str1 
should be its own element in the list chars.
"""

def charsList():
    str1 = "I love python"
    chars = list()
    for letter in str1:
        chars.append(letter)
    print(chars)
#charsList()
"""
For each string in wrds, add ‘ed’ to the end of the word (to make the word past tense).
 Save these past tense words to a list called past_wrds.
"""
def addEd(): 
    wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
    past_wrds= list() 
    for word in wrds: 
        past_wrds.append(word + "ed")
    print(past_wrds)
#addEd()