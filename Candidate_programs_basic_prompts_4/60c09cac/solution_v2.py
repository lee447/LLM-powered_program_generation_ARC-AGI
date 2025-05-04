def solve(grid):
    h=len(grid); w=len(grid[0])
    return [[grid[i//2][j//2] for j in range(w*2)] for i in range(h*2)]