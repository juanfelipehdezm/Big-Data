# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 16:59:09 2020

@author: pipem
"""

"""
To start, define a function called strip_punctuation which takes one parameter, a string which 
represents a word, and removes characters considered punctuation from everywhere in the word. 
(Hint: remember the .replace() method for strings.)
"""
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", "#", "@"]

def strip_punctuation(strg):
    for char in punctuation_chars:
        strg = strg.replace(char,"")
        
    return strg
    
#print(strip_punctuation("#in.cred..ible"))

"""
Next, copy in your strip_punctuation function and define a function called get_pos which takes one 
parameter, a string which represents one or more sentences, and calculates how many words in the 
string are considered positive words. Use the list, positive_words to determine what words will 
count as positive. The function should return a positive integer - how many occurrences there 
are of positive words in the text. Note that all of the words in positive_words are lower cased, 
so you’ll need to convert all the words in the input string to lower case as well.
"""
# list of positive words to use
positive_words = list()
with open("positive_words.txt","r") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
    #print(positive_words)

def get_pos(strg1):
    c = 0
    strg1 = strg1.lower()
    lst = strg1.split()
    for word in lst:
        word = strip_punctuation(word)
        if word in positive_words:
            c += 1
    return c 

"""
Next, copy in your strip_punctuation function and define a function called get_neg which takes one 
parameter, a string which represents one or more sentences, and calculates how many words in the 
string are considered negative words. Use the list, negative_words to determine what words will 
count as negative. The function should return a positive integer - how many occurrences there are 
of negative words in the text. Note that all of the words in negative_words are lower cased, 
so you’ll need to convert all the words in the input string to lower case as well.
"""
# list of negative words to use
negative_words = []
with open("negative_words.txt","r") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
    #print(negative_words)
    
def get_neg(strg2):
    c = 0
    strg2 = strg2.lower()
    lst = strg2.split()
    for word in lst:
        word = strip_punctuation(word)
        if word in negative_words:
            c += 1
    return c 

#print(get_neg("their departure was rather abrupt. However, it was amusing how aloof they had been."))
#To proof it works and it does

"""
Finally, copy in your previous functions and write code that opens the file project_twitter_data.csv 
which has the fake generated twitter data (the text of a tweet, the number of retweets of that tweet,
and the number of replies to that tweet). Your task is to build a sentiment classifier, 
which will detect how positive or negative each tweet is. Copy the code from the code windows above,
and put that in the top of this code window. Now, you will write code to create a csv file called 
resulting_data.csv, which contains the Number of Retweets, Number of Replies, 
Positive Score (which is how many happy words are in the tweet), 
Negative Score (which is how many angry words are in the tweet), 
and the Net Score (how positive or negative the text is overall) for each tweet. 
The file should have those headers in that order.
Remember that there is another component to this project. 
You will upload the csv file to Excel or Google Sheets and produce a graph of the 
Net Score vs Number of Retweets. Check Coursera for that portion of the assignment, 
if you’re accessing this textbook from Coursera.
"""
twi_data = open("project_twitter_data.csv","r") # Funciona pero traje mal el archivo pero en general es asi
lines = twi_data.readlines()

for line in lines[1:]:
    line = line.strip().split(",")
    num_retw = line[1]
    #print(num_retw)
    num_repl = line[2]
    #print(num_repl)
    pos_score = get_pos(line[0])
    neg_score = get_neg(line[0])
    net_score = pos_score - neg_score

resul_tw_data = open("resulting_data.csv","w") 
resul_tw_data.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score") 
resul_tw_data.write("\n")
   
info = "{}{}{}{}{}".format(num_retw,num_repl,pos_score,neg_score,net_score)
resul_tw_data.write(info)
resul_tw_data.write("\n")

resul_tw_data.close()
twi_data.close()


    