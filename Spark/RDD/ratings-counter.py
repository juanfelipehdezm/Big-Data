from pyspark import SparkConf, SparkContext
from pyspark.sql.context import SQLContext
from pyspark.sql.session import SparkSession

conf = SparkConf().setMaster("local").setAppName("RatingsHistogram")
sc = SparkContext(conf=conf)
sqlcontext = SQLContext(sc)
spark = SparkSession(sc)

df = sqlcontext.read.csv(
    "G://Mi unidad//Big data//Spark//ml-latest-small//RDD//ratings.csv", header=True)

rating = df.select("rating").rdd
sorted_ratings = sorted(rating.countByKey().items())

for k, v in sorted_ratings:
    print(k, v)
