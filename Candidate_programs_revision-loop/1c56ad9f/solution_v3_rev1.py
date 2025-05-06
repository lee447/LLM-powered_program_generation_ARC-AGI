def solve(grid):
    R, C = len(grid), len(grid[0])
    color = next(v for row in grid for v in row if v != 0)
    H = sorted(r for r in range(R) if any(grid[r][c] == color and grid[r][c+1] == color for c in range(C-1)))
    V = sorted(c for c in range(C) if any(grid[r][c] == color and grid[r+1][c] == color for r in range(R-1)))
    out = [[0]*C for _ in range(R)]
    for i, r in enumerate(H):
        shift = 1 if i % 2 == 1 else 0
        for c in range(C):
            if grid[r][c] == color:
                nc = c + shift
                if 0 <= nc < C:
                    out[r][nc] = color
    for c in V:
        for r in range(R):
            if grid[r][c] == color and not ((c>0 and grid[r][c-1]==color) or (c<C-1 and grid[r][c+1]==color)):
                for idx in range(len(H)-1):
                    if H[idx] < r < H[idx+1]:
                        seg = r - H[idx] - 1
                        dy = -1 if seg % 2 == 0 else 0
                        nr = r + dy
                        if 0 <= nr < R and nr not in H:
                            out[nr][c] = color
                        break
    return out