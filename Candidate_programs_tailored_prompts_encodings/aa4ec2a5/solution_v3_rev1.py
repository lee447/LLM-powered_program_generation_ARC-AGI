from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    orig = [row[:] for row in grid]
    vis = [[False] * w for _ in range(h)]
    clusters = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and not vis[i][j]:
                stack = [(i, j)]
                vis[i][j] = True
                comp = {(i, j)}
                while stack:
                    r, c = stack.pop()
                    for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                        if 0 <= nr < h and 0 <= nc < w and not vis[nr][nc] and grid[nr][nc] == 1:
                            vis[nr][nc] = True
                            stack.append((nr, nc))
                            comp.add((nr, nc))
                clusters.append(comp)
    clusters.sort(key=lambda c: len(c), reverse=True)
    out = [row[:] for row in grid]
    for idx, comp in enumerate(clusters):
        if idx == 0:
            maxd = 3
            cmap = {1: 2, 2: 8, 3: 6}
        else:
            maxd = 1
            cmap = {1: 2}
        dil = [comp]
        for d in range(1, maxd + 1):
            nxt = set(dil[d-1])
            for r, c in dil[d-1]:
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < h and 0 <= nc < w:
                            nxt.add((nr, nc))
            dil.append(nxt)
        for d in range(1, maxd + 1):
            ring = dil[d] - dil[d-1]
            col = cmap[d]
            for r, c in ring:
                if orig[r][c] != 1 and out[r][c] == orig[r][c]:
                    out[r][c] = col
    return out