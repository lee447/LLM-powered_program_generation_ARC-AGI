from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    counts = {}
    for row in grid:
        for v in row:
            counts[v] = counts.get(v, 0) + 1
    bg = max(counts, key=lambda k: counts[k])
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and grid[i][j] != bg:
                color = grid[i][j]
                stack = [(i, j)]
                visited[i][j] = True
                comp = []
                minr = i
                while stack:
                    r, c = stack.pop()
                    comp.append((r, c))
                    if r < minr:
                        minr = r
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and grid[nr][nc] == color:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
                comps.append((minr, comp, color))
    comps.sort(key=lambda x: x[0])
    new = [[bg]*w for _ in range(h)]
    for idx, (_, comp, color) in enumerate(comps):
        d = -1 if idx % 2 == 0 else 1
        for r, c in comp:
            new[r][c + d] = color
    return new