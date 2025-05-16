from typing import List, Deque, Tuple
from collections import deque

def solve(grid: List[List[int]]) -> List[List[int]]:
    n, m = len(grid), len(grid[0])
    bg = 7
    vis = [[False]*m for _ in range(n)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    comps: List[Tuple[int,int,int,int,List[Tuple[int,int]]]] = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] != bg and not vis[i][j]:
                q: Deque[Tuple[int,int]] = deque([(i,j)])
                vis[i][j] = True
                pts: List[Tuple[int,int]] = []
                minr = maxr = i
                minc = maxc = j
                while q:
                    r, c = q.popleft()
                    pts.append((r, c))
                    minr = min(minr, r)
                    maxr = max(maxr, r)
                    minc = min(minc, c)
                    maxc = max(maxc, c)
                    for dr, dc in dirs:
                        rr, cc = r+dr, c+dc
                        if 0 <= rr < n and 0 <= cc < m and not vis[rr][cc] and grid[rr][cc] != bg:
                            vis[rr][cc] = True
                            q.append((rr, cc))
                h = maxr - minr + 1
                w = maxc - minc + 1
                comps.append((minr, minc, h, w, pts))
    comps = [c for c in comps if max(c[2], c[3]) >= 3]
    comps.sort(key=lambda x: x[1])
    keep = comps[:2]
    out = [[bg]*m for _ in range(n)]
    for _, _, _, _, pts in keep:
        for r, c in pts:
            out[r][c] = grid[r][c]
    return out