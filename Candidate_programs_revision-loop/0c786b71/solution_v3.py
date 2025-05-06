def solve(grid):
    r=len(grid)
    c=len(grid[0])
    rot=[[grid[r-1-i][c-1-j] for j in range(c)] for i in range(r)]
    top=[row+row[::-1] for row in rot]
    return top+top[::-1]