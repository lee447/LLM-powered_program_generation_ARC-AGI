def solve(grid):
    H, W = len(grid), len(grid[0])
    center = None
    for r in range(H):
        for c in range(W):
            if grid[r][c] == 2:
                cnt = 0
                if r > 0 and grid[r-1][c] == 2: cnt += 1
                if r < H-1 and grid[r+1][c] == 2: cnt += 1
                if c > 0 and grid[r][c-1] == 2: cnt += 1
                if c < W-1 and grid[r][c+1] == 2: cnt += 1
                if cnt == 4:
                    center = (r, c)
                    break
        if center:
            break
    r0, c0 = center
    out = [[0]*W for _ in range(H)]
    out[r0][c0] = 2
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        d = 1
        while True:
            r, c = r0 + dr*d, c0 + dc*d
            if not (0 <= r < H and 0 <= c < W):
                break
            if d == 1:
                v = 2
            else:
                v = 4 if (d-2) % 3 == 2 else 8
            out[r][c] = v
            d += 1
    for dr, dc in [(-1,-1),(-1,1),(1,-1),(1,1)]:
        d = 1
        while True:
            r, c = r0 + dr*d, c0 + dc*d
            if not (0 <= r < H and 0 <= c < W):
                break
            out[r][c] = 1
            d += 1
    return out