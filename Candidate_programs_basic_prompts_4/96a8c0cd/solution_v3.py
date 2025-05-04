def solve(grid):
    H, W = len(grid), len(grid[0])
    seen = [[False]*W for _ in range(H)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    comps = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] not in (0,2) and not seen[i][j]:
                color = grid[i][j]
                stack = [(i,j)]
                seen[i][j] = True
                cells = []
                while stack:
                    r,c = stack.pop()
                    cells.append((r,c))
                    for dr,dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < H and 0 <= nc < W and not seen[nr][nc] and grid[nr][nc] == color:
                            seen[nr][nc] = True
                            stack.append((nr,nc))
                comps.append(cells)
    out = [row[:] for row in grid]
    for cells in comps:
        rs = [r for r,c in cells]
        cs = [c for r,c in cells]
        r0, r1, c0, c1 = min(rs), max(rs), min(cs), max(cs)
        for c in range(c0, c1+1):
            for dr in (-1, 1):
                rr = r0+dr if dr<0 else r1+dr
                if 0 <= rr < H and 0 <= c < W and out[rr][c] == 0:
                    out[rr][c] = 2
        for r in range(r0, r1+1):
            for dc in (-1, 1):
                cc = c0+dc if dc<0 else c1+dc
                if 0 <= r < H and 0 <= cc < W and out[r][cc] == 0:
                    out[r][cc] = 2
    return out