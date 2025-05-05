from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    comps_by_color = {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v != 0 and not visited[r][c]:
                stack = [(r, c)]
                visited[r][c] = True
                comp = []
                while stack:
                    i, j = stack.pop()
                    comp.append((i, j))
                    for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
                        ni, nj = i+di, j+dj
                        if 0 <= ni < h and 0 <= nj < w and not visited[ni][nj] and grid[ni][nj] == v:
                            visited[ni][nj] = True
                            stack.append((ni, nj))
                comps_by_color.setdefault(v, []).append(comp)
    shapes = []
    gap = 1
    for v, comps in comps_by_color.items():
        if len(comps) != 2:
            continue
        c1, c2 = comps
        s1, s2 = len(c1), len(c2)
        if s1 != s2:
            comp_small, comp_big = (c1, c2) if s1 < s2 else (c2, c1)
        else:
            r1 = min(r for r,_ in c1)
            r2 = min(r for r,_ in c2)
            comp_small, comp_big = (c1, c2) if r1 < r2 else (c2, c1)
        rs, cs = zip(*comp_small)
        rb, cb = zip(*comp_big)
        min_rs, max_rs = min(rs), max(rs)
        min_cs, max_cs = min(cs), max(cs)
        min_rb, max_rb = min(rb), max(rb)
        min_cb, max_cb = min(cb), max(cb)
        shift_big = (h-1) - max_rb
        lower_top = min_rb + shift_big
        shift_small = (lower_top - gap - 1) - max_rs
        shape_min_c = min(min_cs, min_cb)
        width_small = max_cs - min_cs + 1
        width_big = max_cb - min_cb + 1
        shapes.append((shape_min_c, v, comp_small, comp_big, shift_small, shift_big, min_cs, min_cb, width_small, width_big))
    shapes.sort(key=lambda x: x[0])
    out = [[0]*w for _ in range(h)]
    cur_x = 0
    for _, v, comp_small, comp_big, shs, shb, min_cs, min_cb, ws, wb in shapes:
        dxs = cur_x - min_cs
        dxb = cur_x - min_cb
        for r, c in comp_small:
            out[r + shs][c + dxs] = v
        for r, c in comp_big:
            out[r + shb][c + dxb] = v
        cur_x += max(ws, wb) + gap
    return out