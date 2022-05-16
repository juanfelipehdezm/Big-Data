from pyspark.sql.session import SparkSession
from pyspark.sql.context import SQLContext

# create spark session
spark = SparkSession.builder.appName("SparkSql").getOrCreate()
sqlcontext = SQLContext(spark)

# reading from a csv ans turning into a datafram from spark
df = sqlcontext.read.csv(
    "G://Mi unidad//Big data//Spark//Data_frames//fakefriends.csv", header=True)

# print(df.show(10))
# register the Dataframe as a SQL temporary view
df.createOrReplaceTempView("people")
# Runnung an SQL query in pyspark
query = "SELECT * FROM people WHERE age >= 13 AND age <=25"

teenager = spark.sql(query)
# using functions instead of executing SQL queries
teenager.groupBy("age").count().orderBy("age").show()

spark.stop()
