from sre_parse import SPECIAL_CHARS
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("WordCount")
sc = SparkContext(conf=conf)

lines = sc.textFile("G://Mi unidad//Big data//Spark//RDD//Book.txt")

# CLEANING, removing special characteres and standarizing the case


def upper_clear_str(word: str) -> str:
    special_characteres = '!"#$%&\'()*+,./:;<=>?@[\\]^_`{|}~-'
    uppercased_str = word.upper()
    for sch in special_characteres:
        uppercased_str = uppercased_str.replace(sch, "")
    return uppercased_str.split()


words_rdd = lines.flatMap(upper_clear_str)
# print(words.take(10))

words_key_value = words_rdd.map(lambda x: (x, 1))
# print(words_key_value.take(20))
word_count = words_key_value.reduceByKey(lambda x, y: x + y)
# print(word_count.take(20))
# flipping to coonver the sum in the keys
word_count_sorted = word_count.map(lambda x: (x[1], x[0])).sortByKey(False)
print(word_count_sorted.take(20))
