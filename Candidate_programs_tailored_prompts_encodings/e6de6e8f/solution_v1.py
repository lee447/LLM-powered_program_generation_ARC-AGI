def solve(grid):
    cols = sorted({j for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 2})
    anchor = 3
    clusters = [c for c in cols if c != anchor]
    out = [[0]*7 for _ in range(len(clusters)+1)]
    out[0][3] = 3
    curr = 3
    for i, c in enumerate(clusters):
        if c > anchor:
            curr += 1
        if grid[0][c] == 2 and grid[1][c] == 2:
            out[i+1][curr] = out[i+1][curr+1] = 2
        else:
            out[i+1][curr] = 2
    return out