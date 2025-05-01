def solve(grid):
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]==1 and not visited[i][j]:
                stack = [(i,j)]
                visited[i][j] = True
                cells = []
                while stack:
                    r,c = stack.pop()
                    cells.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and not visited[nr][nc] and grid[nr][nc]==1:
                            visited[nr][nc] = True
                            stack.append((nr,nc))
                comps.append(cells)
    shape_to_color = {}
    for cells in comps:
        seeds = set()
        for r,c in cells:
            for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr,nc = r+dr, c+dc
                if 0<=nr<h and 0<=nc<w and grid[nr][nc] not in (0,1):
                    seeds.add(grid[nr][nc])
        if len(seeds)==1:
            color = seeds.pop()
            minr = min(r for r,c in cells)
            minc = min(c for r,c in cells)
            shape = frozenset((r-minr,c-minc) for r,c in cells)
            shape_to_color[shape] = color
    out = [row[:] for row in grid]
    for cells in comps:
        minr = min(r for r,c in cells)
        minc = min(c for r,c in cells)
        shape = frozenset((r-minr,c-minc) for r,c in cells)
        if shape in shape_to_color:
            col = shape_to_color[shape]
            for r,c in cells:
                out[r][c] = col
    return out