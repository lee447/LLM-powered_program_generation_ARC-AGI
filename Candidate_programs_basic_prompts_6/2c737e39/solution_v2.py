def solve(grid):
    h, w = len(grid), len(grid[0])
    fives = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 5]
    def has_neighbor(r, c):
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            rr, cc = r+dr, c+dc
            if 0 <= rr < h and 0 <= cc < w and grid[rr][cc] != 0:
                return True
        return False
    shape_center = next(p for p in fives if has_neighbor(*p))
    target_center = next(p for p in fives if p != shape_center)
    sr, sc = shape_center
    tr, tc = target_center
    visited = [[False]*w for _ in range(h)]
    stack = [shape_center]
    shape = []
    while stack:
        r, c = stack.pop()
        if not (0 <= r < h and 0 <= c < w): continue
        if visited[r][c] or grid[r][c] == 0: continue
        visited[r][c] = True
        shape.append((r, c))
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            stack.append((r+dr, c+dc))
    out = [row[:] for row in grid]
    out[tr][tc] = 0
    for r, c in shape:
        v = grid[r][c]
        if v == 5: continue
        nr, nc = tr + (r - sr), tc + (c - sc)
        if 0 <= nr < h and 0 <= nc < w:
            out[nr][nc] = v
    return out