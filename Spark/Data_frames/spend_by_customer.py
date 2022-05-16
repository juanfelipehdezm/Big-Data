from pyspark.sql.session import SparkSession
from pyspark.sql.context import SQLContext
from pyspark.sql.types import IntegerType, FloatType
from pyspark.sql.functions import round, col


# create spark session
spark = SparkSession.builder.appName("Customer_Spend").getOrCreate()
sqlcontext = SQLContext(spark)

# reading from a csv ans turning into a datafram from spark
df = sqlcontext.read.csv(
    "G://Mi unidad//Big data//Spark//Data_frames//customer-orders.csv", header=True)

# casting to data types and selecting only necesary documentation
id_spend = df.select((df["Client_ID"].cast(IntegerType())).alias("cust_ID"),
                     (df["Spent"].cast(FloatType())).alias("spent_amount")
                     )

# print(id_spend.show(10))
# finding the total amount by customer
result = id_spend.groupBy("cust_ID").sum("spent_amount").orderBy(
    "sum(spent_amount)", ascending=False)

result.select(col("cust_ID").alias("Customer ID"),
              round(col("sum(spent_amount)"), 2).alias("total amount spent")).show()


spark.stop()
