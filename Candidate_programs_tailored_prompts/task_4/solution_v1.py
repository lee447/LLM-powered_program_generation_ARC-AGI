def solve(grid):
    h, w = len(grid), len(grid[0])
    counts = {}
    for row in grid:
        for v in row:
            counts[v] = counts.get(v, 0) + 1
    bg = max(counts, key=counts.get)
    visited = [[False]*w for _ in range(h)]
    regions = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != bg and not visited[i][j]:
                color = grid[i][j]
                stack = [(i,j)]
                coords = []
                visited[i][j] = True
                top = i
                while stack:
                    r,c = stack.pop()
                    coords.append((r,c))
                    if r < top: top = r
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        rr,cc = r+dr, c+dc
                        if 0 <= rr < h and 0 <= cc < w and not visited[rr][cc] and grid[rr][cc] == color:
                            visited[rr][cc] = True
                            stack.append((rr,cc))
                regions.append((top, color, coords))
    regions.sort(key=lambda x: x[0])
    new = [[bg]*w for _ in range(h)]
    for idx, (_top, color, coords) in enumerate(regions):
        shift = -1 if idx % 2 == 0 else 1
        for r,c in coords:
            new[r][c+shift] = color
    return new