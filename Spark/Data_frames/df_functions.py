from pyspark.sql.session import SparkSession
from pyspark.sql.context import SQLContext

# create spark session
spark = SparkSession.builder.appName("SparkSql").getOrCreate()
sqlcontext = SQLContext(spark)

# reading from a csv ans turning into a datafram from spark
df = sqlcontext.read.csv(
    "G://Mi unidad//Big data//Spark//Data_frames//fakefriends.csv", header=True)

print("here is our schema:")
print(df.printSchema())

print("Lets display the name column:")
print(df.select("name").show())

print("filter out anyone over 21:")
print(df.select("name").filter(df["age"] < 21).orderBy("name").show())

print("Mkae everyone 10 years older:")
print(df.select(df["name"], df["age"] + 10).show())

spark.stop()
