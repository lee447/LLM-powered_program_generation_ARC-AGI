from typing import List
from collections import deque

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def inb(r,c): return 0 <= r < h and 0 <= c < w
    seed = None
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 2:
                seed = (r,c)
                break
        if seed: break
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 2:
                grid[r][c] = 0
    seen = [[False]*w for _ in range(h)]
    centers = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] not in (0,2) and not seen[r][c]:
                color = grid[r][c]
                q = [(r,c)]
                seen[r][c] = True
                comp = []
                for x,y in q:
                    comp.append((x,y))
                    for dr,dc in dirs:
                        nr, nc = x+dr, y+dc
                        if inb(nr,nc) and not seen[nr][nc] and grid[nr][nc] == color:
                            seen[nr][nc] = True
                            q.append((nr,nc))
                if len(comp) == 3:
                    comp.sort()
                    centers.append(comp[1])
    order = []
    cur = seed
    while centers:
        nxt = min(centers, key=lambda p: abs(p[0]-cur[0]) + abs(p[1]-cur[1]))
        order.append(nxt)
        centers.remove(nxt)
        cur = nxt
    def bfs_path(start, target, allow):
        prev = {start: None}
        dq = deque([start])
        while dq:
            u = dq.popleft()
            if u == target: break
            for dr,dc in dirs:
                v = (u[0]+dr, u[1]+dc)
                if inb(*v) and v not in prev and allow(v):
                    prev[v] = u
                    dq.append(v)
        path = []
        if target in prev:
            u = target
            while prev[u] is not None:
                path.append(u)
                u = prev[u]
        return path
    cur = seed
    for tgt in order:
        path = bfs_path(cur, tgt, lambda v: grid[v[0]][v[1]] == 0 or v == tgt)
        for u in path:
            if grid[u[0]][u[1]] == 0:
                grid[u[0]][u[1]] = 2
        cur = tgt
    exit_path = bfs_path(cur, None, lambda v: grid[v[0]][v[1]] == 0 or v == cur)  # placeholder
    prev = {cur: None}
    dq = deque([cur])
    exit_cell = None
    while dq:
        u = dq.popleft()
        r,c = u
        if r == 0 or r == h-1 or c == 0 or c == w-1:
            exit_cell = u
            break
        for dr,dc in dirs:
            v = (r+dr, c+dc)
            if inb(*v) and v not in prev and grid[v[0]][v[1]] == 0:
                prev[v] = u
                dq.append(v)
    if exit_cell:
        u = exit_cell
        while prev[u] is not None:
            if grid[u[0]][u[1]] == 0:
                grid[u[0]][u[1]] = 2
            u = prev[u]
    return grid