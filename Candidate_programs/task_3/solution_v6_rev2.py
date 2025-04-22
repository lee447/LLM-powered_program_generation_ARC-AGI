from typing import List
from collections import deque

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    visited = [[False]*W for _ in range(H)]
    comps = []
    for i in range(H):
        for j in range(W):
            v = grid[i][j]
            if v > 1 and not visited[i][j]:
                dq = deque([(i, j)])
                visited[i][j] = True
                cells = [(i, j)]
                while dq:
                    r, c = dq.popleft()
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc] and grid[nr][nc] == v:
                            visited[nr][nc] = True
                            dq.append((nr, nc))
                            cells.append((nr, nc))
                rs = [r for r, _ in cells]
                cs = [c for _, c in cells]
                minR, maxR, minC, maxC = min(rs), max(rs), min(cs), max(cs)
                comps.append((minR, maxR, minC, maxC, v))
    comps.sort(key=lambda x: (x[1]-x[0])*(x[3]-x[2]))
    out = [row[:] for row in grid]
    for minR, maxR, minC, maxC, v in comps:
        top = None
        for rr in range(minR-1, -1, -1):
            if all(grid[rr][c] == 1 for c in range(minC, maxC+1)):
                top = rr
                break
        if top is None: continue
        bottom = None
        for rr in range(maxR+1, H):
            if all(grid[rr][c] == 1 for c in range(minC, maxC+1)):
                bottom = rr
                break
        if bottom is None: continue
        left = None
        for cc in range(minC-1, -1, -1):
            if all(grid[r][cc] == 1 for r in range(top, bottom+1)):
                left = cc
                break
        if left is None: continue
        right = None
        for cc in range(maxC+1, W):
            if all(grid[r][cc] == 1 for r in range(top, bottom+1)):
                right = cc
                break
        if right is None: continue
        for r in range(top+1, bottom):
            for c in range(left+1, right):
                if out[r][c] == 1:
                    out[r][c] = v
    return out