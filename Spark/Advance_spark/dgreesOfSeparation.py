from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("Breadth First Search")
sc = SparkContext(conf=conf)

# The characters we wish to find the degree of separation bwtween:
startCharID = 5306  # Spiderman
targetCharID = 14  # Adam 1,031

# Our accumulator, used to signal when we find the target character during the BFS traversal.
hitCounter = sc.accumulator(0)


def convertoBFS(line) -> tuple:
    """Convert th line to a tuple structuring the data in the way we need"""
    fields = line.split()
    heroID = int(fields[0])
    connections = [int(connection) for connection in fields[1:]]
    color = "WHITE"
    distance = 9999

    if heroID == startCharID:
        color = "GRAY"
        distance = 0
    return (heroID, (connections, distance, color))


def creatStartingRDD():
    file = sc.textFile(
        "G://Mi unidad//Big data//Spark//Advance_spark//Marvel Graph.txt")
    return file.map(convertoBFS)


def bfsMap(node):
    characterID = node[0]
    connections = node[1][0]
    distance = node[1][1]
    color = node[1][2]

    results = []

    # IF this node needs to be expanded
    if (color == "GRAY"):
        newColor = "GRAY"
        for connection in connections:
            newCharacterID = connection
            newDistance = distance + 1
            if targetCharID == newCharacterID:
                hitCounter.add(1)
            newEntry = (newCharacterID, ([], newDistance, newColor))
            results.append(newEntry)

        # We have processed this node, so color is turning black
        color = "BLACK"
    else:
        results.append((characterID, (connections, distance, color)))
        return results


def bfsReduce(data1, data2):
    edges1 = data1[0]
    edges2 = data2[0]
    distance1 = data1[1]
    distance2 = data2[2]
    color1 = data1[2]
    color2 = data2[2]

    distance = 9999
    color = color1
    edges = []

    # see if 1 is the original node with its coneections.
    # if so preserve them
    if len(edges1) > 0:
        edges.extend(edges1)
    if len(edges2) > 0:
        edges.extend(edges2)

    # preserve darkest color
    if color1 == 'WHITE' and color2 in ['GRAY', 'BLACK']:
        color = color2

    if (color1 == 'GRAY' and color2 == 'BLACK'):
        color = color2

    if color2 == 'WHITE' and color1 in ['GRAY', 'BLACK']:
        color = color1

    if (color2 == 'GRAY' and color1 == 'BLACK'):
        color = color1

    return (edges, distance, color)

# Main program here:


iterationRDD = creatStartingRDD()

for iteration in range(10):
    print("Running BFS iterarion #", iteration+1)

    # Create new vertices as needed to darken or reduce distances in the
    # reduce stage. If we encounter the node we're looking for as a GRAY
    # node, increment our accumulator to signal that we're done.
    mapped = iterationRDD.flatMap(bfsMap)
    mapped.collect()
    if (hitCounter.value > 0):
        print("Hit the target character! from " +
              str(hitCounter.value) + " different directions")
        break

    # Reducer combines data for each character ID, preserving the darkest
    # color and shortest path.
    iterationRDD = mapped.reduceByKey(bfsReduce)
