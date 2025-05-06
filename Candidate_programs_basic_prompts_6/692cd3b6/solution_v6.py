def solve(grid):
    H, W = len(grid), len(grid[0])
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    ps = []
    for r in range(H):
        for c in range(W):
            if grid[r][c] == 5:
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] == 0:
                        ps.append((nr, nc))
                        break
    for r, c in ps:
        grid[r][c] = 4
    r1, c1 = ps[0]
    r2, c2 = ps[1]
    r0, r3 = min(r1, r2), max(r1, r2)
    c0, c3 = min(c1, c2), max(c1, c2)
    for r in range(r0+1, r3+1):
        for c in range(c0, c3):
            if grid[r][c] == 0:
                grid[r][c] = 4
    return grid