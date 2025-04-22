from typing import List
from collections import deque

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    orig = grid
    out = [row[:] for row in orig]
    visited = [[False]*W for _ in range(H)]
    comps = []
    for i in range(H):
        for j in range(W):
            v = orig[i][j]
            if v > 1 and not visited[i][j]:
                dq = deque([(i, j)])
                visited[i][j] = True
                cells = [(i, j)]
                while dq:
                    r, c = dq.popleft()
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc] and orig[nr][nc] == v:
                            visited[nr][nc] = True
                            dq.append((nr, nc))
                            cells.append((nr, nc))
                rs = [r for r, c in cells]
                cs = [c for r, c in cells]
                minR, maxR, minC, maxC = min(rs), max(rs), min(cs), max(cs)
                area = (maxR-minR)*(maxC-minC)
                comps.append((area, v, minR, maxR, minC, maxC))
    comps.sort()
    for _, v, minR, maxR, minC, maxC in comps:
        c1 = None
        for c in range(minC-1, -1, -1):
            if all(orig[r][c] == 1 for r in range(minR, maxR+1)):
                c1 = c
                break
        if c1 is None:
            continue
        c2 = None
        for c in range(maxC+1, W):
            if all(orig[r][c] == 1 for r in range(minR, maxR+1)):
                c2 = c
                break
        if c2 is None:
            continue
        r1 = None
        for r in range(minR-1, -1, -1):
            if all(orig[r][c] == 1 for c in range(c1, c2+1)):
                r1 = r
                break
        if r1 is None:
            continue
        r2 = None
        for r in range(maxR+1, H):
            if all(orig[r][c] == 1 for c in range(c1, c2+1)):
                r2 = r
                break
        if r2 is None:
            continue
        if not all(orig[r1][c] == 1 and orig[r2][c] == 1 for c in range(c1, c2+1)):
            continue
        if not all(orig[r][c1] == 1 and orig[r][c2] == 1 for r in range(r1, r2+1)):
            continue
        for r in range(r1+1, r2):
            for c in range(c1+1, c2):
                if out[r][c] == 1:
                    out[r][c] = v
    return out