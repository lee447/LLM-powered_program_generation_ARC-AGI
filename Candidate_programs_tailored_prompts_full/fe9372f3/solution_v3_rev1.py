def solve(grid):
    H, W = len(grid), len(grid[0])
    reds = [(r, c) for r in range(H) for c in range(W) if grid[r][c] == 2]
    row_counts = [0]*H
    col_counts = [0]*W
    for r, c in reds:
        row_counts[r] += 1
        col_counts[c] += 1
    maxr = max(row_counts)
    maxc = max(col_counts)
    cr = next(r for r in range(H) if row_counts[r] == maxr)
    cc = next(c for c in range(W) if col_counts[c] == maxc)
    out = [[0]*W for _ in range(H)]
    for r, c in reds:
        out[r][c] = 2
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        i = 2
        while True:
            r, c = cr + dr*i, cc + dc*i
            if not (0 <= r < H and 0 <= c < W): break
            out[r][c] = 8 if (i-2)%3 < 2 else 4
            i += 1
    for dr, dc in [(-1,-1),(-1,1),(1,-1),(1,1)]:
        j = 1
        while True:
            r, c = cr + dr*j, cc + dc*j
            if not (0 <= r < H and 0 <= c < W): break
            if out[r][c] == 0:
                out[r][c] = 1
            j += 1
    return out