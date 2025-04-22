def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = grid[0][0]
    visited = [[False]*w for _ in range(h)]
    comps = []
    for r in range(h):
        for c in range(w):
            if not visited[r][c] and grid[r][c] != bg:
                color = grid[r][c]
                stack = [(r, c)]
                visited[r][c] = True
                cells = []
                top = r
                while stack:
                    rr, cc = stack.pop()
                    cells.append((rr, cc))
                    if rr < top:
                        top = rr
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = rr+dr, cc+dc
                        if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and grid[nr][nc] == color:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
                comps.append((top, color, cells))
    comps.sort(key=lambda x: x[0])
    new = [[bg]*w for _ in range(h)]
    for i, (_, color, cells) in enumerate(comps):
        shift = -1 if i % 2 == 0 else 1
        for r, c in cells:
            new[r][c+shift] = color
    return new