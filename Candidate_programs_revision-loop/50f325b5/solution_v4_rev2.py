from typing import List
from collections import deque

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    # find the 8-shape component
    seen = [[False]*w for _ in range(h)]
    comp8 = []
    for y in range(h):
        for x in range(w):
            if grid[y][x] == 8:
                start = (y, x)
                comp8 = []
                dq = deque([start])
                seen[y][x] = True
                while dq:
                    cy, cx = dq.popleft()
                    comp8.append((cy, cx))
                    for dy, dx in dirs:
                        ny, nx = cy+dy, cx+dx
                        if 0 <= ny < h and 0 <= nx < w and not seen[ny][nx] and grid[ny][nx] == 8:
                            seen[ny][nx] = True
                            dq.append((ny, nx))
                break
        if comp8:
            break
    if not comp8:
        return grid
    N = len(comp8)
    # find center of 8-shape (node with degree >= 3)
    S8 = set(comp8)
    center8 = None
    for y, x in comp8:
        deg = sum((y+dy, x+dx) in S8 for dy, dx in dirs)
        if deg >= 3:
            center8 = (y, x)
            break
    if center8 is None:
        # fallback to node with deg >= 2
        for y, x in comp8:
            deg = sum((y+dy, x+dx) in S8 for dy, dx in dirs)
            if deg >= 2:
                center8 = (y, x)
                break
    cy8, cx8 = center8
    offs8 = sorted((y-cy8, x-cx8) for y, x in comp8)
    # generate rotations of offs8
    rots = []
    for r in range(4):
        if r == 0:
            rset = offs8
        elif r == 1:
            rset = sorted((-dx, dy) for dy, dx in offs8)
        elif r == 2:
            rset = sorted((-dy, -dx) for dy, dx in offs8)
        else:
            rset = sorted((dx, -dy) for dy, dx in offs8)
        rots.append(rset)
    out = [row[:] for row in grid]
    visited = [[False]*w for _ in range(h)]
    for y0 in range(h):
        for x0 in range(w):
            if visited[y0][x0]:
                continue
            c = grid[y0][x0]
            if c == 0 or c == 8:
                continue
            # bfs component of c
            comp = []
            dq = deque([(y0, x0)])
            visited[y0][x0] = True
            while dq:
                y, x = dq.popleft()
                comp.append((y, x))
                for dy, dx in dirs:
                    ny, nx = y+dy, x+dx
                    if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx] and grid[ny][nx] == c:
                        visited[ny][nx] = True
                        dq.append((ny, nx))
            if len(comp) != N:
                continue
            # find center(s) of this comp (deg>=2)
            Scomp = set(comp)
            centers = []
            for y, x in comp:
                deg = sum((y+dy, x+dx) in Scomp for dy, dx in dirs)
                if deg >= 2:
                    centers.append((y, x))
            # try each center
            matched = False
            for cy, cx in centers:
                offs = sorted((y-cy, x-cx) for y, x in comp)
                for rset in rots:
                    if offs == rset:
                        # match; fill
                        for y, x in comp:
                            out[y][x] = 8
                        matched = True
                        break
                if matched:
                    break
    return out