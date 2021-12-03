results = open(r"results.txt", 'r')

lines = []
bfs_time = []
bfs_distance = []
dijkstra_time = []
dijkstra_distance = []
astar_time = []
astar_distance = []

def getData(algo, type, value):
    if algo == 'Astar':
        print()
        if type == 'time':
            astar_time.append(value) 
        if type == 'distance':
            astar_distance.append(value)
    if algo == 'Dijkstra':
        print()
        if type == 'time':
            dijkstra_time.append(value) 
        if type == 'distance':
            dijkstra_distance.append(value)
    if algo == 'BFS':
        print()
        if type == 'time':
            bfs_time.append(value) 
        if type == 'length':
            bfs_distance.append(value)

def sortList():
    astar_time.sort(reverse = True)
    astar_distance.sort(reverse = True)
    dijkstra_time.sort(reverse = True)
    dijkstra_distance.sort(reverse = True)
    bfs_time.sort(reverse = True)
    bfs_distance.sort(reverse = True)

def getMax():
    aTimeMax = astar_time[0]
    aDistMax = astar_distance[0]
    dTimeMax = dijkstra_time[0]
    dDistMax = dijkstra_distance[0]
    bTimeMax = bfs_time[0]
    bDistMax = bfs_distance[0]

    max = [aTimeMax, aDistMax, dTimeMax, dDistMax, bTimeMax, bDistMax]
    
    return max

def avg(lst):
    return sum(map(float, lst)) / len(lst)

def getMean():
    aTimeAvg = round(avg(astar_time), 4)
    aDistAvg = round(avg(astar_distance), 4)
    dTimeAvg = round(avg(dijkstra_time), 4)
    dDistAvg = round(avg(dijkstra_distance), 4)
    bTimeAvg = round(avg(bfs_time), 4)
    bDistAvg = round(avg(bfs_distance))

    mean = [aTimeAvg, aDistAvg, dTimeAvg, dDistAvg, bTimeAvg, bDistAvg]
    return mean
    

lines = results.readlines()
for i in lines:
    # print(i)
    i = i.split()
    getData(i[0], i[1], i[3])
sortList()
for i in astar_time:
    print(i)

data = open(r"processedData.txt", "w")

data.write("Sample size: " + str(round(len(lines)/3/2)) + "\n")
data.write("Max data\n\n")
max = getMax()
for i in range(len(max)+1):
    if i == 1:
        print("Astar max time: " + str(max[i-1]) + "ms")
        data.write("Astar max time: " + str(max[i-1]) + "ms\n")
    if i == 2:
        print("Astar max distance: " + str(max[i-1]) + "m")
        data.write("Astar max distance: " + str(max[i-1]) + "m\n")
    if i == 3:
        print("Dijkstra max time: " + str(max[i-1]) + "ms")
        data.write("Dijkstra max time: " + str(max[i-1]) + "ms\n")
    if i == 4:
        print("Dijkstra max distance: " + str(max[i-1]) + "m")
        data.write("Dijkstra max distance: " + str(max[i-1]) + "m\n")
    if i == 5:
        print("BFS max time: " + str(max[i-1]) + "ms")
        data.write("BFS max time: " + str(max[i-1]) + "ms\n")
    if i == 6:
        print("BFS max distance: " + str(max[i-1]) + " nodes")    
        data.write("BFS max distance: " + str(max[i-1]) + " nodes\n")    

data.write("\n-------------------------------------------------------------\n")
data.write("Mean data\n\n")

mean = getMean()
for i in range(len(mean)+1):
    if i == 1:
        print("Astar mean time: " + str(mean[i-1]) + "ms")
        data.write("Astar mean time: " + str(mean[i-1]) + "ms\n")
    if i == 2:
        print("Astar mean distance: " + str(mean[i-1]) + "m")
        data.write("Astar mean distance: " + str(mean[i-1]) + "m\n")
    if i == 3:
        print("Dijkstra mean time: " + str(mean[i-1]) + "ms")
        data.write("Dijkstra mean time: " + str(mean[i-1]) + "ms\n")
    if i == 4:
        print("Dijkstra mean distance: " + str(mean[i-1]) + "m")
        data.write("Dijkstra mean distance: " + str(mean[i-1]) + "m\n")
    if i == 5:
        print("BFS mean time: " + str(mean[i-1]) + "ms")
        data.write("BFS mean time: " + str(mean[i-1]) + "ms\n")
    if i == 6:
        print("BFS mean distance: " + str(mean[i-1]) + " nodes")
        data.write("BFS mean distance: " + str(mean[i-1]) + " nodes\n")


results.close()
data.close()    
