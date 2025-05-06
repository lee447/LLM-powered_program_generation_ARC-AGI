def solve(grid):
    rows = len(grid)
    cols = len(grid[0])
    sep = next(j for j in range(cols) if len({grid[i][j] for i in range(rows)})==1 and grid[0][j]!=0)
    left_w = sep
    right_w = cols - sep - 1
    w = min(left_w, right_w)
    res = [[0]*w for _ in range(rows)]
    for i in range(rows):
        for j in range(w):
            a = grid[i][j] != 0
            b = grid[i][sep+1+j] != 0
            if a ^ b:
                res[i][j] = 2
    return res