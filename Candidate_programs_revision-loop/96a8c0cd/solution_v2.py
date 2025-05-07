from typing import List, Tuple
from collections import deque

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def inb(r,c): return 0 <= r < h and 0 <= c < w
    # find seed
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 2:
                seed = (r,c)
    # flood fill clusters of size 3
    seen = [[False]*w for _ in range(h)]
    clusters = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] not in (0,2) and not seen[r][c]:
                color = grid[r][c]
                q = [(r,c)]
                comp = []
                seen[r][c] = True
                for x,y in q:
                    comp.append((x,y))
                    for dr,dc in dirs:
                        nr, nc = x+dr, y+dc
                        if inb(nr,nc) and not seen[nr][nc] and grid[nr][nc]==color:
                            seen[nr][nc] = True
                            q.append((nr,nc))
                if len(comp)==3:
                    # center = median cell
                    comp.sort()
                    clusters.append(comp[1])
    # sort by distance from seed
    clusters.sort(key=lambda x: abs(x[0]-seed[0]) + abs(x[1]-seed[1]))
    # pathfind and draw
    for tgt in clusters:
        sr, sc = seed
        tr, tc = tgt
        # BFS
        q = deque()
        q.append((sr,sc))
        prev = { (sr,sc): None }
        while q:
            r,c = q.popleft()
            if (r,c) == (tr,tc):
                break
            for dr,dc in dirs:
                nr, nc = r+dr, c+dc
                if inb(nr,nc) and (nr,nc) not in prev:
                    v = grid[nr][nc]
                    if (nr,nc)==(tr,tc) or v==0 or v==2:
                        prev[(nr,nc)] = (r,c)
                        q.append((nr,nc))
        # backtrack
        cur = (tr,tc)
        while cur and cur != seed:
            pr = prev[cur]
            if pr and grid[cur[0]][cur[1]] == 0:
                grid[cur[0]][cur[1]] = 2
            cur = pr
    return grid