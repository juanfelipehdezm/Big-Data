from pyspark.sql.session import SparkSession
from pyspark.sql.context import SQLContext
from pyspark.sql.types import IntegerType

# create spark session
spark = SparkSession.builder.appName("SparkSql").getOrCreate()
sqlcontext = SQLContext(spark)

# reading from a csv ans turning into a datafram from spark
df = sqlcontext.read.csv(
    "G://Mi unidad//Big data//Spark//Data_frames//fakefriends.csv", header=True)

age_friends = df.select(
    (df["age"].cast(IntegerType())).alias("age"),
    (df["friends"].cast(IntegerType())).alias("friends")
)
# casting to integer the respective columns


print(age_friends.printSchema())
age_friends.groupBy("age").avg("friends").orderBy(
    "avg(friends)", ascending=False).show()

spark.stop()
