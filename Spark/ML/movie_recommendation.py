from msilib import schema
from pyspark.sql.session import SparkSession
from pyspark.sql.context import SQLContext
from pyspark.sql.types import StringType, IntegerType, FloatType, LongType, StructField, StructType
from pyspark.ml.recommendation import ALS, ALSModel
from pyspark.mllib.evaluation import RegressionMetrics, RankingMetrics
from pyspark.ml.evaluation import RegressionEvaluator
import sys

spark = SparkSession.builder.appName("ML movie recommendation").getOrCreate()
sqlcontext = SQLContext(spark)

ratingsDFsch = StructType([StructField("userId", IntegerType(), True),
                           StructField("movieId", IntegerType(), True),
                           StructField("rating", FloatType(), True),
                           StructField("timestamp", LongType(), True)])

moviesDFsch = StructType([StructField("Id", IntegerType(), True),
                          StructField("title", StringType(), True),
                          StructField("genres", StringType(), True)])

ratingDF = sqlcontext.read.csv(
    "G://Mi unidad//Big data//Spark//ML//ratings.csv", header=True, schema=ratingsDFsch).drop("timestamp")

moviesDF = sqlcontext.read.csv(
    "G://Mi unidad//Big data//Spark//ML//movies.csv", header=True, schema=moviesDFsch)

# Split in Train (70%) and Test (30%).

training, test = ratingDF.randomSplit([0.7, 0.3], seed=42)

# train the model and evaluate it with the Mean Absolute Error (MAE)

als = ALS(
    rank=30,
    maxIter=4,
    userCol="userId",
    itemCol="movieId",
    coldStartStrategy='drop',
    implicitPrefs=False
)

model = als.fit(training)

predictions = model.transform(training)
evaluator = RegressionEvaluator(
    metricName="mae", labelCol="rating", predictionCol="prediction")

mae = evaluator.evaluate(predictions)

print("MAPE (test) {}".format(mae))
