def solve(grid):
    H = len(grid)
    W = len(grid[0])
    centers = []
    for r in range(1, H-1):
        for c in range(1, W-1):
            if grid[r][c] == 3 and grid[r-1][c] == 3 and grid[r+1][c] == 3 and grid[r][c-1] == 3 and grid[r][c+1] == 3:
                centers.append((r, c))
    result = [row[:] for row in grid]
    for i in range(len(centers)):
        r1, c1 = centers[i]
        for j in range(i+1, len(centers)):
            r2, c2 = centers[j]
            dr = r2 - r1
            dc = c2 - c1
            if dr != 0 and abs(dr) == abs(dc):
                sr = 1 if dr > 0 else -1
                sc = 1 if dc > 0 else -1
                for k in range(1, abs(dr)):
                    rr = r1 + k*sr
                    cc = c1 + k*sc
                    if result[rr][cc] == 0:
                        result[rr][cc] = 2
    return result