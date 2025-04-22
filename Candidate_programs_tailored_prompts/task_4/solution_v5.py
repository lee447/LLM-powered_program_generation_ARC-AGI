def solve(grid):
    m, n = len(grid), len(grid[0])
    counts = {}
    for row in grid:
        for v in row:
            counts[v] = counts.get(v, 0) + 1
    bg = max(counts, key=counts.get)
    visited = [[False]*n for _ in range(m)]
    regions = []
    for r in range(m):
        for c in range(n):
            if not visited[r][c] and grid[r][c] != bg:
                color = grid[r][c]
                stack = [(r, c)]
                visited[r][c] = True
                coords = []
                while stack:
                    rr, cc = stack.pop()
                    coords.append((rr, cc))
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = rr+dr, cc+dc
                        if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == color:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
                minrow = min(rp for rp, cp in coords)
                regions.append((minrow, color, coords))
    regions.sort(key=lambda x: x[0])
    out = [[bg]*n for _ in range(m)]
    for i, (_, color, coords) in enumerate(regions):
        shift = -1 if i % 2 == 0 else 1
        for r, c in coords:
            nc = c + shift
            if 0 <= nc < n:
                out[r][nc] = color
    return out