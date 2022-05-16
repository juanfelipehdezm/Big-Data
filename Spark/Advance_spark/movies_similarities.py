from unittest import result
from pyspark.sql.session import SparkSession
from pyspark.sql.context import SQLContext
from pyspark.sql.types import StructField, StructType, IntegerType, StringType, LongType, FloatType
from pyspark.sql import functions as func
import sys


def computeCosineSimilarity(spark, data):
    # Compute xx, xy, and yy columns
    pairScores = data.withColumn("xx", data["ratings1"] * data["ratings1"])\
                     .withColumn("yy", data["ratings2"] * data["ratings2"])\
                     .withColumn("xy", data["ratings1"] * data["ratings2"])

    # Compute numerator, denominator and numPairs columns
    calculateSimilarity = pairScores.groupBy("movie1", "movie2").agg(
        func.sum("xy").alias("numerator"),
        (func.sqrt(func.sum("xx")) *
         func.sqrt(func.sum("yy"))).alias("denominator"),
        func.count("xy").alias("numPairs")
    )

    # Calculate score and select only needed columns (movie1, movie2, score, numPairs)
    return calculateSimilarity.withColumn(
        "score",
        func.when(
            calculateSimilarity["denominator"] != 0, calculateSimilarity["numerator"] /
            calculateSimilarity["denominator"]
        ).otherwise(0),
    ).select("movie1", "movie2", "score", "numPairs")

# Get movie name by given movie id


def getMovieName(movieNames, movieId):
    return movieNames.filter(movieNames["Id"] == movieId).select(
        "title").first()


# the master("local[*]") is to use every CPU core on the local system this is bc I am gg use a join computencionally demanding
# take in count this will make the program run only the local machine and not in the other machines in the cluster
spark = SparkSession.builder.appName(
    "movies similirity").master("local[*]").getOrCreate()
sqlcontext = SQLContext(spark)

# structuring and loading movies and rating data frames

moviesNameSchema = StructType([StructField("Id", IntegerType(), True),
                               StructField("title", StringType(), True),
                               StructField("genres", StringType(), True)])

moviesRatingSchema = StructType([StructField("userId", IntegerType(), True),
                                 StructField("movieId", IntegerType(), True),
                                 StructField("rating", FloatType(), True),
                                 StructField("timestamp", LongType(), True)])

moviesDF = sqlcontext.read.csv("G://Mi unidad//Big data//Spark//Advance_spark//ratings.csv",
                               header=True, schema=moviesNameSchema)

ratingsDF = sqlcontext.read.csv("G://Mi unidad//Big data//Spark//Advance_spark//ratings.csv",
                                header=True, schema=moviesRatingSchema).select("userId", "movieId", "rating")


# Emit evety movie rated together by the same user but avoiding duplicates
# self join to find every combination
# Select movie pair and rating pair
moviePairs = ratingsDF.alias("ratings1").join(ratingsDF.alias("ratings2"), (func.col("ratings1.userId") == func.col("ratings2.userId")) & (func.col("ratings1.movieId") < func.col("ratings2.movieId")))\
    .select(func.col("ratings1.movieId").alias("movie1"),
            func.col("ratings2.movieId").alias("movie2"),
            func.col("ratings1.rating").alias("ratings1"),
            func.col("ratings2.rating").alias("ratings2"))

# print(moviePairs.show())

moviePairSimilarities = computeCosineSimilarity(spark, moviePairs).cache()

if len(sys.argv) > 1:
    scoreThreshold = 0.97  # similarity score above 97%
    coOccurrenceThreshold = 50.0  # at least 50 user view both movies

    movieID_recommendations = int(sys.argv[1])

    # Filter for movies with similarity "good" as defined
    filteredResults = moviePairSimilarities.filter(
        ((moviePairSimilarities["movie1"] == movieID_recommendations) | (moviePairSimilarities["movie2"] == movieID_recommendations)) &
        (moviePairSimilarities["score"] > scoreThreshold) & (moviePairSimilarities["numPairs"] > coOccurrenceThreshold))

    results = filteredResults.sort(func.col("score").desc()).take(10)

    print("TOP 10 SIMILAR MOVIES FOR ", getMovieName(
        moviesDF, movieID_recommendations))

    for result in results:
        # display the similarity result that is not the movie we are looking at
        similarMovieId = result.movie1
        if similarMovieId == movieID_recommendations:
            similarMovieId = result.movie2

        print(getMovieName(moviesDF, similarMovieId), "score",
              str(result.score), "strenght:", str(result.numPairs))

"""How we can Improve it ?. 
-- Discard bad ratings, we dont wanna recommend movies with ratings < 4
-- recommend by genre of the movie provided"""