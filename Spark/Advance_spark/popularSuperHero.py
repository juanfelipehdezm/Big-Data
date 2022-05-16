from pyspark.sql.session import SparkSession
from pyspark.sql.context import SQLContext
from pyspark.sql.types import IntegerType, StringType, StructField, StructType
from pyspark.sql import functions as func

# Creating spark session
spark = SparkSession.builder.appName("Super Heroes").getOrCreate()
sqlcontext = SQLContext(spark)

# correct schema
schema = StructType([StructField("id", IntegerType(), True),
                    StructField("name", StringType(), True)])

# Importing Marvel-graph, the first column os this data set represente the ID of a super hero, the next lines are the Id
# Of others super hereoes with whome the first here has shared comic
lines = spark.read.text(
    "G://Mi unidad//Big data//Spark//Advance_spark//Marvel Graph.txt")

# Marvel Names represent the id and the name of the super hero
names = spark.read.schema(schema).option("sep", " ").csv(
    "G://Mi unidad//Big data//Spark//Advance_spark//Marvel Names.txt")

"""Creating a new DF.
Lines is just one column called "value" so we split it and the first object of each lines is the super hero ID
and the rest are the other with whome he/she have connections, so we sum them to now the cuantity of connections
Finally, id groupBy ID and sum all possible connections to know the connections/ID """
connections = lines.withColumn("id", func.split(lines["value"], " ")[0])\
                   .withColumn("connections", func.size(func.split(lines["value"], " "))-1)\
                   .groupBy("id").agg(func.sum("connections").alias("connections")).orderBy("connections", ascending=False)

# most poppular hero contains ID and number of connections
mostPopular = connections.first()

# name for that super hero
mostPopularName = names.filter(names["id"] == mostPopular[0])

print(mostPopularName.show())
print(mostPopularName.select("name").collect(), "is the mosth populat with " +
      str(mostPopular[1]), "connections")
