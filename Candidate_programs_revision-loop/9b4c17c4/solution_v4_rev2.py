from typing import List, Tuple
from collections import deque
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    counts = {}
    for i in range(H):
        for j in range(W):
            counts[grid[i][j]] = counts.get(grid[i][j], 0) + 1
    fg = min(counts, key=counts.get)
    bgs = [c for c in counts if c != fg]
    bbox = {}
    for c in bgs:
        min_x, max_x, min_y, max_y = H, -1, W, -1
        for i in range(H):
            for j in range(W):
                if grid[i][j] == c:
                    if i < min_x: min_x = i
                    if i > max_x: max_x = i
                    if j < min_y: min_y = j
                    if j > max_y: max_y = j
        bbox[c] = (min_x, max_x, min_y, max_y)
    b0, b1 = bgs[0], bgs[1]
    hpart = bbox[b0][2] == 0 and bbox[b0][3] == W-1 and bbox[b1][2] == 0 and bbox[b1][3] == W-1
    vpart = bbox[b0][0] == 0 and bbox[b0][1] == H-1 and bbox[b1][0] == 0 and bbox[b1][1] == H-1
    seen = [[False]*W for _ in range(H)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    comps = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] == fg and not seen[i][j]:
                dq = deque([(i,j)])
                seen[i][j] = True
                comp = []
                while dq:
                    x,y = dq.popleft()
                    comp.append((x,y))
                    for dx,dy in dirs:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < H and 0 <= ny < W and not seen[nx][ny] and grid[nx][ny] == fg:
                            seen[nx][ny] = True
                            dq.append((nx, ny))
                comps.append(comp)
    out = [row[:] for row in grid]
    for comp in comps:
        rs = [x for x,_ in comp]; cs = [y for _,y in comp]
        minr, maxr = min(rs), max(rs)
        minc, maxc = min(cs), max(cs)
        if hpart:
            if minr <= bbox[b0][1]:
                bcol = b0
            else:
                bcol = b1
            region_min_y, region_max_y = 0, W-1
        else:
            if minc <= bbox[b0][3]:
                bcol = b0
            else:
                bcol = b1
            region_min_y, region_max_y = bbox[bcol][2], bbox[bcol][3]
        other_bg = b1 if bcol == b0 else b0
        width = maxc - minc + 1
        if bcol < other_bg:
            new_min = region_max_y - width + 1
        else:
            new_min = region_min_y
        for x,y in comp:
            out[x][y] = bcol
        for x,y in comp:
            out[x][new_min + (y - minc)] = fg
    return out