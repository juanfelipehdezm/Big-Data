# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:50:34 2020

@author: pipem
"""
import requests
import json


def getInfoFromApi():

    page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
    print(type(page))

    print(page.url) # print the url that was fetched
    print("------")
    x = json.loads(page.text) # turn page.text into a python object
    print(type(x))

    print("---the whole list, pretty printed---")
    return json.dumps(x, indent=2) # pretty print the results
#print(getInfoFromApi())

"""
Suppose you were writing a computer program that was going to automatically translate paragraphs of text into 
paragraphs with similar meanings but with more rhymes. You would want to contact the datamuse API repeatedly, 
passing different values associated with the key rel_rhy. Let’s make a python function to do that. 
You can think of it as a wrapper for the call to requests.get.
"""
def get_rhymes(word):
    baseurl = "https://api.datamuse.com/words" #URL base que no cambia de la API
    params_diction = dict() # Set up an empty dictionary for query parameters
    params_diction["rel_rhy"] = word #word con la que quiero encontrar que rime
    params_diction["max"] = "3" # get at most 3 results
    resp = requests.get(baseurl, params=params_diction) #los parametros se sacan de la documentacion de la API
    # return the top three words
    print(resp.url)
    word_ds = json.loads(resp.text) #cargo la info del url en un python object
    
    return [d['word'] for d in word_ds] #sabemos que las palabras estan dentro de un dic con key = "word"
#print(get_rhymes("funny"))


"""
 with itunes API 
"""
def itunesApi():
    parameters = {"term": "Ann Arbor", "entity": "podcast"}
    iTunes_response = requests.get("https://itunes.apple.com/search", params = parameters)

    py_data = json.loads(iTunes_response.text)
    for r in py_data['results']:
        return r['trackName']
    
print(itunesApi())