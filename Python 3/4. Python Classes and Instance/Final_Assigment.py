# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 10:13:03 2020

@author: pipem
"""
import random
VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'
"""
Part A: WOFPlayer

We’re going to start by defining a class to represent a Wheel of Fortune player, called WOFPlayer. 
Every instance of WOFPlayer has three instance variables:

.name: The name of the player (should be passed into the constructor)

.prizeMoney: The amount of prize money for this player (an integer, initialized to 0)

.prizes: The prizes this player has won so far (a list, initialized to [])

Of these instance variables, only name should be passed into the constructor.

It should also have the following methods (note: we will exclude self in our descriptions):

.addMoney(amt): Add amt to self.prizeMoney

.goBankrupt(): Set self.prizeMoney to 0

.addPrize(prize): Append prize to self.prizes

.__str__(): Returns the player’s name and prize money in the following format:
Steve ($1800) (for a player with instance variables .name == 'Steve' and prizeMoney == 1800)
"""
class WOFPlayer():
    def __init__ (self,name, prizeMoney = 0 , prizes = list()):
        self.name = name
        self.prizeMoney = 0
        self.prizes = list()
        
    def addMoney(self,amt):
        self.prizeMoney += amt
        return self.prizeMoney
    
    def goBankrupt(self):
        self.prizeMoney = 0
        return self.prizeMoney
    
    def addPrize(self,prize):
        return self.prizes.append(prize)
    
    def __str__(self):
        return "{} (${})".format(self.name,self.prizeMoney)
    
#p1 = WOFPlayer("Steve")
#print(p1)

"""
Part B: WOFHumanPlayer

Next, we’re going to define a class named WOFHumanPlayer, which should inherit from WOFPlayer (part A). 
This class is going to represent a human player. In addition to having all of the instance variables and methods 
that WOFPlayer has, WOFHumanPlayer should have an additional method:

.getMove(category, obscuredPhrase, guessed): Should ask the user to enter a move (using input()) and 
return whatever string they entered.

.getMove()’s prompt should be:

    {name} has ${prizeMoney}

    Category: {category}
    Phrase:  {obscured_phrase}
    Guessed: {guessed}
    Guess a letter, phrase, or type 'exit' or 'pass':

For example:

    Steve has $200

    Category: Places
    Phrase: _L___ER N____N_L P_RK
    Guessed: B, E, K, L, N, P, R, X, Z
    Guess a letter, phrase, or type 'exit' or 'pass':

The user can then enter:

'exit' to exit the game

'pass' to skip their turn

a single character to guess that letter

a complete phrase (a multi-character phrase other than 'exit' or 'pass') to guess that phrase

Note that .getMove() does not need to enforce anything about the user’s input; that will be done via the game logic that we define in the next ActiveCode window.
"""

class WOFHumanPlayer(WOFPlayer):
    def __init__(self, name):
        WOFPlayer.__init__(self,name)
    
    def getMove(self,category, obscuredPhrase, guesse):
        print("""
              {} has ${}

              Category: {}
              Phrase:  {}
              Guessed: {}
              """.format(self.name,self.prizeMoney,category,obscuredPhrase,guesse)
              )
        guess = input("Guess a letter, phrase, or type 'exit' or 'pass': ")
        return guess
"""
Part C: WOFComputerPlayer

Finally, we’re going to define a class named WOFComputerPlayer, which should inherit from WOFPlayer (part A). 
This class is going to represent a computer player.

Every computer player will have a difficulty instance variable. Players with a higher difficulty generally play 
“better”. There are many ways to implement this. We’ll do the following:

If there aren’t any possible letters to choose (for example: if the last character is a vowel but this player 
                                                doesn’t have enough to guess a vowel), we’ll 'pass'

Otherwise, semi-randomly decide whether to make a “good” move or a “bad” move on a given turn
 (a higher difficulty should make it more likely for the player to make a “good” move)
To make a “bad” move, we’ll randomly decide on a possible letter.

To make a “good” move, we’ll choose a letter according to their overall frequency in the English language.

In addition to having all of the instance variables and methods that WOFPlayer has, 
WOFComputerPlayer should have:

Class variable

.SORTED_FREQUENCIES: Should be set to 'ZQXJKVBPYGFWMUCLDRHSNIOATE', which is a list of English characters sorted
from least frequent ('Z') to most frequent ('E'). We’ll use this when trying to make a “good” move.

Additional Instance variable

.difficulty: The level of difficulty for this computer (should be passed as the second argument into the 
                                                        constructor after .name)

Methods

.smartCoinFlip(): This method will help us decide semi-randomly whether to make a “good” or “bad” move. 
A higher difficulty should make us more likely to make a “good” move. Implement this by choosing a random number
 between 1 and 10 using random.randint(1, 10) (see above) and returning True if that random number is greater
 than self.difficulty. If the random number is less than or equal to self.difficulty, return False.

.getPossibleLetters(guessed): This method should return a list of letters that can be guessed.
These should be characters that are in LETTERS ('ABCDEFGHIJKLMNOPQRSTUVWXYZ') but not in the guessed parameter.

Additionally, if this player doesn’t have enough prize money to guess a vowel (variable VOWEL_COST set to 250), 
then vowels (variable VOWELS set to 'AEIOU') should not be included

.getMove(category, obscuredPhrase, guessed): Should return a valid move.
Use the .getPossibleLetters(guessed) method described above.

If there aren’t any letters that can be guessed (this can happen if the only letters left to guess are vowels 
                                                 and the player doesn’t have enough for vowels), return 'pass'

Use the .smartCoinFlip() method to decide whether to make a “good” or a “bad” move
If making a “good” move (.smartCoinFlip() returns True), then return the most frequent 
(highest index in .SORTED_FREQUENCIES) possible character

If making a “bad” move (.smartCoinFlip() returns False), then return a random character from the set of possible 
characters (use random.choice())
"""
class WOFComputerPlayer(WOFPlayer):
    #Class vairables:
    SORTED_FREQUENCIES = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def __init__(self, name,difficulty):
        WOFPlayer.__init__(self,name)
        self.difficulty = difficulty
    
    def smartCoinFlip(self):
        if  random.randint(1, 10) > self.difficulty:
            return True
        else:
            return False
    
    def getPossibleLetters(self, guessed):
        remainingLetters = []
        for letter in LETTERS:
            if letter not in guessed:
                remainingLetters.append(letter)
        
        if self.prizeMoney < VOWEL_COST:
            for vowel in VOWELS:
                if vowel in remainingLetters:
                    remainingLetters.remove(vowel)
        return remainingLetters
    
    def getMove(self, category, obscuredPhrase, guessed = list()):
        
        if len(self.getPossibleLetters(guessed)) == 0:
            return "pass"
        elif self.smartCoinFlip():
            for letter in self.SORTED_FREQUENCIES[::-1]:
                if letter in self.getPossibleLetters():
                    return letter
        else:
            return random.choice(self.getPossibleLetters())
        
            