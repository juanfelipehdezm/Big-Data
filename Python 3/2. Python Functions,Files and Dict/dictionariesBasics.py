# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 11:31:36 2020

@author: pipem
"""

"""
At the halfway point during the Rio Olympics, the United States had 70 medals, 
Great Britain had 38 medals, China had 45 medals, Russia had 30 medals, and Germany had 17 medals.
Create a dictionary assigned to the variable medal_count with the country names as the keys and 
the number of medals the country had as each key’s value.
"""
def creatDic():
    medal_count = dict()
    medal_count["United States"] = 70
    medal_count["Great Britain"] = 38
    medal_count["China"] = 45
    medal_count["Russia"] = 30
    medal_count["Germany"] = 17
    print(medal_count)
#creatDic()

"""
Given the dictionary swimmers, add an additional key-value pair to the dictionary with 
"Phelps" as the key and the integer 23 as the value. Do not rewrite the entire dictionary.
"""
def newKey():
     swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4}
     swimmers["Phelps"] = 23
     print(swimmers)
#newKey()

"""
The dictionary golds contains information about how many gold medals each country
won in the 2016 Olympics. But today, Spain won 2 more gold medals.
Update golds to reflect this information.
"""
def updateDic():
    golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}
    golds["Spain"] = golds["Spain"] + 2
    print(golds)
#updateDic()

"""
Create a list of the countries that are in the dictionary golds, and assign that list to the 
variable name countries. Do not hard code this.
"""
def listOfKeys():
    golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}
    countries = list(golds.keys())
    print(countries)
#listOfKeys()

"""
Provided is the dictionary, medal_count, which lists countries and their respective medal count 
at the halfway point in the 2016 Rio Olympics. Using dictionary mechanics, 
assign the medal count value for "Belarus" to the variable belarus. 
Do not hardcode this.
"""

def xyz():
    medal_count = {'United States': 70, 'Great Britain':38, 'China':45, 'Russia':30, 'Germany':17, 'Italy':22, 'France': 22, 'Japan':26, 'Australia':22, 'South Korea':14, 'Hungary':12, 'Netherlands':10, 'Spain':5, 'New Zealand':8, 'Canada':13, 'Kazakhstan':8, 'Colombia':4, 'Switzerland':5, 'Belgium':4, 'Thailand':4, 'Croatia':3, 'Iran':3, 'Jamaica':3, 'South Africa':7, 'Sweden':6, 'Denmark':7, 'North Korea':6, 'Kenya':4, 'Brazil':7, 'Belarus':4, 'Cuba':5, 'Poland':4, 'Romania':4, 'Slovenia':3, 'Argentina':2, 'Bahrain':2, 'Slovakia':2, 'Vietnam':2, 'Czech Republic':6, 'Uzbekistan':5}
    belarus = medal_count["Belarus"]
    print(belarus)   
#xyz()