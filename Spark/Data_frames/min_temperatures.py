from pyspark.sql.session import SparkSession
from pyspark.sql.context import SQLContext
from pyspark.sql.types import IntegerType, FloatType
from pyspark.sql import functions as func

# create spark session
spark = SparkSession.builder.appName("Temperatures").getOrCreate()
sqlcontext = SQLContext(spark)

# reading from a csv ans turning into a datafram from spark
df = sqlcontext.read.csv(
    "G://Mi unidad//Big data//Spark//Data_frames//1800.csv", header=True)

# defining proper data types
temperatures = df.select("Station_ID", "Max_Min",
                         (df["Date"].cast(IntegerType())).alias("Date"),
                         (df["Temperature"].cast(FloatType())).alias("Temperature"))

# Filtering by TMIN and selection station:id and temperature which is whith what i am gg work with
min_temps = temperatures.filter(
    temperatures["Max_Min"] == "TMIN").select("Station_ID", "temperature")

# converting to celsious
min_temps_C = min_temps.withColumn("temperature", func.col("temperature") / 10)

min_tempsBy_station = min_temps_C.groupBy("Station_ID").min("temperature").orderBy(
    "min(temperature)", ascending=False)

print(min_tempsBy_station.show())

spark.stop()
