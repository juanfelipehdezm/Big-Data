from pyspark import SparkConf, SparkContext

# setting up sparkContext (sc)
conf = SparkConf().setMaster("local").setAppName("FriendsByAge")
sc = SparkContext(conf=conf)

lines = sc.textFile("G://Mi unidad//Big data//Spark//RDD//customer-orders.csv")


def parseline(line: str) -> tuple:
    """ Extract necessary information from the RDD line"""
    fields = line.split(",")
    client_id = fields[0]
    spend = float(fields[2])
    return (client_id, spend)


client_spend = lines.map(parseline)
# sumando the amount spent by customer and sorted them
total_spend_by_client = client_spend.reduceByKey(lambda x, y: x + y)
sorted_clients = total_spend_by_client.map(
    lambda x: (x[1], x[0])).sortByKey(False)

for result in sorted_clients.collect():
    print("Client {} spent {:.2f} $".format(result[1], result[0]))
