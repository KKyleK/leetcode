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

# newGraph = cloneGraph(vertex1)
# printGraph(vertex1)
# print()
# printGraph(newGraph)
# print("mutating the original graph:")
# vertex1.val = 10
# vertex2.val=20
# vertex3.val=30
# vertex4.val=40
# #This is working as expected. Only the first graph is mutated, the second remains untouched.
# printGraph(vertex1)
# print()
# printGraph(newGraph)


# print()
# print()
# print(createAdjacencyList(vertex1))
# print(createAdjacencyList(newGraph))

#994: Rotting oranges
#Find the minimum number of minutes that must elapse until no cell has a fresh orange.
def orangesRotting(grid):

    rows = len(grid)
    columns = len(grid[0])
    minutes = 0
    orangesToAvoid = []
    noChange = False
    while not noChange:
        for r in range(rows):
            for c in range(columns):
                #Found a rotten orange, change adjacent oranges.
                if (grid[r][c] == 2) and ((r,c) not in orangesToAvoid):

                    if r+1 < rows:
                        r = int(r)
                        c = int(c)
                        if grid[r+1][c] == 1:
                            grid[r+1][c] = 2
                            orangesToAvoid.append((r+1,c))
                    if r-1 >= 0:
                        if grid[r-1][c] == 1:
                            grid[r-1][c] = 2
                            orangesToAvoid.append((r-1,c))
                    if c+1 < columns:
                        if grid[r][c+1] == 1:
                            grid[r][c+1] = 2
                            orangesToAvoid.append((r,c+1))
                    if c-1 >= 0:
                        if grid[r][c-1] == 1:
                            grid[r][c-1] = 2
                            orangesToAvoid.append((r,c-1))
        if len(orangesToAvoid) == 0:
            noChange = True
        else:
            minutes+=1
        orangesToAvoid = []

    #Check if all oranges are rotten.
    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == 1:
                return -1
    return minutes

# grid = [[2,1,1],[1,1,0],[0,1,1]]
# print(orangesRotting(grid))

#417: Pacific Atlantic ocean flow
#Return a list of coordinates representing areas on an island where water can flow into both the pacific ocean and Atlantic ocean.

#Idea: for each coordinate, attempt to move in all directions (up, down, left, right) if moving gets to atlantic/pacific ocean, mark it.
#If moving gets to both atlantic and pacific, done.

def pacificAtlantic(grid):
    rows = len(grid)
    columns = len(grid[0])

    traveled=[]
    toTravel=[]
    visitedPacific=False
    visitedAtlantic=False
    success=[]

    for r in range (rows):
        for c in range(columns):
            toTravel.append((r,c))
            while (len(toTravel) != 0) and ((visitedPacific != True) or (visitedAtlantic != True)):
                row, col = toTravel.pop()
                traveled.append((row, col))

                if (onPacific(row,col)):
                    visitedPacific = True
                if (onAtlantic(rows,columns,row,col)):
                    visitedAtlantic = True

                if row+1 < rows:
                    if (grid[row+1][col] <= grid[row][col]) and ((row+1,col) not in traveled):
                        toTravel.append((row+1,col))
                if row-1 >= 0:
                    if (grid[row-1][col] <= grid[row][col]) and ((row-1,col) not in traveled):
                        toTravel.append((row-1,col))
                if col+1 < columns:
                    if (grid[row][col+1] <= grid[row][col]) and ((row,col+1) not in traveled):
                        toTravel.append((row,col+1))
                if col-1 >= 0:
                    if (grid[row][col-1] <= grid[row][col]) and ((row,col-1) not in traveled):
                        toTravel.append((row,col-1))

            if visitedAtlantic == True and visitedPacific == True:
                success.append([r,c])
            traveled = []
            toTravel = []
            visitedAtlantic = False
            visitedPacific = False

    return success
#pacific is far left and top of grid.
def onPacific(row,col):
    if row == 0 or col ==0:
        return True
    return False

#atlantic is far right and bottom of grid.
def onAtlantic(rows, columns,row,col):
    if (row == rows-1) or (col == columns-1):
        return True
    return False




heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(pacificAtlantic(heights))

heights = [[1,1],[1,1],[1,1]]

print(pacificAtlantic(heights))