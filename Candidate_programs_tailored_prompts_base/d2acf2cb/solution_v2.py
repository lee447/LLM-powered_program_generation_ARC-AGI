from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    anchors = [(r,c) for r in range(h) for c in range(w) if grid[r][c]==4]
    rows = {}
    for r,c in anchors:
        rows.setdefault(r, []).append(c)
    stripes = [(r, sorted(cs)[0], sorted(cs)[1]) for r,cs in rows.items() if len(cs)==2]
    if len(anchors)==4:
        rs = sorted(set(r for r,_ in anchors))
        cs = sorted(set(c for _,c in anchors))
        r1, r2 = rs[0], rs[1]
        c1, c2 = cs[0], cs[1]
        for r in range(r1+1, r2):
            left = grid[r][:c1]
            right = grid[r][c2+1:]
            if any(v==6 for v in left):
                res[r][c1] = 8
            if any(v==6 for v in right):
                res[r][c2] = 7
        return res
    for r, c1, c2 in stripes:
        seq = grid[r][c1+1:c2]
        order = []
        for v in seq:
            if v not in order:
                order.append(v)
        if set(order)=={0,6}:
            m = {order[0]:8, order[1]:7}
        else:
            m = {order[0]:6, order[1]:0}
        for c in range(c1+1, c2):
            v = grid[r][c]
            if v in m:
                res[r][c] = m[v]
    return res