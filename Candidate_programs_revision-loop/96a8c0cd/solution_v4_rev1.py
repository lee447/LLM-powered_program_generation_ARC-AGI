from typing import List
from collections import deque

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def inb(r,c): return 0 <= r < h and 0 <= c < w
    seen = [[False]*w for _ in range(h)]
    comps2 = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 2 and not seen[r][c]:
                q = [(r,c)]
                seen[r][c] = True
                comp = []
                for x,y in q:
                    comp.append((x,y))
                    for dr,dc in dirs:
                        nr, nc = x+dr, y+dc
                        if inb(nr,nc) and not seen[nr][nc] and grid[nr][nc] == 2:
                            seen[nr][nc] = True
                            q.append((nr,nc))
                comps2.append(comp)
    seed_comp = min(comps2, key=len)
    seed = seed_comp[0]
    seen = [[False]*w for _ in range(h)]
    clusters_by_color = {}
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
                    center = comp[1]
                    clusters_by_color.setdefault(color, []).append(center)
    order = []
    current = seed
    for color in sorted(clusters_by_color.keys(), reverse=True):
        sub = clusters_by_color[color][:]
        while sub:
            nxt = min(sub, key=lambda x: abs(x[0]-current[0]) + abs(x[1]-current[1]))
            order.append(nxt)
            sub.remove(nxt)
            current = nxt
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 2 and (r,c) != seed:
                grid[r][c] = 0
    current = seed
    for tgt in order:
        prev = {current: None}
        dq = deque([current])
        while dq:
            u = dq.popleft()
            if u == tgt:
                break
            for dr,dc in dirs:
                v = (u[0]+dr, u[1]+dc)
                if inb(*v) and v not in prev and (grid[v[0]][v[1]] == 0 or v == tgt):
                    prev[v] = u
                    dq.append(v)
        u = tgt
        while prev[u] is not None:
            p = prev[u]
            if u != tgt and grid[u[0]][u[1]] == 0:
                grid[u[0]][u[1]] = 2
            u = p
        current = tgt
    prev = {current: None}
    dq = deque([current])
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
    grid[seed[0]][seed[1]] = 0
    return grid