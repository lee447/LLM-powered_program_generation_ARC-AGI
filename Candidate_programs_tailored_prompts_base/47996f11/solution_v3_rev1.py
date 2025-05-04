from typing import List, Tuple
from collections import deque

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    visited = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if grid[i][j]==6 and not visited[i][j]:
                q = deque([(i,j)])
                visited[i][j]=True
                comp = []
                while q:
                    x,y = q.popleft()
                    comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and grid[nx][ny]==6:
                            visited[nx][ny]=True
                            q.append((nx,ny))
                rs = [x for x,_ in comp]
                cs = [y for _,y in comp]
                r0,r1 = min(rs), max(rs)
                c0,c1 = min(cs), max(cs)
                comps.append((len(comp), comp, (r0,r1,c0,c1)))
    if not comps:
        return out
    max_area = max(a for a,_,_ in comps)
    stripes = []
    for a, comp, bb in comps:
        if a*2 >= max_area:
            stripes.append((comp, bb))
        else:
            for x,y in comp:
                out[x][y] = 9
    for comp, (r0,r1,c0,c1) in stripes:
        for x,y in comp:
            out[x][y] = 7
        for cc in (c0-1, c1+1):
            if 0 <= cc < w:
                for x in range(h):
                    if grid[x][cc]==8 and (x==r0 or x==r1):
                        out[x][cc] = 9
    for i in range(h-1):
        for j in range(w-1):
            if grid[i][j]==5 and grid[i][j+1]==5 and grid[i+1][j]==5 and grid[i+1][j+1]==5:
                for dr,dc in ((-2,-2),(-2,2),(2,-2),(2,2)):
                    ri, cj = i+dr, j+dc
                    if 0<=ri<h-1 and 0<=cj<w-1:
                        block = [grid[ri][cj],grid[ri][cj+1],grid[ri+1][cj],grid[ri+1][cj+1]]
                        if set(block)=={1,3}:
                            for dx in (0,1):
                                for dy in (0,1):
                                    x,y = ri+dx, cj+dy
                                    out[x][y] = 1 if grid[x][y]==3 else 3
    for comp, (r0,r1,c0,c1) in stripes:
        for r in range(h):
            runs = []
            cur = grid[r][0]
            start = 0
            for c in range(1,w+1):
                v = grid[r][c] if c<w else None
                if v==cur and cur in (2,8):
                    continue
                else:
                    if cur in (2,8):
                        runs.append((start, c-1, cur))
                    cur = v
                    start = c
            for a,b,val in runs:
                if b+1==c0 or a-1==c1:
                    idx = b if b+1==c0 else a
                    out[r][idx] = None
    for r in range(h):
        row = [c for c in out[r] if c is not None]
        while len(row)<w:
            row.insert(0, 0)
        out[r] = row
    return out