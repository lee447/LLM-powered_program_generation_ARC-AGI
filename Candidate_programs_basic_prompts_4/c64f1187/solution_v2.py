def solve(grid):
    R, C = len(grid), len(grid[0])
    shape = {}
    for i in range(R):
        for j in range(C):
            c = grid[i][j]
            if c not in (0,1,5) and c not in shape:
                pts = [(i+di, j+dj) for di in range(-3,4) for dj in range(-3,4)
                       if 0 <= i+di < R and 0 <= j+dj < C and grid[i+di][j+dj] == 1]
                if pts:
                    minr = min(x for x,y in pts)
                    minc = min(y for x,y in pts)
                    shape[c] = [(x-minr, y-minc) for x,y in pts]
    minr, minc, maxr, maxc = R, C, 0, 0
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 5:
                minr = min(minr, i); minc = min(minc, j)
                maxr = max(maxr, i); maxc = max(maxc, j)
    H = maxr - minr + 1
    W = maxc - minc + 1
    out = [[0]*W for _ in range(H)]
    for i in range(minr, maxr+1):
        for j in range(minc, maxc+1):
            c = grid[i][j]
            if c not in (0,1,5) and c in shape:
                for dr, dc in shape[c]:
                    rr = i - minr + dr
                    cc = j - minc + dc
                    if 0 <= rr < H and 0 <= cc < W:
                        out[rr][cc] = c
    return out