# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 10:11:52 2020

@author: pipem
"""

"""
The class, Pokemon, is provided below and describes a Pokemon and its leveling and evolving characteristics. 
An instance of the class is one pokemon that you create.

Grass_Pokemon is a subclass that inherits from Pokemon but changes some aspects, for instance, 
the boost values are different.

For the subclass Grass_Pokemon, add another method called action that returns the string 
"[name of pokemon] knows a lot of different moves!". Create an instance of this class with the name as "Belle". 
Assign this instance to the variable p1.
"""

class Pokemon(object):
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name, level = 5):
        self.name = name
        self.level = level

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level%self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10
        
    def opponent(self):
        if self.p_type == "Grass":
            return ("Fire","Water")
        elif self.p_type == "Ghost":
            return ("Dark","Psychic")
        elif self.p_type == "Fire":
            return ("Water","Grass")
        elif self.p_type == "Flying":
            return ("Electric","Fighting")

    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

class Grass_Pokemon(Pokemon): #heredando
    attack = 15
    defense = 14
    health = 12
    p_type = "Grass"
    
    def __init__(self, name,level = 5):
        Pokemon.__init__(self,name,level=5) #invocamos el constructor de Pokemon

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]
        
    def attack_up(self):
        if self.level >= 10:
            Pokemon.attack_up(self)
            return self.attack
        
    def action(self):
        return "{} knows a lot of different moves!".format(self.name)
    
p1= Grass_Pokemon("Belle",4)
print(p1.action())
print(p1.opponent())
p2 = Grass_Pokemon('Bulby')
p3 = Grass_Pokemon('Pika')
for n in range(10):
  p3.train()
print(p1, p2, p3)