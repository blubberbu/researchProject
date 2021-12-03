# Adjascency List representation in Python
import math
from collections import defaultdict


def uninformedGraph():
    graph2 = defaultdict(list)
    print("Enter number of vertices and edges (eg. v e)")
    v,e = map(int,input().split())
    for i in range(e):
        print("Enter the 2 vertices to be connected (eg. v1 v2)")
        u,v = map(str,input().split())
        graph2[u].append(v)
        graph2[v].append(u)
    for v in graph2:
        print(v,graph2[v])

    return graph2


# Print the graph
def print_graph(self):
    for i in range(self.V):
        print("Vertex " + str(i) + ":", end="")
        temp = self.graph[i]
        while temp:
            print(" -> {}".format(temp.vertex), end="")
            temp = temp.next
        print(" \n")

def bfs(graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

def bfs_driver():
    # Driver code for BFS algorithm

    # Create a graph given in
    # the above diagram
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print ("Following is Breadth First Traversal"
                    " (starting from vertex 2)")
    g.BFS(2)

# This code is contributed by Neelam Yadav
num = 100


# modified from https://www.annytab.com/a-star-search-algorithm-in-python/

import time


# This class represent a graph
class Graph:
    # Initialize the class
    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()
    # Create an undirected graph by adding symmetric edges
    def make_undirected(self):
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.graph_dict.setdefault(b, {})[a] = dist
    # Add a link from A and B of given distance, and also add the inverse link if the graph is undirected
    def connect(self, A, B, distance=1):
        self.graph_dict.setdefault(A, {})[B] = distance
        if not self.directed:
            self.graph_dict.setdefault(B, {})[A] = distance
    # Get neighbors or a neighbor
    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)
    # Return a list of nodes in the graph
    def nodes(self):
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)
# This class represent a node
class Node:
    # Initialize the class
    def __init__(self, name:str, parent:str):
        self.name = name
        self.parent = parent
        self.g = 0 # Distance to start node
        self.h = 0 # Distance to goal node
        self.f = 0 # Total cost
    # Compare nodes
    def __eq__(self, other):
        return self.name == other.name
    # Sort nodes
    def __lt__(self, other):
            return self.f < other.f
    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.name, self.f))

# A* search
def astar_search(graph, heuristics, start, end):
    
    # Create lists for open nodes and closed nodes
    open = []
    closed = []
    # Create a start node and an goal node
    start_node = Node(start, None)
    goal_node = Node(end, None)
    # Add the start node
    open.append(start_node)
    
    
    # Loop until the open list is empty
    while len(open) > 0:
        # Sort the open list to get the node with the lowest cost first
        open.sort()
        # Get the node with the lowest cost
        current_node = open.pop(0)
        # Add the current node to the closed list
        closed.append(current_node)
        
        # Check if we have reached the goal, return the path
        if current_node == goal_node:
            path = []
            global distance
            distance = current_node.g
            while current_node != start_node:
                path.append(current_node.name + ': ' + str(current_node.g) + 'm')
                current_node = current_node.parent
            path.append(start_node.name + ': ' + str(start_node.g) + 'm')
            # Return reversed path
            return path[::-1]
        # Get neighbours
        neighbors = graph.get(current_node.name)
        # Loop neighbors
        for key, value in neighbors.items():
            # Create a neighbor node
            neighbor = Node(key, current_node)
            # Check if the neighbor is in the closed list
            if(neighbor in closed):
                continue
            # Calculate full path cost
            neighbor.g = current_node.g + graph.get(current_node.name, neighbor.name)
            neighbor.h = heuristics.get(neighbor.name)
            neighbor.f = neighbor.g + neighbor.h
            # Check if neighbor is in open list and if it has a lower f value
            if(add_to_open(open, neighbor) == True):
                # Everything is green, add neighbor to open list
                open.append(neighbor)
    # Return None, no path is found
    return None
# Check if a neighbor should be added to open list
def add_to_open(open, neighbor):
    for node in open:
        if (neighbor == node and neighbor.f > node.f):
            return False
    return True

# The main entry point for this module

# Create a graph
graph = Graph()
# Create graph connections (Actual distance)
# graph.connect('A', 'B', 900)
# graph.connect('A', 'D', 1020)
# graph.connect('A', 'F', 1340)
# graph.connect('B', 'C', 430)
# graph.connect('C', 'E', 450)
# graph.connect('D', 'H', 330)
# graph.connect('D', 'E', 1030)
# graph.connect('E', 'I', 290)
# graph.connect('F', 'H', 710)
# graph.connect('H', 'I', 1140)
# graph.connect('H', 'K', 410)
# graph.connect('I', 'J', 490)
# graph.connect('J', 'L', 660)
# graph.connect('K', 'J', 1080)
# graph.connect('K', 'N', 870)
# graph.connect('L', 'M', 400)
# graph.connect('L', 'N', 780)
# graph.connect('M', 'N', 640)
# graph.connect('N', 'G', 550)

# Make graph undirected, create symmetric connections
graph.make_undirected()
# Create heuristics (straight-line distance, air-travel distance)
heuristics = {}




hujan = 2
gerimis = 1
cerah = 0

gang = 2
jalan_raya = 1
tol = 0

modifier = 100

