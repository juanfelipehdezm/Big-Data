from pyspark.sql.session import SparkSession
from pyspark.sql.context import SQLContext
from pyspark.sql.types import StructField, StructType, IntegerType, StringType
from pyspark.sql import functions as func

# Spark session
spark = SparkSession.builder.appName("unpop super heroes").getOrCreate()
sqlcontext = SQLContext(spark)

# schema
schema = StructType([StructField("id_hero", IntegerType(), True),
                     StructField("name", StringType(), True)])

# importing marvel graph and names
graph = spark.read.text(
    "G://Mi unidad//Big data//Spark//Advance_spark//Marvel Graph.txt")

names = spark.read.schema(schema).option("sep", " ").csv(
    "G://Mi unidad//Big data//Spark//Advance_spark//Marvel Names.txt")

# connection df, as we want the least poppul
connections = graph.withColumn("id", func.split(graph["value"], " ")[0])\
                   .withColumn("connections", func.size(func.split(graph["value"], " "))-1)\
                   .groupBy("id").agg(func.sum("connections").alias("connections"))

# joinning to tables
unpopheroes = connections.join(
    names, connections["id"] == names["id_hero"], "inner").drop("id_hero").orderBy("connections")
# extracting the min value of connections, the .first()[0] is neccesary to be able to use minConnection on filter later on
minConnection = unpopheroes.agg(func.min("connections")).first()[0]
# filtering to obtain only the heroes with the min connection possible
unpopheroes.filter(unpopheroes["connections"] == minConnection).show()
