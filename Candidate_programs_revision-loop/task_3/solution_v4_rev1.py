from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and not visited[i][j]:
                stack = [(i, j)]
                visited[i][j] = True
                cells = []
                while stack:
                    r, c = stack.pop()
                    cells.append((r, c))
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and grid[nr][nc] == 1:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
                comps.append(cells)
    shape_map = {}
    for cells in comps:
        cells_set = set(cells)
        seeds = set()
        for r, c in cells:
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r+dr, c+dc
                if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] not in (0,1):
                    seeds.add(grid[nr][nc])
        if len(seeds) == 1:
            color = seeds.pop()
            minr = min(r for r,c in cells)
            minc = min(c for r,c in cells)
            maxr = max(r for r,c in cells)
            maxc = max(c for r,c in cells)
            shape = frozenset((r-minr, c-minc) for r,c in cells)
            if shape not in shape_map:
                interior = set()
                if maxr-minr == 0 and maxc-minc >= 2:
                    for r, c in cells:
                        if (r, c-1) in cells_set and (r, c+1) in cells_set:
                            interior.add((r-minr, c-minc))
                elif maxc-minc == 0 and maxr-minr >= 2:
                    for r, c in cells:
                        if (r-1, c) in cells_set and (r+1, c) in cells_set:
                            interior.add((r-minr, c-minc))
                else:
                    for r, c in cells:
                        if ((r-1, c) in cells_set and (r+1, c) in cells_set and
                            (r, c-1) in cells_set and (r, c+1) in cells_set):
                            interior.add((r-minr, c-minc))
                shape_map[shape] = (color, interior)
    out = [row[:] for row in grid]
    for cells in comps:
        minr = min(r for r,c in cells)
        minc = min(c for r,c in cells)
        shape = frozenset((r-minr, c-minc) for r,c in cells)
        if shape in shape_map:
            color, interior = shape_map[shape]
            for dr, dc in interior:
                r, c = minr+dr, minc+dc
                if out[r][c] == 1:
                    out[r][c] = color
    return out