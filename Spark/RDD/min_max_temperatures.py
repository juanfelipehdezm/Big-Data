from pyspark import SparkConf, SparkContext

# setting up sparkContext (sc)
conf = SparkConf().setMaster("local").setAppName("minTemperatures")
sc = SparkContext(conf=conf)

# reading the csv file and returning a RDD object
lines = sc.textFile("G://Mi unidad//Big data//Spark//RDD//1800.csv")


def parseline(line):
    fields = line.split(",")
    stationID = fields[0]
    entryType = fields[2]
    temperature = float(fields[3]) / 10
    return (stationID, entryType, temperature)


RDD = lines.map(parseline)

"""MIN"""
# only needed the min tempratures
minTemps = RDD.filter(lambda x: "TMIN" in x[1])
# I can get ride off "entryType"
stationMinTemps = minTemps.map(lambda x: (
    x[0], x[2])).reduceByKey(lambda x, y: min(x, y))

for result in stationMinTemps.collect():
    print(result[0], "{:.2f}°C".format(result[1]))

print(" -------- ")
"""MAX"""

RDD = lines.map(parseline)
maxTemps = RDD.filter(lambda x: "TMAX" in x[1])
stationMaxTemps = maxTemps.map(lambda x: (
    x[0], x[2])).reduceByKey(lambda x, y: max(x, y))

for result_2 in stationMaxTemps.collect():
    print(result_2[0], "{:.2f}°C".format(result_2[1]))