def testrunA_star():
    start_time = time.time()
    # Run the search algorithm
    path = astar_search(graph, heuristics, 'A', 'G')
    print(path)
    print()
    # Tell python to run main method
    # if __name__ == "__main__": main()

    end_time = time.time()

    timeTaken = (end_time - start_time) * 1000.0
    timeTaken = round(timeTaken, 3)


    # print('Distance: ' + str(distance) +'m')

    print('Time: ' + str(timeTaken) + 'ms')

def getNodes(type):
    # type = 1 is informed while 2 is uninformed
    if type == 1:
        print("Enter node1, node2, and weight (eg. node1 node2 weight)")
        node1, node2, weight = input().split()
        weight = int(weight)
        graph.connect(node1, node2, weight)
    if type == 2:
        # print("Enter node1 and node2 (eg. node1 node2)")
        # node1, node2 = input().split()
        # graph2.addEdge(node1, node2)
        uninformedGraph()

def getHeuristics():
    print("Type in desired node and heuristic value (eg. node 5)")
    node1, h = input().split()
    h = int(h)
    heuristics[node1] = h * 100

def informed():
    c = 0
    while c != '3':
        print(graph.nodes())
        
        print("1. Create nodes")
        # print("2. Add heuristic")
        print("2. Pick algorithm")
        print("3. Exit")

        c = input()

        if c == '1':
            getNodes(1)
        # if c == '2':
        #     getHeuristics()
        if c == '2':
            AlgoMenu()
        if c == '4':
            main()
            break


def uninformed():
    # graph2.print_graph()
    c = 0
    while c != '3':
        print("1. Create nodes")
        print("2. Run BFS algorithm")
        print("3. Exit")
        c = input()

        if c == '1':
            graph2 = uninformedGraph()
        
        if c == '2':
            bfs_(graph2)

        if c == '3':
            main()
            break

def astar_():
    c = 0
    for i in graph.nodes():
            heuristics[str(i)] = 1
    while c != '2':
        print("astar")
        print("1. Add heuristics")
        print("2. Find path")
        print("3. Exit")

        c = input()

        if c == '1':
            getHeuristics()
        
        if c == '3':
            main()
            break

    print("Enter start and end nodes")
    startNode, endNode = input().split()
    for i in range(20):
        start_time = time.perf_counter()
        path = astar_search(graph, heuristics, str(startNode), str(endNode))
        print(path)
        
        end_time = time.perf_counter()
        execTime = (end_time - start_time) * 1000.0
        # execTime = round(execTime, 4)
        print("Astar time     = %.4f ms\n" % execTime)
        print("Astar distance = " + str(distance) + " m\n")
        
        results = open(r"results.txt", "a")

        results.write("Astar time     = %.4f ms\n" % execTime)
        results.write("Astar distance = " + str(distance) + " m\n")
        results.close()


def dijkstra_():
    print("dijkstra")

    for i in graph.nodes():
        heuristics[i] = 0

    print("Enter start and end nodes")
    startNode, endNode = input().split()
    for i in range(20):
        start_time = time.perf_counter()
        path = astar_search(graph, heuristics, str(startNode), str(endNode))
        print(path)
        
        end_time = time.perf_counter()
        execTime = (end_time - start_time) * 1000.0
        # execTime = round(execTime, 4)
        
        print("Dijkstra time     = %.4f ms\n" % execTime)
        print("Dijkstra distance = " + str(distance) + " m\n")
        
        results = open(r"results.txt", "a")
    
        results.write("Dijkstra time     = %.4f ms\n" % execTime)
        results.write("Dijkstra distance = " + str(distance) + " m\n")
        results.close()

def round_up(n, decimals=4):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier


def bfs_(graph2):
    print("bfs")
    print("Enter start and end node (eg. node1 node2)")
    start, end = input().split()
    
    for i in range(20):
        start_time = time.perf_counter()
        length = bfs(graph2, start, end).__len__()
        print(bfs(graph2, start, end))
        end_time = time.perf_counter()
        execTime = (end_time - start_time) * 1000
        
        # execTime = round_up(execTime, 4)
        print("BFS time       = %.4f ms\n" % execTime)
        # print("BFS time       = " + str(execTime) + " ms\n")
        print("BFS length     = " + str(length) + " nodes\n")

        results = open(r"results.txt", "a")
    
        results.write("BFS time       = %.4f ms\n" % execTime)
        results.write("BFS length     = " + str(length) + " nodes\n")
        results.close()


def AlgoMenu():
    print("1. Astar")
    print("2. Dijkstra")
    print("3. BFS")
    print("4. Exit")

    c = input()

    if c == "1":
        astar_()

    if c == "2":
        dijkstra_()

    if c == "3":
        bfs_()

    if c == '4':
        main()    

def createGraph():
    print("1. Informed")
    print("2. Uninformed")
    c = input()

    if c == '1':
        informed()
    if c == '2':
        uninformed()

def analyzeResults():
    result = open(r"results.txt", "a+")

def main():
    c = 0
    while c != "3":
        c = 0
        print("1. Create graph")
        print("2. Analyze results") 
        print("3. Exit") 

        c = input()

        if c == "1":
            createGraph()
        
        if c == '2':
            import analyzeresult


if __name__ == '__main__':
    main()
    