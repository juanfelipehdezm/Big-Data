from pyspark.sql.session import SparkSession
from pyspark.sql.context import SQLContext
from pyspark.sql.types import IntegerType, FloatType, LongType, StructField, StructType

# Creating spark session
spark = SparkSession.builder.appName("Movies").getOrCreate()
sqlcontext = SQLContext(spark)

# schema for the data when reading
schema = StructType([StructField("userId", IntegerType(), True),
                    StructField("movieId", IntegerType(), True),
                    StructField("rating", FloatType(), True),
                    StructField("timestamp", LongType(), True)])

"""
One intent to do it but did not work, anyways the function do works so lets keep it 
def movies_dict() -> dict:
    # passing from pyspark df to dict
    moviesDF = sqlcontext.read.csv(
        "G://Mi unidad//Big data//Spark//Advance_spark//movies.csv",
        header=True)
    return {
        int(row["movieId"]): [row["title"], row["genres"]]
        for row in moviesDF.collect()
    }"""

# loading ratings csv file
ratesDF = sqlcontext.read.csv(
    "G://Mi unidad//Big data//Spark//Advance_spark//ratings.csv",
    header=True, schema=schema)
# movies df
moviesDF = sqlcontext.read.csv(
    "G://Mi unidad//Big data//Spark//Advance_spark//movies.csv",
    header=True)

# joinning the two data sources
fullDF = ratesDF.join(
    moviesDF, ratesDF["movieId"] == moviesDF["Id"], "inner").drop("Id")

movies_frecuency = fullDF.groupBy("movieId", "title", "genres").count().orderBy(
    "count", ascending=False)

print(movies_frecuency.show(10))
# the movie 365 was rated 329 times

spark.stop()
