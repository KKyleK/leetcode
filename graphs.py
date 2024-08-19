#200: Number of islands.
#Return the number of islands in a 2x2 grid.

#Idea: Traverse the 2d grid. When we hit a land, traverse in all four directions, adding them to be traversed, and turn them into water afterwards.

def numIslands(grid):
    rows = len(grid)
    columns = len(grid[0])
    # for i in grid:
    #     for j in i:
    #         print(j)
    # print(rows)
    # print(columns)

    for row in range(rows):
        for col in range(columns):
            print(grid[row][col])



grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
numIslands(grid)