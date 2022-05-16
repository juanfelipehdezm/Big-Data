from pyspark import SparkConf, SparkContext

# setting up sparkContext (sc)
conf = SparkConf().setMaster("local").setAppName("FriendsByAge")
sc = SparkContext(conf=conf)

# reading the csv file and returning a RDD object
lines = sc.textFile("G://Mi unidad//Big data//Spark//RDD//fakefriends.csv")
# print(lines.collect())


def parseline(line):
    """ Return the 2 and 3 position from a line as a tuple 
        in this case the age and the number of friends"""
    fields = line.split(",")
    age = int(fields[2])
    numFriends = int(fields[3])
    return (age, numFriends)


RDD = lines.map(parseline)
# print(RDD.collect())
# next, lets map values adding (,1) to the tuple and then group or "reduce" the keys (ages)
totalByAge = RDD.mapValues(lambda x: (x, 1)).reduceByKey(
    lambda x, y: (x[0] + y[0], x[1] + y[1]))
# print(totalByAge.collect())
# finally, calculate the average
averagesByAge = totalByAge.mapValues(lambda x: x[0] / x[1])
for result in averagesByAge.collect():
    print(result)
