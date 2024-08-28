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




# heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# print(pacificAtlantic(heights))

# heights = [[1,1],[1,1],[1,1]]

# print(pacificAtlantic(heights))

#207: Course Schedule
#Num courses represents an array of courses numCourses long.
#Prerequisites is an array of pairs, where each pair represents the course, followed by the courses prerequisite.
#Example: numCourses = 2, prerequisites = [[1,0]] means that there are two courses, and to take course 1, you need course 0.
#Each course can only have 1 prerequisite.
#
#Idea: We can build a directed graph to represent the courses and their dependencies.
#If the graph contains a cycle, then return false, otherwise return true.
#This is because a cycle means that a two or more courses depend on each other, meaning
#they can never be completed.
#
#Unfortunately my solution below is too inefficient and doesn't pass the runtime requirements for leetcode. Will have to find a better way to find if the graph has no cycles.
def canFinish(numCourses, prerequisites):
    #Create graph of courses
    vertices=[]
    for c in range(numCourses):
        vertices.append(Node(c))
    #Add connections
    for p in range(len(prerequisites)):
        vertices[prerequisites[p][0]].neighbors.append(vertices[prerequisites[p][1]])

    #Find if there are any cycles in the directed graph:
    #For each vertex, go to its neighbor, maintaining a list of nodes traveled.
    #If we ever repeat a node traveled, there is a cycle.
    #If a node has two neighbors, maintain a separate list of nodes traveled.
    toVisit=[] #Looks like: [Node,#] where # is the corresponding array in visited.
    visited=[]

    for vertex in range(len(vertices)):
        toVisit.append((vertices[vertex],0))
        visited.append([]) #We will have at least 1 path.

        while len(toVisit) != 0:
            currentNode, visitedIndex = toVisit.pop()
            if currentNode.val in visited[visitedIndex]:
                return False
            visited[visitedIndex].append(currentNode.val)

            #Add neighbors. If a neighbor can't be added, delete the whole
            #chain. Since we are using a stack to determine which path to check next, just pop visited.
            if len(currentNode.neighbors) == 0:
                visited.pop()
            else:
                for n in range(len(currentNode.neighbors)):
                    toVisit.append((currentNode.neighbors[n], n+visitedIndex))
                    #Create a new path, copy what we have seen already in visited.
                    if n > 0:
                        copyPath=[]
                        for i in range(len(visited[visitedIndex])):
                            copyPath.append(visited[visitedIndex][i])
                        visited.append(copyPath)
        toVisit=[]
        visited=[]
    return True


#Topological sorting approach:
# An ordering of nodes such that for every directed edge u-> v, node u comes before node v.
# In other words, each node in the ordering must appear before the nodes that it points to.
#
# If this is possible, than you can take all of the courses, if not, there is a cycle, and you can't take the courses.
#Khan's algorithm:
#   Maintain a queue.
#   Add all nodes with an indegree (number of edges coming in) of 0 to the queue.
#   Visit first node in Queue.
#       Delete all outbound edges from this node.
#       Repeat.
#   If there are any nodes that weren't visited, they are a cycle.
def canFinish(numCourses, prerequisites):
    visited=[False]*numCourses
    toVisit=[] #A queue of the numbers to visit.
    nodesAffected=[]

    findInDegreeZeros(numCourses, prerequisites, toVisit, nodesAffected)
    while len(toVisit)!=0:
        #Visit the nodes and remove their outbound edges.
        while len(toVisit)!=0:
            currentNode = toVisit.pop(0) #Pop the first element like a queue.
            visited[currentNode] = True
            counter = 0
            while counter < len(prerequisites):
                if(prerequisites[counter][1]) == currentNode:
                    nodesAffected.append(prerequisites[counter][0])
                    prerequisites.pop(counter)
                    counter-=1
                counter+=1
        #After we have visited all nodes with 0 in degree, find more to visit.
        findInDegreeZeros(numCourses, prerequisites, toVisit, nodesAffected)
        nodesAffected=[]
        #Don't look at nodes we have already visited.
        counter = 0
        while counter < len(toVisit):
            if visited[(toVisit[counter])]:
                toVisit.pop(counter)
                counter-=1
            counter+=1
    if False in visited:
        return False
    else:
        return True

#If we know which nodes are effected, only check them instead of all nodes.
def findInDegreeZeros(numCourses, prerequisites, toVisit, nodesAffected):
    if len(nodesAffected) != 0:
        for i in nodesAffected:
            inDegreeZero = True
            for j in range(len(prerequisites)):
                if prerequisites[j][0] == i:
                    inDegreeZero = False
                    break
            if (inDegreeZero):
                toVisit.append(i)

    else:
        for i in range(numCourses):
            inDegreeZero = True
            for j in range(len(prerequisites)):
                if prerequisites[j][0] == i:
                    inDegreeZero = False
                    break
            if (inDegreeZero):
                toVisit.append(i)
    return

# ##TRUE
# numCourses = 2
# prerequisites = [[1,0]]
# print(canFinish(numCourses, prerequisites))

# #FALSE
# numCourses = 2
# prerequisites = [[1,0],[0,1]]
# print(canFinish(numCourses, prerequisites))

# #FALSE
# prerequisites = [[2,0],[1,0],[3,1],[3,2],[1,3]]
# numCourses = 4
# print(canFinish(numCourses, prerequisites))

# #TRUE
# numCourses = 5
# prerequisites = [[1,4],[2,4],[3,1],[3,2]]
# print(canFinish(numCourses, prerequisites))

