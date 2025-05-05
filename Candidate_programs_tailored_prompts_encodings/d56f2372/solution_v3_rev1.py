from typing import List
from collections import deque

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0]) if grid else 0
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                color = grid[i][j]
                q = deque([(i,j)])
                visited[i][j] = True
                cells = []
                while q:
                    r,c = q.popleft()
                    cells.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and grid[nr][nc] == color:
                            visited[nr][nc] = True
                            q.append((nr,nc))
                comps.append((color, cells))
    best = None
    best_key = None
    for color, cells in comps:
        minr = min(r for r,c in cells)
        maxr = max(r for r,c in cells)
        minc = min(c for r,c in cells)
        maxc = max(c for r,c in cells)
        ch = maxr - minr + 1
        cw = maxc - minc + 1
        mask = [[0]*cw for _ in range(ch)]
        for r,c in cells:
            mask[r-minr][c-minc] = 1
        excl = 0
        for i in range(ch):
            for j in range(cw//2):
                a = mask[i][j]
                b = mask[i][cw-1-j]
                if (a>0) ^ (b>0):
                    excl += 1
        key = (excl, -(ch*cw))
        if best_key is None or key < best_key:
            best_key = key
            best = (color, mask)
    color, mask = best
    ch = len(mask)
    cw = len(mask[0])
    if cw % 2 == 0:
        for row in mask:
            row.append(0)
        cw += 1
    for i in range(ch):
        for j in range(cw):
            if mask[i][cw-1-j]:
                mask[i][j] = 1
    out = [[color if mask[i][j] else 0 for j in range(cw)] for i in range(ch)]
    return out