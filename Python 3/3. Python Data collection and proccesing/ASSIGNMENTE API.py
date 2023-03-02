# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:37:43 2020

@author: pipem
"""

import requests
import json

"""
Define a function, called get_movies_from_tastedive. It should take one input parameter, a string that is the 
name of a movie or music artist. The function should return the 5 TasteDive results that are associated with 
that string; be sure to only get movies, not other kinds of media. It will be a python dictionary with just 
one key, ‘Similar’.
"""


def get_movies_from_tastedive(movie_music_name):
    base_url = "https://tastedive.com/api/similar"
    param_as_dic = dict()
    param_as_dic["q"] = movie_music_name
    param_as_dic["type"] = "movies"
    param_as_dic["limit"] = 5
    reque = requests.get(base_url, params=param_as_dic)

    # print(reque.url)
    py_object = json.loads(reque.text)

    # to_string = json.dumps(py_object, indent = 4) por si quiero verlo organizado
    return py_object


#print(get_movies_from_tastedive("Black Panther"))
"""
Please copy the completed function from above into this active code window. Next, you will need to write a 
function that extracts just the list of movie titles from a dictionary returned by get_movies_from_tastedive. 
Call it extract_movie_titles.
"""


def extract_movie_titles(movie_name):
    dic_of_movies = get_movies_from_tastedive(movie_name)
    # to_string = json.dumps(dic_of_movies, indent = 4) por si quiero verlo organizado
    # print(to_string)
    # retorna una lista dentro de la KEY "Similar"
    similar = dic_of_movies["Similar"]["Results"]
    # print(similar)
    list_of_movies = list()
    for movie in similar:
        list_of_movies.append(movie["Name"])

    return list_of_movies

#print(extract_movie_titles("Black Panther"))


"""
Please copy the completed functions from the two code windows above into this active code window. 
Next, you’ll write a function, called get_related_titles. It takes a list of movie titles as input. 
It gets five related movies for each from TasteDive, extracts the titles for all of them, and combines 
them all into a single list. Don’t include the same movie twice.
"""


def get_related_titles(list_of_movies):
    single_list = list()
    for movie in list_of_movies:
        # tengo una lista por cada nombre de pelicula entrado como parametro
        names = extract_movie_titles(movie)
        # print(names)
        for name in names:
            if name in single_list:
                continue
            single_list.append(name)
    return single_list
#print(get_related_titles(["Black Panther", "Captain Marvel"]))


"""
Define a function called get_movie_data. It takes in one parameter which is a string that should represent the 
title of a movie you want to search. The function should return a dictionary with information about that movie.

Again, use requests_with_caching.get(). For the queries on movies that are already in the cache, 
you won’t need an api key. You will need to provide the following keys: t and r. As with the TasteDive cache, 
be sure to only include those two parameters in order to extract existing data from the cache.
"""


def get_movie_data(movie_tittle):
    base_url = "http://www.omdbapi.com/"
    param_as_dic = dict()
    param_as_dic["t"] = movie_tittle
    param_as_dic["r"] = "json"
    param_as_dic["apikey"] = "fec40cad"  # para aprender a usar la key jeje
    reque = requests.get(base_url, params=param_as_dic)
    py_object = json.loads(reque.text)

    # to_string = json.dumps(py_object, indent = 4) por si quiero verlo organizado
    return py_object
#print(get_movie_data("Baby Mama"))


"""
Please copy the completed function from above into this active code window. Now write a function called 
get_movie_rating. It takes an OMDB dictionary result for one movie and extracts the 
Rotten Tomatoes rating as an integer. For example, if given the OMDB dictionary for “Black Panther”, 
it would return 97. If there is no Rotten Tomatoes rating, return 0.
"""


def get_movie_rating(movie):
    rotten_tomato = 0
    info_of_movie = get_movie_data(movie)
    ratings = info_of_movie["Ratings"]
    for rate in ratings:
        if rate["Source"] == "Rotten Tomatoes":
            rotten_tomato = int(rate["Value"][:-1])

    return rotten_tomato


# print(get_movie_rating("Venom"))
"""

Now, you’ll put it all together. Don’t forget to copy all of the functions that you have previously defined 
into this code window. Define a function get_sorted_recommendations. It takes a list of movie titles as an input.
It returns a sorted list of related movie titles as output, up to five related movies for each input movie title. 
The movies should be sorted in descending order by their Rotten Tomatoes rating, 
as returned by the get_movie_rating function. Break ties in reverse alphabetic order, 
so that ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’.
"""


def get_sorted_recommendations(list_of_movies):
    related_movies = get_related_titles(list_of_movies)
    best_sort = sorted(related_movies, key=lambda name: (
        get_movie_rating(name), name), reverse=True)
    # sorte por el rate de la pelicula y si eran iguales por el nombre en orden alfabetico
    return best_sort


print(get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"]))