# #TRUE
# prerequisites =[[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]
# numCourses=8
# print(canFinish(numCourses, prerequisites))

# #TRUE
# prerequisites = [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]
# numCourses=7
# print(canFinish(numCourses, prerequisites))

# #TRUE
# numCourses=100
# prerequisites = [[1,0],[2,0],[2,1],[3,1],[3,2],[4,2],[4,3],[5,3],[5,4],[6,4],[6,5],[7,5],[7,6],[8,6],[8,7],[9,7],[9,8],[10,8],[10,9],[11,9],[11,10],[12,10],[12,11],[13,11],[13,12],[14,12],[14,13],[15,13],[15,14],[16,14],[16,15],[17,15],[17,16],[18,16],[18,17],[19,17],[19,18],[20,18],[20,19],[21,19],[21,20],[22,20],[22,21],[23,21],[23,22],[24,22],[24,23],[25,23],[25,24],[26,24],[26,25],[27,25],[27,26],[28,26],[28,27],[29,27],[29,28],[30,28],[30,29],[31,29],[31,30],[32,30],[32,31],[33,31],[33,32],[34,32],[34,33],[35,33],[35,34],[36,34],[36,35],[37,35],[37,36],[38,36],[38,37],[39,37],[39,38],[40,38],[40,39],[41,39],[41,40],[42,40],[42,41],[43,41],[43,42],[44,42],[44,43],[45,43],[45,44],[46,44],[46,45],[47,45],[47,46],[48,46],[48,47],[49,47],[49,48],[50,48],[50,49],[51,49],[51,50],[52,50],[52,51],[53,51],[53,52],[54,52],[54,53],[55,53],[55,54],[56,54],[56,55],[57,55],[57,56],[58,56],[58,57],[59,57],[59,58],[60,58],[60,59],[61,59],[61,60],[62,60],[62,61],[63,61],[63,62],[64,62],[64,63],[65,63],[65,64],[66,64],[66,65],[67,65],[67,66],[68,66],[68,67],[69,67],[69,68],[70,68],[70,69],[71,69],[71,70],[72,70],[72,71],[73,71],[73,72],[74,72],[74,73],[75,73],[75,74],[76,74],[76,75],[77,75],[77,76],[78,76],[78,77],[79,77],[79,78],[80,78],[80,79],[81,79],[81,80],[82,80],[82,81],[83,81],[83,82],[84,82],[84,83],[85,83],[85,84],[86,84],[86,85],[87,85],[87,86],[88,86],[88,87],[89,87],[89,88],[90,88],[90,89],[91,89],[91,90],[92,90],[92,91],[93,91],[93,92],[94,92],[94,93],[95,93],[95,94],[96,94],[96,95],[97,95],[97,96],[98,96],[98,97],[99,97]]

# print(canFinish(numCourses, prerequisites))

#684: Redundant connection
#Find the redundant edge in a graph.
#Idea: Since an extra edge was added there exists a cycle in the graph. Find the cycle, then return the last edge in the
#Input that is contained in the cycle.
def findRedundantConnection(edges):
    #Use Khan's algorithm to find the cycle. Since it's an undirected graph, we visit, and remove the edges of
    #nodes with in degree 1 instead of 0.
    visit = [False] * len(edges) #There are nodes+1 number of edges since one edge was added.
    toVisit=[]
    nodesAffected=[]
    findInDegreeOneUndirected(len(edges), edges, toVisit, nodesAffected)

    while len(toVisit) != 0:
        while len(toVisit) != 0:
            #Remove edges for all nodes of in degree = 0:
            currentNode = toVisit.pop(0)
            visit[currentNode-1] = True
            counter = 0
            while counter < len(edges):
                if(edges[counter][1]) == currentNode:
                    nodesAffected.append(edges[counter][0])
                    edges.pop(counter)
                    counter-=1
                if(edges[counter][0]) == currentNode:
                    nodesAffected.append(edges[counter][1])
                    edges.pop(counter)
                    counter-=1
                counter+=1
        #After we have visited all nodes with 0 in degree, find more to visit.
        findInDegreeOneUndirected(len(edges), edges, toVisit, nodesAffected)
        nodesAffected=[]
    #Return the cycle:
    #The cycle will be the LAST edge that includes any of the nodes in the cycle. AKA, if 1,2,3,4 are nodes in the cycle, than if [1,4] is the last edge in edges, that's the answer.
    cycleNodes=[]
    for i in range(len(visit)):
        if not visit[i]:
            cycleNodes.append(i+1)
    counter = len(edges)-1
    while counter >=0:
        if edges[counter][0] in cycleNodes and edges[counter][1] in cycleNodes:
            return edges[counter]
        counter -=1

#Finds nodes with an in degree of 1 in a non directed graph.
def findInDegreeOneUndirected(numNodes, edges, toVisit, nodesAffected):

    if len(nodesAffected) != 0:
        for i in nodesAffected:
            inDegree = 0
            for j in range(len(edges)):
                if edges[j][0] == i or edges[j][1] == i:
                    inDegree +=1
                    if (inDegree==2):
                        break
            if (inDegree < 2):
                toVisit.append(i)

    else:
        for i in range(1, numNodes+1):
            inDegree = 0
            for j in range(len(edges)):
                if edges[j][0] == i or edges[j][1] == i:
                    inDegree +=1
                    if (inDegree==2):
                        break
            if (inDegree < 2):
                toVisit.append(i)
    return


edges = [[1,2],[1,3],[2,3]]
print(findRedundantConnection(edges))

edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
print(findRedundantConnection(edges))