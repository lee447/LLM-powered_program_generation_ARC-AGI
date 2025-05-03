from typing import List
from collections import deque

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    full4 = [r for r in range(H) if all(grid[r][c] == 4 for c in range(W))]
    bounds = [-1] + full4 + [H]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(len(bounds)-1):
        top, bottom = bounds[i]+1, bounds[i+1]-1
        if top > bottom: continue
        visited = [[False]*W for _ in range(H)]
        comps = []
        for r in range(top, bottom+1):
            for c in range(W):
                if visited[r][c]: continue
                v = grid[r][c]
                if v in (0,4): continue
                visited[r][c] = True
                q = deque([(r,c)])
                comp = [(r,c)]
                while q:
                    pr, pc = q.popleft()
                    for dr, dc in dirs:
                        nr, nc = pr+dr, pc+dc
                        if top <= nr <= bottom and 0 <= nc < W and not visited[nr][nc] and grid[nr][nc] == v:
                            visited[nr][nc] = True
                            q.append((nr,nc))
                            comp.append((nr,nc))
                comps.append((v, comp))
        seeds = [(v, c) for v,c in comps if v != 1 and len(c) > 1]
        ones = [c for v,c in comps if v == 1 and len(c) > 1]
        used = [False]*len(ones)
        changes = {}
        for color, sc in seeds:
            for j, oc in enumerate(ones):
                if used[j] or len(oc) != len(sc): continue
                sset = set(sc)
                oset = set(oc)
                found = False
                for ax, ay in sc:
                    for bx, by in oc:
                        dr, dc = bx-ax, by-ay
                        if all((x+dr, y+dc) in oset for x,y in sc):
                            for x,y in sc:
                                changes[(x,y)] = 1
                            for x,y in oc:
                                changes[(x,y)] = color
                            used[j] = True
                            found = True
                            break
                    if found: break
                if found: break
        for (r,c), v in changes.items():
            grid[r][c] = v
    return grid