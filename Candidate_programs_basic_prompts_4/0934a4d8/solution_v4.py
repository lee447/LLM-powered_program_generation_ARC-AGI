def solve(grid):
    R = [i for i,row in enumerate(grid) if 8 in row]
    C = [j for j in range(len(grid[0])) if any(grid[i][j]==8 for i in range(len(grid)))]
    out = [[0]*len(C) for _ in R]
    for i, r in enumerate(R):
        for j, c in enumerate(C):
            out[i][j] = grid[r+ (1 if r+1<len(grid) and grid[r+1][c]!=8 else -1)][c+ (1 if c+1<len(grid[0]) and grid[r][c+1]!=8 else -1)]
    return out