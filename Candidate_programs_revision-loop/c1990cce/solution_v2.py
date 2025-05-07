def solve(grid):
    row = grid[0]
    n = len(row)
    mid = row.index(2)
    out = [[0]*n for _ in range(n)]
    for i in range(mid+1):
        if i == 0:
            out[i][mid] = 2
        else:
            out[i][mid-i] = 2
            out[i][mid+i] = 2
    for r in range(mid, n):
        for c in range(n):
            if out[r][c] == 0:
                dr = r - mid
                dc = c - mid
                if abs(dr) == abs(dc) and dr >= 1:
                    out[r][c] = 1
    return out