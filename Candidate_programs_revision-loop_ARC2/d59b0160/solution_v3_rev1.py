from typing import List, Deque, Tuple
from collections import deque

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    bg = 7
    vis = [[False]*n for _ in range(n)]
    dirs = ((1,0),(-1,0),(0,1),(0,-1))
    comps: List[Tuple[int,int,int,int,List[Tuple[int,int]]]] = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] != bg and not vis[i][j]:
                q: Deque[Tuple[int,int]] = deque()
                q.append((i,j))
                vis[i][j] = True
                pts: List[Tuple[int,int]] = []
                minr, maxr, minc, maxc = i, i, j, j
                while q:
                    r,c = q.popleft()
                    pts.append((r,c))
                    minr = min(minr, r)
                    maxr = max(maxr, r)
                    minc = min(minc, c)
                    maxc = max(maxc, c)
                    for dr,dc in dirs:
                        rr,cc = r+dr, c+dc
                        if 0 <= rr < n and 0 <= cc < n and not vis[rr][cc] and grid[rr][cc] != bg:
                            vis[rr][cc] = True
                            q.append((rr,cc))
                h = maxr - minr + 1
                w = maxc - minc + 1
                comps.append((minr, minc, h, w, pts))
    out = [[bg]*n for _ in range(n)]
    for r0,c0,h,w,pts in comps:
        if max(h,w) >= 3:
            for r in range(r0, r0+h):
                for c in range(c0, c0+w):
                    out[r][c] = grid[r][c]
    return out