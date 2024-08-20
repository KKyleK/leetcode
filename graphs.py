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

grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]

print(maxAreaOfIsland(grid))