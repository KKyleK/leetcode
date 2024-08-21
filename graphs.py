#200: Number of islands.
#Return the number of islands in a 2x2 grid.

#Idea: Traverse the 2d grid. When we hit a land, traverse in all four directions, marking any additional land we see as water.

def numIslands(grid):
    rows = len(grid)
    columns = len(grid[0])
    totalLand=0
    landToVisit=[]
    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == '1':
                totalLand+=1
                landToVisit.append((r,c)) #A tuple of the land to visit.
            #Traverse any lands that we've discovered, so that an island is only counted once.
            while len(landToVisit) != 0:
                row,col = landToVisit.pop()
                grid[row][col] = '0'
                if row+1 < rows:
                    if grid[row+1][col] == '1':
                      landToVisit.append((row+1,col))
                if row-1 >= 0:
                    if grid[row-1][col] == '1':
                      landToVisit.append((row-1,col))
                if col+1 < columns:
                    if grid[row][col+1] == '1':
                      landToVisit.append((row,col+1))
                if col-1 >= 0:
                    if grid[row][col-1] == '1':
                      landToVisit.append((row,col-1))
    return totalLand


# grid = [["1","1","1"],
#         ["0","1","0"],
#         ["1","1","1"]]

# print(numIslands(grid))

#695: Max area of island
#Very similar to numIsland, except this time we want the max size of the island.
#One difference is that the grid contains 1's and 0's as integers instead of as strings.
def maxAreaOfIsland(grid):
    rows = len(grid)
    columns = len(grid[0])
    largestLand=0
    currentLand=0
    landToVisit=[]
    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == 1:
                landToVisit.append((r,c))
            while len(landToVisit) != 0:
                row,col = landToVisit.pop()
                #A land can get double checked. Only add it if already hasn't been counted.
                if grid[row][col] ==1:
                    currentLand+=1
                    grid[row][col] = 0
                if row+1 < rows:
                    if grid[row+1][col] == 1:
                      landToVisit.append((row+1,col))
                if row-1 >= 0:
                    if grid[row-1][col] == 1:
                      landToVisit.append((row-1,col))
                if col+1 < columns:
                    if grid[row][col+1] == 1:
                      landToVisit.append((row,col+1))
                if col-1 >= 0:
                    if grid[row][col-1] == 1:
                      landToVisit.append((row,col-1))
            if currentLand > largestLand:
               largestLand = currentLand
            currentLand = 0
    return largestLand

# grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

# print(maxAreaOfIsland(grid))

# grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]

# print(maxAreaOfIsland(grid))

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

#133: Clone graph
#Given a reference of a node in a connected, undirected graph, return a deep copy clone of the graph.
#Connected: Each node is connected to at least one other node.
# Idea: Start with first node, copy it, then if it has any neighbors, add them. Then add each neighbor to be traversed to.
def cloneGraph(node):
    toVisit=[]
    newToVisit=[]
    #It's possible for us to get stuck in a loop of visiting the same node over and over again.
    #Since the problem states that all node values are unique, we can use that to prevent revisiting nodes.
    visited=[]
    if node is None:
        return None
    toVisit.append(node)
    newGraph = Node(node.val)
    newToVisit.append(newGraph)

    while len(toVisit) > 0:
        newGraphCurrent = newToVisit.pop()
        currentNode = toVisit.pop()
        if currentNode.val in visited:
            continue
        visited.append(currentNode.val)

        #Populate the new graph node's neighbors.
        for neighbor in currentNode.neighbors:
            toVisit.append(neighbor)
            newNode = Node(neighbor.val)
            newToVisit.append(newNode)
            newGraphCurrent.neighbors.append(newNode)

    return createAdjacencyList(newGraph)

#print all nodes of a connected graph.
def printGraph(node):
    toVisit=[]
    visited=[]
    toVisit.append(node)
    while len(toVisit) != 0:
        currentNode = toVisit.pop()
        if currentNode.val in visited:
            continue
        visited.append(currentNode.val)
        print(currentNode.val)
        for neighbor in currentNode.neighbors:
            toVisit.append(neighbor)
    return

#An adjacency list is a list of lists, where each list is the node's value, followed by their neighbors values.
def createAdjacencyList(node):
    returnList = []
    toVisit=[]
    visited=[]
    toVisit.append(node)
    while len(toVisit) != 0:
        currentNode = toVisit.pop()
        nodeList =[]
        nodeList.append(currentNode.val)
        if currentNode.val in visited:
            continue
        visited.append(currentNode.val)
        print(currentNode.val)
        for neighbor in currentNode.neighbors:
            nodeList.append(neighbor.val)
            toVisit.append(neighbor)
        returnList.append(nodeList)
    return returnList


vertex1 = Node(1)
vertex2 = Node(2)
vertex3 = Node(3)
vertex4 = Node(4)

vertex1.neighbors=[vertex2, vertex3]
vertex2.neighbors=[vertex1,vertex4]
vertex3.neighbors=[vertex1,vertex4]
vertex4.neighbors=[vertex2,vertex3]
"""
1 ------- 3
|         |
|         |
2 ------- 4

"""

newGraph = cloneGraph(vertex1)
printGraph(vertex1)
print()
printGraph(newGraph)
print("mutating the original graph:")
vertex1.val = 10
vertex2.val=20
vertex3.val=30
vertex4.val=40
#This is working as expected. Only the first graph is mutated, the second remains untouched.
printGraph(vertex1)
print()
printGraph(newGraph)


print()
print()
print(createAdjacencyList(vertex1))
print(createAdjacencyList(newGraph))